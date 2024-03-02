import React from 'react';
import '../Styles/FlyPopUp.css'

function FlyPopUp({isOpen, togglePopup, selectedFly}) {
    if(isOpen === true) {
        return (
            <div className='card-overlay'>
                <div className='card'>
                    <h1 className='card-name'>{selectedFly.fly_name}</h1>
                    <img className='fly-image' src={selectedFly.fly_image} alt='Not available' />
                    <div className='details-container'>
                        <div className='details-left'>
                            <ul>{selectedFly.fly_type} fly</ul>
                            <ul>Immitation:{selectedFly.fly_imitation} {selectedFly.fly_life_cycle}</ul>
                            <ul>Tying tutorial:<a href='#'></a></ul>
                        </div>
                        <div className='details-right'>
                            <img className='bug-image' src={selectedFly.bug_image} alt='Not available' />
                        </div>

                    </div>
                    <button className='card-button' onClick={togglePopup}>Close</button>
                </div>
            </div>
          );
    }
}

export default FlyPopUp;
