import React from 'react';
import '../Styles/FlyPopUp.css'

function FlyPopUp({isOpen, togglePopup, selectedFly}) {
    if(isOpen === true) {
        return (
            <div className='card-overlay'>
                <div className='card'>
                    <div className='card-header'>
                        <h2 className='card-name'>{selectedFly[1]}</h2>
                        <button className='card-x' onClick={togglePopup}>X</button>
                    </div>
                    <div className='images-and-details'>
                        <div className='image-container'>
                            <img className='fly-image-popup' src={selectedFly[2]} alt='Not available' />
                            <img className='bug-image' src={selectedFly[9]} alt='Not available' />
                        </div>
                        <div className='details-container'>
                            <ul>Type: {selectedFly[3]} fly</ul>
                            <ul>Immitation: {selectedFly[4]} {selectedFly[5]}</ul>
                            <ul>Tying tutorial:<a href='#'> Coming Soon</a></ul>
                        </div>
                    </div>
                    <div className='written-tutorial'>
                        <div className='materials'>
                            <h3>Materials:</h3>
                            <div dangerouslySetInnerHTML={{ __html: selectedFly[6].replace(/\n/g, '<br />') }} />
                        </div>
                        <div className='instructions'>
                            <h3>Tying Instructions:</h3>
                            <div dangerouslySetInnerHTML={{ __html: selectedFly[7].replace(/\n/g, '<br />') }} />
                        </div>
                    </div>
                    <button className='card-button' onClick={togglePopup}>Close</button>
                </div>
            </div>
          );
    }
}

export default FlyPopUp;
