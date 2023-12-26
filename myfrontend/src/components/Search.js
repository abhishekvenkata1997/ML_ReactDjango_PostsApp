import React, {useState} from 'react'
import './../SearchBar.css'

const SearchBar = ({onSearch}) => {

  //query values initially empty input is set whenever new values is added
    const [query, setQuery] = useState('')
    const handleInputChange = (event) => {
        setQuery(event.target.value)
    }

    //onSearch function passed as parameter
    const handleSearch = () => {
        onSearch(query)
    }

    return (
        <div className="search-bar-container">
          <input
            type="text"
            placeholder="Search..."
            value={query}
            onChange={handleInputChange}
            className="search-input"
          />
          <button onClick={handleSearch} className="search-button">
            Search
          </button>
        </div>
      );
    
};

export default SearchBar;