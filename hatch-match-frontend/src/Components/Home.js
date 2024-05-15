import '../Styles/home.css';
import FlyPopUp from './FlyPopUp';
import React, { useEffect} from "react";

function Home({ featuredFlies, togglePopup, setSelectedFly, isOpen, setIsOpen, selectedFly}) {

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

    return (
        <div className='home'>
            <header className="header">
                <h1>Welcome to Hatch Match</h1>
                <img className='logo' src='https://cdn.pixabay.com/photo/2022/03/24/19/37/fly-fishing-7089758_960_720.png' alt='Hatch Match Logo' />
            </header>
            <main className='into-text'>Welcome to our comprehensive fly fishing fly encyclopedia, where every cast tells a story and every fly holds the promise of adventure. Explore our vast collection of meticulously curated flies, from timeless classics to innovative patterns, and uncover the secrets to unlocking the perfect catch. Whether you're a seasoned angler or just dipping your toes into the sport, let our wealth of knowledge guide you through the rich and vibrant world of fly fishing.</main>
            <div className="featured-flies">
                <FlyPopUp isOpen={isOpen} togglePopup={togglePopup} selectedFly={selectedFly}/>
                <h2 className='featured-fly-header'>Featured Flies</h2>
                <div className="featured-flies-container">
                    {featuredFlies.map((fly) => {
                        return(
                            <div key={fly[0]} className="fly-card" onClick={() => { togglePopup(); setSelectedFly(fly)}}>
                                <h2 >{fly[1]}</h2>
                                <img className='fly-image' src={fly[2]} alt='Not available'/>
                                <h3>Imitation: {fly[4]}</h3>
                            </div>
                        ) 
                    })}
                </div>
            </div>
            <div className='catch-of-week-container'>
                <h2>Catch of the week</h2>
                <div className='catch-card'>
                    <a href='#'>@socialmedialink</a>
                    <img className='catch-image' src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq4Q_j_5LKlFR7fCRhAf5muEwLOQG9Oebuow&usqp=CAU' alt='Not Available' />
                </div>
                <div className='fly-used'>
                    <h3>Fly used:</h3> 
                    <img className='fly-used-image' src='https://www.johnkreft.com/wp-content/uploads/2019/09/Miasmic-October-Caddis-Pupa-Emerger.jpg' alt='Not Available' />
                    <p>Miasmic October Caddis Pupa-Emerger</p>
                </div>
            </div>
            <footer className='footer'>
                <a href='/about-us'>About Us</a>
            </footer>
        </div>
    );
}

export default Home;

