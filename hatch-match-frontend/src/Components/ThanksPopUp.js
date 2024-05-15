import React from 'react';

function ThanksPopUp({ showThanks, setShowThanks, image, catchImage }) {
    return showThanks ? (
        <div className='card-overlay'>
            <div className='card'>
                <h1>Thank you for your submission</h1>
                {catchImage === null ? (
                    <p>I will review the suggestions and add them to the index as soon as possible</p>
                ) : image === null ? (
                    <p>I will review all catch submissions and update the Catch of the Week on Sundays</p>
                ) : null}
                <button className='card-button' onClick={() => setShowThanks(!showThanks)}>Close</button>
            </div>
        </div>
    ) : null;
}

export default ThanksPopUp;