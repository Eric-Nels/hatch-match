import { NavLink } from "react-router-dom";
import '../Styles/navbar.css'


function Navbar() {
    return(
        <div className="navbar">
            <NavLink to='/'> Home </NavLink>
            <NavLink to='/flies'> Flies</NavLink>
            <NavLink to='/species'>Search by Fish Species</NavLink>
            <NavLink to='/bugs'>Search bugs by region</NavLink>
        </div>
    )
}

export default Navbar;