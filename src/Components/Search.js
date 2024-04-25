import '../Styles/search.css'
import { NavLink } from 'react-router-dom';

function Search({ searchValue, handleSearchChange}) {

    return(
        <div className="search-container">
            <label className="search-label">Search:</label>
           <input className="search-input" value={searchValue} onChange={handleSearchChange}></input>
           <NavLink  className='search-button' to='/flies'>Go</NavLink>
        </div>     
    )
}

export default Search;