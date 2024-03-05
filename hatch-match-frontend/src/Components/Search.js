import '../Styles/search.css'

function Search({ searchValue, handleSearchChange, handleSearchSubmit}) {

    return(
        <div className="search-container">
            <label className="search-label">Search:</label>
           <input className="search-input" value={searchValue} onChange={handleSearchChange}></input>
           <button className="search-button" onClick={handleSearchSubmit}>Go</button>
        </div>     
    )
}

export default Search;