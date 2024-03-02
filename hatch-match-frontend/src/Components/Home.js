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
        <div>
            <header className="header">
                <h1>Welcome to Hatch Match</h1>
                <img className='logo' src='https://media.istockphoto.com/id/1292289580/vector/dry-fly.jpg?s=612x612&w=0&k=20&c=oNnjoO5_t9hPTSczXk3j38TNvJCgymmlXCbGL7Bnha8=' alt='Hatch Match Logo' />
            </header>
            <main>Welcome to our comprehensive fly fishing fly encyclopedia, where every cast tells a story and every fly holds the promise of adventure. Explore our vast collection of meticulously curated flies, from timeless classics to innovative patterns, and uncover the secrets to unlocking the perfect catch. Whether you're a seasoned angler or just dipping your toes into the sport, let our wealth of knowledge guide you through the rich and vibrant world of fly fishing.</main>
            <div className="featured-flies">
                <FlyPopUp isOpen={isOpen} togglePopup={togglePopup} selectedFly={selectedFly}/>
                <h2>Featured Flies</h2>
                <div className="container">
                    {featuredFlies.map((fly) => {
                        return(
                            <div key={fly.id} className="fly-card" onClick={() => { togglePopup(); setSelectedFly(fly)}}>
                                <h2 >{fly.fly_name}</h2>
                                <img src={fly.fly_image} alt='Not available'/>
                                <h3>Imitation: {fly.fly_imitation}</h3>
                            </div>
                        ) 
                    })}
                </div>
            </div>
            <section className="testimonials">
                <div className="container">
                    <div className="testimonial">
                        <p>Customer Testimonial 1</p>
                    </div>
                    <div className="testimonial">
                        <p>Customer Testimonial 2</p>
                    </div>
                </div>
            </section>

            <footer>
                <div className="container">
                    <ul>
                        <li><a href="javascript:void(0)">Terms of Service</a></li>
                        <li><a href="javascript:void(0)">Privacy Policy</a></li>
                        <li><a href="javascript:void(0)">FAQs</a></li>
                    </ul>
                </div>
            </footer>
        </div>
    );
}

export default Home;

