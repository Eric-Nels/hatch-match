import React from 'react';

function ThanksPopUp({ showThanks, setShowThanks }) {
    if(showThanks == true) {
        return(
            <div className='card-overlay'>
                <div className='card'>
                    <h1>Thank you for your submittion</h1>
                    <p>I will review the suggestions and add it to the index as soon as possible</p>
                    <button className='card-button' onClick={() => setShowThanks(!showThanks)}>Close</button>
                </div>
            </div>  
        )
    } else {
        return null;
    }
}

export default ThanksPopUp