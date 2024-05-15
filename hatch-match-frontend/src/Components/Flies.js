import '../Styles/flies.css'
import React, { useEffect, useState } from "react";
import FlyPopUp from './FlyPopUp';

function Flies({flies, selectedFly, setSelectedFly, isOpen, setIsOpen, togglePopup, searchValue}) {

    const [selectedType, setSelectedType] = useState('')
    const [selectedCycle, setSelectedCycle] = useState('')
    const [selectedSpecies, setSelectedSpecies] = useState('')
    
    const [searchResult, setSearchResult] = useState([])
    const [currentPage, setCurrentPage] = useState(1);
    const [cardsPerPage] = useState(12);
    

    useEffect(() => {
        filterFlies();
    }, [selectedType, selectedCycle, selectedSpecies, searchValue, flies]);

    useEffect(() => {
        setCurrentPage(1); 
    }, [selectedType, selectedCycle, selectedSpecies, searchValue, flies]);

    function filterFlies() {
        let filteredFlies = flies.filter(fly => {
            const typeMatch = !selectedType || fly[3] === selectedType;
            const cycleMatch = !selectedCycle || fly[5] === selectedCycle;
            const speciesMatch = !selectedSpecies || fly[4] === selectedSpecies;
            const searchMatch = fly[1].toLowerCase().includes(searchValue.toLowerCase());
            return typeMatch && cycleMatch && speciesMatch && searchMatch;
        });
        console.log(filteredFlies)
        setSearchResult(filteredFlies);
    }

    function handleTypeChange(e) {
        setSelectedType(e.target.value);
    }

    function handleCycleChange(e) {
        setSelectedCycle(e.target.value);
    }

    function handleSpeciesChange(e) {
        setSelectedSpecies(e.target.value);
    }



    function togglePage(pageNumber) {
        setCurrentPage(pageNumber);
    }

    const indexOfLastCard = currentPage * cardsPerPage;
    const indexOfFirstCard = indexOfLastCard - cardsPerPage;
    const currentCards = searchResult.slice(indexOfFirstCard, indexOfLastCard);
    
    useEffect(() => {
        function handleEscapeKey(event) {
            if (event.key === 'Escape') {
                setIsOpen(false);
            }
        }
        window.addEventListener('keydown', handleEscapeKey);
        return () => {
            window.removeEventListener('keydown', handleEscapeKey);
        };
    }, [setIsOpen]);


    if (flies.length === 0) {
        return <div>Loading...</div>;
    } else {
        return (
        <div className='flies-container'>
            <div className='flies-header-container'>
                <h2>Flies</h2>
            </div>
            <div className='filters-container'>
                <div className='filter_type'>
                    <h3>Fly<br/>Types</h3>
                    <select value={selectedType} onChange={handleTypeChange}>
                        <option value=''> All </option>
                        <option value='Dry'>Dry Flies</option>
                        <option value='Wet'>Wet Flies</option>
                        <option value='Streamer'>Steamers</option>
                    </select>
                </div>
                <div className='filter_cycle'>
                    <h3>Life<br/> Cycle</h3>
                    <select value={selectedCycle} onChange={handleCycleChange}>
                        <option value=''> All </option>
                        <option value='Nymph'>Nymph</option>
                        <option value='Emerger'>Emerger</option>
                        <option value='Adult'>Adult</option>
                    </select>
                </div>
                <div className='filter_species'>
                    <h3>Immitation<br/>Species</h3>
                    <select value={selectedSpecies} onChange={handleSpeciesChange}>
                        <option value=''>All</option>
                        <option value='Mayfly'>Mayfly</option>
                        <option value='Caddis'>Caddis</option>
                        <option value='Stonefly'>Stonefly</option>
                        <option value='Midge'>Midge</option>
                        <option value='Terrestrial'>Terrestrial</option>
                        <option value='Baitfish'>Baitfish</option>
                    </select>
                </div>
            </div>
            <div className='search-container'>
                
            </div>
            <div>
                <FlyPopUp isOpen={isOpen} togglePopup={togglePopup} selectedFly={selectedFly}/>
            </div>
            <div className='fly-grid'>
                {currentCards.map((fly) => {
                    return (
                        <div key={fly[0]} className="fly-card" onClick={() => { togglePopup(); setSelectedFly(fly)}}>
                            <h2 onClick={togglePopup}>{fly[1]}</h2>
                            <img  className='fly-image' src={fly[2]} alt='Image not available'/>
                        </div>
                    )                    
                })}
            </div>
            <div className='pagination'>
            {searchResult.length > cardsPerPage &&
                    Array.from({ length: Math.ceil(searchResult.length / cardsPerPage) }, (_, index) => (
                        <button key={index} onClick={() => togglePage(index + 1)}>
                            {index + 1}
                        </button>
                    ))}
            </div>
        </div>    
        )
    }
}

export default Flies;



