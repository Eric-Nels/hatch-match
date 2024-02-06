import '../Styles/flies.css'
import React, { useState } from "react";

function Flies({flies}) {

    const [selectedType, setSelectedType] = useState('')

    function filterFlies() {
        let sortedFlies;

        if(selectedType === 'Dry Flies') {
            sortedFlies = [...flies].filter(fly => fly.type == 'Dry Fly')
        } else if(selectedType === 'Wet Flies') {
            sortedFlies = [...flies].filter(fly => fly.type == 'Wet Fly')
        } else if (selectedType === 'Nymphs') {
            sortedFlies = [...flies].filter(fly => fly.type == 'Nymph')
        } else if (selectedType === "Emergers") {
            sortedFlies = [...flies].filter(fly => fly.type == 'Emerger')
        } else {
            sortedFlies = flies
        }

        return sortedFlies
    }

    const flyInfo = filterFlies();

    function handleTypeChange(e) {
        setSelectedType(e.target.value);
    }

    return (
        <div>
            <header>Flies</header>
            <div className='filter'>
            <h2>Fly types</h2>
            <select value={selectedType} onChange={handleTypeChange}>
                <option value=''> Select Type</option>
                <option value='Dry Flies'>Dry Flies</option>
                <option value='Wet Flies'>Wet Flies</option>
                <option value='Nymphs'>Nymphs</option>
                <option value='Emergers'>Emergers</option>
            </select>
            </div>
            <div className='fly-grid'>
                {flyInfo.map((fly)=> {
                    return(
                        <div key={fly.id} className="fly-card">
                            <h2>{fly.name}</h2>
                            <img src={fly.image} />
                            <h3>Target Species: {fly.species_name}</h3>
                        </div>
                    )
                })}
            </div>
        </div>    
    )
}

export default Flies;