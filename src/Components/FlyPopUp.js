import React from 'react';
import '../Styles/FlyPopUp.css'

function FlyPopUp({isOpen, togglePopup, selectedFly}) {
    if(isOpen == true) {
        return (
            <div className='card-overlay'>
                <div className='card'>
                    <h1 className='card-name'>{selectedFly.fly_name}</h1>
                    <img className='card-image' src={selectedFly.fly_image} alt='Image not available' />
                    <ul>{selectedFly.fly_type}</ul>
                    <ul>{selectedFly.fly_imitation}</ul>
                    <button className='card-button' onClick={togglePopup}>Close</button>
                </div>
            </div>
          );
    }
}

export default FlyPopUp;
