import React from "react";
import '../Styles/header.css'

function Header() {
    return(
        <div className="header-container">
            <h1>Hatch Match</h1>
            <img className='logo' src='https://cdn.pixabay.com/photo/2022/03/24/19/37/fly-fishing-7089758_960_720.png' alt='Hatch Match Logo' />
        </div>
    )
}

export default Header