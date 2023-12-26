import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './../Home.css';
import Post from './Post';
import SearchBar from './Search';
import isEqual from 'lodash/isEqual';

export default function Home() {
  const [posts, setPosts] = useState([]); //has the list of posts
  const [addStatus, setAddStatus] = useState(false); //add Status decides when to show the option to add a new post
  const [imagePreview, setImagePreview] = useState([]) //imagepreview is used in the add post to give a preview of images
  const [fetchData, setFetchData] = useState(true) //fetchData checks when to get posts from backend
  const [sortByDateAsc, setSortByDateAsc] = useState(true)

  let api = 'http://127.0.0.1:8000/api'; //backend api
  
  //running useEffect whenever fetchdata changes state and on initialisation
  useEffect(() => {
    const getData = async () => {
      try {
        const response = await axios.get(api + '/Post/');
        const result = response.data
        setPosts(result)
      } catch (error) {
        console.error(error)
      }
    };

    if(fetchData){
      getData()
      setFetchData(false)
    }

  }, [api, fetchData]);

  //Runs on component mounting, sets localstorage to the value of posts to prevent re-render
  useEffect(() => {
 
    const storedPosts = localStorage.getItem('posts');
    if (storedPosts) {
      setPosts(JSON.parse(storedPosts));
    } else {
      // If no data in localStorage, fetch data
      setFetchData(true);
    }
  }, []);

  //runs whenever there is an updated to posts and sets the localstorage to posts, prevents posts rerendering
  useEffect(() => {
    // Save the posts data to localStorage
    localStorage.setItem('posts', JSON.stringify(posts));
  }, [posts]);

  
  //whenever add new post or cancel is clicked add status flips and imagepreview is set to null
  function handleClick(e) {
    e.preventDefault();
    setAddStatus(!addStatus)
    setImagePreview([])
  }

  //to handle image preview promise waits for all images to load and shows images image preview column
  const handleFileChange = (event) => {
    const files = event.target.files;

    if (files) {
      const newPreviews = Array.from(files).map((file) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        return new Promise((resolve) => {
          reader.onloadend = () => {
            resolve(reader.result);
          };
        });
      });

      //promise waits for every promise in array of files to run then sets newPreviews to that result
      Promise.all(newPreviews).then((results) => {
        setImagePreview(results);
      });
    }
  };


  //sorting function
  const handleSortByDate = () => {
    setSortByDateAsc((SortByDateAsc) => !SortByDateAsc )
    getSortedPosts()
  }

  const getSortedPosts = async() => {
    try{
      //create a copy of current posts state value
      const sortedPosts = [...posts]

      //sort by copy based on desired order
      sortedPosts.sort((a,b) => {
        const dateA = new Date(a.timePosted).getTime()
        const dateB = new Date(b.timePosted).getTime()

        return sortByDateAsc ? dateB - dateA : dateA - dateB
      })
      setPosts(sortedPosts)
    }
    catch(error){
      console.log(error)
    }
  }

  const handleSearch = async (query) => {

    // Perform your search logic here
    const queryParts = query.split(' ');

    //content search searches for all the content columns inside the post based on search params and returns result  
    if (query.startsWith('content') && queryParts.length > 1) {
        const searchParams = queryParts.slice(1).join(' ');
        console.log(searchParams)
        try {
            const response = await axios.get(api + '/Post/search/', {
                params: {
                    search: searchParams
                }
            });
            const result = response.data;
            if(isEqual(result,JSON.parse(localStorage.getItem('posts')))){;}
            else{setPosts(result)}
        } catch (error) {
            console.error(error)
        }
    }
    //search for images based on tag values and return the ones that match the query params passed 
    else if (query.startsWith('image') && queryParts.length > 1) {
        // Do something else for 'image'
        const imageParams = queryParts.slice(1).join(' ');
        console.log(imageParams)
        try{
            const response = await axios.get(api+'/Post/imagesearch/' , {
                params: {
                    search: imageParams
                }
            })

            const result = response.data
            if(isEqual(result,JSON.parse(localStorage.getItem('posts')))){;}
            else{setPosts(result)}

        } catch(error) {
            console.error(error)
        }
    //if no 'content' or 'image' query is passed return the values for content search only    
    } else {
        try {
            const response = await axios.get(api + '/Post/search/', {
                params: {
                    search: query
                }
            });
            const result = response.data
            if(isEqual(result,JSON.parse(localStorage.getItem('posts')))){;}
            else{setPosts(result)}
        } catch (error) {
            console.error(error)
        }
    }
};

  //handle submit function runs on adding new post, it runs a post which adds the data, then sets fetchdata to true
  //setFetchData to true reruns one of the useEffects to get the new updated posts value
  async function handleSubmit(formData) {
    try {
      setAddStatus(false)
      const response = await axios.post(api + '/Post/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setFetchData(true)
    } catch (error) {
      console.log('Error in handleSubmit function', error)
    }
  }

  //handleFormSubmit takes formdata and sends to handlesubmit, written as seperate function 
  //to allow added functionality later on
  function handleFormSubmit(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    handleSubmit(formData);
  }

  return (
    
<div className="container">
      <div className="header" style={{margin: '5px', borderRadius:'5px'}}>
        <SearchBar onSearch={handleSearch} />
        <button className={`add-post-btn ${addStatus ? 'cancel-btn' : ''}`} onClick={handleClick}
        style={{ borderRadius: '5px'}}>
          {addStatus ? 'Cancel' : 'Add New Post'}
        </button>
      </div>

      {addStatus && (
        <form className="form" onSubmit={handleFormSubmit} style={{ margin: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '5px', backgroundColor: '#f9f9f9' }}>
          <label style={{ display: 'block', margin: '10px 0' }}>
            Content:
            <input type="text" name="content" style={{ marginLeft: '10px', padding: '5px', borderRadius: '3px', border: '1px solid #ccc' }} />
          </label>
          <label style={{ display: 'block', margin: '10px 0' }}>
            Images:
            <input type="file" name="images" accept="image/jpeg"  onChange={handleFileChange} multiple required style={{ marginLeft: '10px', padding: '5px', borderRadius: '3px', border: '1px solid #ccc' }} />
          </label>
          <div style={{ marginTop: '10px', display: 'flex', gap: '10px' }}>
            {/* Pass imagePreview state with a specific size to show */}
            {imagePreview.map((preview, index) => (
              <img key={index} src={preview} alt={`Images Preview ${index}`} style={{ width: '50px', borderRadius: '5px' }} />
            ))}
          </div>
          <button type="submit" style={{ backgroundColor: '#4caf50', color: 'white', padding: '10px', borderRadius: '3px', border: 'none', cursor: 'pointer', marginTop: '10px' }}>Submit</button>
        </form>
      )}


      <h1>Posts</h1>
      
      {/* Sorting dropdown */}
      <div className='sort-dropdown' style={{marginTop: '10px'}}>
        <span>Sort By Posted Date:</span>
        <select onChange={handleSortByDate} value={sortByDateAsc ? 'asc' : 'desc'}>
          <option value="asc">Ascending</option>
          <option value="desc">Descending</option>
        </select>
      </div>
      <div className="posts-container">
        {posts &&
          posts.map((post) => (
            <div key={post.id} className="post">
             {/* a post component passed with id and value of post */}
              <Post key={post.id} post={post} />
            </div>
          ))}
      </div>
    </div>
  );
}
