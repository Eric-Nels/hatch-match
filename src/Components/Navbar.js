import { NavLink } from "react-router-dom";
import '../Styles/navbar.css'


function Navbar() {
    return(
        <div className="navbar">
            <NavLink to='/'> Home </NavLink>
            <NavLink to='/flies'> Flies</NavLink>
        </div>
    )
}

export default Navbar;