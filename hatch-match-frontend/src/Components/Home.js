import '../Styles/home.css';
import FlyPopUp from './FlyPopUp';

function Home({ featuredFlies, togglePopup, setSelectedFly, isOpen, selectedFly }) {

    return (
        <div>
            <header className="header">
                <h1>Welcome to Hatch Match</h1>
                <img className='logo' src='https://media.istockphoto.com/id/1292289580/vector/dry-fly.jpg?s=612x612&w=0&k=20&c=oNnjoO5_t9hPTSczXk3j38TNvJCgymmlXCbGL7Bnha8=' alt='Hatch Match Logo' />
            </header>

            <section className="featured-flies">
                <FlyPopUp isOpen={isOpen} togglePopup={togglePopup} selectedFly={selectedFly}/>
                <h2>Featured Flies</h2>
                <div className="container">
                    {featuredFlies.map((fly) => {
                        return(
                            <div key={fly.id} className="fly-card" onClick={() => { togglePopup(); setSelectedFly(fly)}}>
                                <h2 >{fly.fly_name}</h2>
                                <img src={fly.fly_image} alt='Image not available'/>
                                <h3>Imitation: {fly.fly_imitation}</h3>
                            </div>
                        ) 
                    })}
                </div>
            </section>

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
                        <li><a href="#">Terms of Service</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                        <li><a href="#">FAQs</a></li>
                    </ul>
                </div>
            </footer>
        </div>
    );
}

export default Home;