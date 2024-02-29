import '../Styles/flies.css'
import React, { useEffect, useState } from "react";
import FlyPopUp from './FlyPopUp';
import Search from './Search';

function Flies({flies, selectedFly, setSelectedFly, isOpen, togglePopup}) {

    const [selectedType, setSelectedType] = useState('')
    const [selectedCycle, setSelectedCycle] = useState('')
    const [selectedSpecies, setSelectedSpecies] = useState('')
    const [searchValue, setSearchValue] = useState('')
    const [searchResult, setSearchResult] = useState([])
    

    useEffect(() => {
        filterFlies();
    }, [selectedType, selectedCycle, selectedSpecies, searchValue]);

    function filterFlies() {
        let filteredFlies = flies.filter(fly => {
            const typeMatch = !selectedType || fly.fly_type === selectedType;
            const cycleMatch = !selectedCycle || fly.fly_life_cycle === selectedCycle;
            const speciesMatch = !selectedSpecies || fly.fly_imitation === selectedSpecies;
            const searchMatch = fly.fly_name.toLowerCase().includes(searchValue.toLowerCase());
            return typeMatch && cycleMatch && speciesMatch && searchMatch;
        });
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

    function handleSearchChange(e) {
        setSearchValue(e.target.value)
    } 


    return (
        <div className='flies-container'>
            <header>Flies</header>
            <div className='filters-container'>
                <div className='filter_type'>
                    <h2>Fly types</h2>
                    <select value={selectedType} onChange={handleTypeChange}>
                        <option value=''> All </option>
                        <option value='Dry'>Dry Flies</option>
                        <option value='Wet'>Wet Flies</option>
                        <option value='Streamer'>Steamers</option>
                    </select>
                </div>
                <div className='filter_cycle'>
                    <h2>Life Cycle</h2>
                    <select value={selectedCycle} onChange={handleCycleChange}>
                        <option value=''> All </option>
                        <option value='Nymph'>Nymph</option>
                        <option value='Emerger'>Emerger</option>
                        <option value='Adult'>Adult</option>
                    </select>
                </div>
                <div className='filter_species'>
                    <h2>Species</h2>
                    <select value={selectedSpecies} onChange={handleSpeciesChange}>
                        <option value=''>All</option>
                        <option value='Mayfly'>Mayfly</option>
                        <option value='Caddis'>Caddis</option>
                        <option value='Stonefly'>Stonefly</option>
                        <option value='Midge'>Midge</option>
                        <option value='Terrestrials'>Terrestrials</option>
                        <option value='Baitfish'>Baitfish</option>
                    </select>
                </div>
            </div>
            <div className='search-container'>
                <Search  searchValue={searchValue} setSearchValue={setSearchValue} handleSearchChange={handleSearchChange}/>
            </div>
            <div>
                <FlyPopUp isOpen={isOpen} togglePopup={togglePopup} selectedFly={selectedFly}/>
            </div>
            <div className='fly-grid'>
                {searchResult.map((fly) => {
                    return (
                        <div key={fly.id} className="fly-card" onClick={() => { togglePopup(); setSelectedFly(fly)}}>
                            <h2 onClick={togglePopup}>{fly.fly_name}</h2>
                            <img src={fly.fly_image} alt='Image not available'/>
                        </div>
                    )                    
                })}
            </div>
        </div>    
    )
}

export default Flies;



