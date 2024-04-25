import React from 'react';
import '../Styles/FlyPopUp.css'

function FlyPopUp({isOpen, togglePopup, selectedFly}) {
    if(isOpen === true) {
        return (
            <div className='card-overlay'>
                <div className='card'>
                    <div className='card-header'>
                        <h1 className='card-name'>{selectedFly.fly_name}</h1>
                        <button className='card-x' onClick={togglePopup}>X</button>
                    </div>
                    <div className='image-container'>
                        <img className='fly-image-popup' src={selectedFly.fly_image} alt='Not available' />
                        <img className='bug-image' src={selectedFly.bug_image} alt='Not available' />
                    </div>
                    <div className='details-container'>
                        <ul>Type: {selectedFly.fly_type} fly</ul>
                        <ul>Immitation: {selectedFly.fly_imitation} {selectedFly.fly_life_cycle}</ul>
                        <ul>Tying tutorial:<a href='#'> Youtube-link</a></ul>
                        <ul>Materials: Coming Soon!</ul>
                        <ul>Tying Instructions: Coming Soon!</ul>
                    </div>
                    <button className='card-button' onClick={togglePopup}>Close</button>
                </div>
            </div>
          );
    }
}

export default FlyPopUp;
