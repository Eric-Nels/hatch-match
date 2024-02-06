import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import Flies from "./Flies";
import Species from "./Species"
import Bugs from "./Bugs";


function App() {

    const [flies, setFlies] = useState([])
    const [species, setSpecies] = useState([])

    useEffect(()=> {
        fetch('http://127.0.0.1:5000/api/data')
        .then((r)=>r.json())
        .then((data)=> {
            setFlies(data)
        })
    }, [])

    return(
        <div className="App">
            <Navbar />
            <Routes>
                <Route path="/flies" element={<Flies flies={flies} />} />
                <Route path="/species" element={<Species species={species} />} />
                <Route path="/bugs" element={<Bugs />} />
                <Route path="/" element={<Home />} />    
            </Routes>    
        </div>
    )
}

export default App;