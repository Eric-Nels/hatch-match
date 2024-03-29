import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import Flies from "./Flies";
import SuggestionForm from "./SuggestionForm";
import About from "./About";


function App() {

    const [flies, setFlies] = useState([])
    const [isOpen, setIsOpen] = useState(false);
    const [selectedFly, setSelectedFly] = useState([])
    const [featuredFlies, setFeaturedFlies] = useState([]);

    useEffect(()=> {
        fetchFliesData(); 
    }, []);

    function fetchFliesData() {
        fetch('http://127.0.0.1:5000/api/flies')
            .then((r) => r.json())
            .then((data) => {
                setFlies(data);
                console.log(flies)
            })
            .catch((error) => console.error('Error fetching flies:', error));
    }
    
    useEffect(() => {
        if (flies.length > 0) {
            const selectedFlies = selectThreeRandomFlies();
            setFeaturedFlies(selectedFlies);
        }
    }, [flies]);

    const togglePopup = () => {
        setIsOpen(!isOpen);
      };

    function selectThreeRandomFlies() {
        const selectedFlies = [];
        const availableFlies = [...flies];

        while (selectedFlies.length < 3 && availableFlies.length > 0) {
            const randomIndex = Math.floor(Math.random() * availableFlies.length);
            const randomFly = availableFlies.splice(randomIndex, 1)[0];
            selectedFlies.push(randomFly);
        }

        return selectedFlies;
    } 

    return(
        <div className="App">
            <Navbar />
            <Routes>
                <Route path="/flies" element={<Flies flies={flies} isOpen={isOpen} setIsOpen={setIsOpen} selectedFly={selectedFly} setSelectedFly={setSelectedFly} togglePopup={togglePopup}/>} />
                <Route path="/suggestions" element={<SuggestionForm />} />
                <Route path="/about-us" element={<About />} />
                <Route path="/" element={<Home featuredFlies={featuredFlies} isOpen={isOpen} setIsOpen={setIsOpen} selectedFly={selectedFly} setSelectedFly={setSelectedFly} togglePopup={togglePopup}/>} />    
            </Routes>    
        </div>
    )
}

export default App;