import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "./Home";
import Flies from "./Flies";
import SuggestionForm from "./SuggestionForm";
import About from "./About";
import Header from "./Header";
import Search from "./Search";
import '../Styles/app.css'


function App() {

    const [flies, setFlies] = useState([])
    const [isOpen, setIsOpen] = useState(false);
    const [selectedFly, setSelectedFly] = useState([])
    const [featuredFlies, setFeaturedFlies] = useState([]);
    const [searchValue, setSearchValue] = useState('')

    useEffect(()=> {
        fetchFliesData(); 
    }, []);

    function fetchFliesData() {
        fetch('https://ernelson.pythonanywhere.com/api/flies')
            .then((r) => r.json())
            .then((data) => {
                console.log(data)
                setFlies(data);
                console.log(flies)
            })
            .catch((error) => console.error('Error fetching flies:', error));
    }
    
    useEffect(() => {
        console.log(flies);
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
    
    function handleSearchChange(e) {
        setSearchValue(e.target.value)
    }

    // Render loading indicator or the app content based on the state of 'flies'
    if (flies.length === 0) {
        return <div>Loading...</div>;
    }

    return(
        <div className="App">
            <Header />
            <div className="navigation-container"> 
                <Navbar />
                <Search  searchValue={searchValue} setSearchValue={setSearchValue} handleSearchChange={handleSearchChange}/>
            </div>
            <Routes>
                <Route path="/flies" element={<Flies flies={flies} isOpen={isOpen} setIsOpen={setIsOpen} selectedFly={selectedFly} setSelectedFly={setSelectedFly} togglePopup={togglePopup} searchValue={searchValue}/>} />
                <Route path="/suggestions" element={<SuggestionForm />} />
                <Route path="/about-us" element={<About />} />
                <Route path="/" element={<Home featuredFlies={featuredFlies} isOpen={isOpen} setIsOpen={setIsOpen} selectedFly={selectedFly} setSelectedFly={setSelectedFly} togglePopup={togglePopup}/>} />    
            </Routes>    
        </div>
    )
}

export default App;