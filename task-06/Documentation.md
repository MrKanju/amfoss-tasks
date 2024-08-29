# Documentation for React Movie App

## Overview

The React Movie App is a movie search application built with React. It allows users to search for movies by title using the OMDb API and displays the results. The app uses the `useReducer` hook for state management and `useEffect` for initial data fetching.

## Functionality

### Components

#### `App.js`

- **State Management**
  - Uses `useReducer` to manage state with actions for loading, success, and error states.
  - `initialState` includes `loading`, `movies`, and `errorMessage`.

- **Effect Hook**
  - The `useEffect` hook is used to fetch initial movie data from the OMDb API when the component mounts.

- **Search Functionality**
  - The `search` function dispatches a request action, fetches movie data based on the search query, and updates the state with results or errors.

- **Rendering**
  - Displays a `Header` component, a `Search` component for input, and a list of `Movie` components based on the search results.
  - Shows a loading indicator or an error message as needed.

### Reducer

#### `reducer(state, action)`

- **SEARCH_MOVIES_REQUEST**
  - Sets loading to `true` and clears any previous error message.

- **SEARCH_MOVIES_SUCCESS**
  - Updates state with the fetched movies and sets loading to `false`.

- **SEARCH_MOVIES_FAILURE**
  - Updates state with the error message and sets loading to `false`.

### Components

#### `Header.js`

- **Purpose**: Displays the application title.

#### `Search.js`

- **Purpose**: Provides an input field for users to enter their search query and a button to trigger the search.
- **Props**: `search` function to handle search queries.

#### `Movie.js`

- **Purpose**: Renders individual movie details such as title, year, and poster.
- **Props**: `movie` object containing movie details.

## Implementation Details

### Initial Data Fetching

On component mount, `useEffect` fetches a default movie list from the OMDb API and dispatches a success action with the results.

### Search Function

The `search` function is called when a user submits a search query. It dispatches a request action, fetches data from the API, and dispatches either a success or failure action based on the API response.

### Rendering Logic

- **Loading State**: Displays a loading spinner when data is being fetched.
- **Error State**: Shows an error message if the API call fails.
- **Movies List**: Renders a list of `Movie` components if data is successfully fetched.

## Code Example

Here's a snippet from `App.js` showing the search functionality:

```javascript
import React, { useReducer, useEffect } from "react";
import "../App.css";
import Header from "./Header";
import Movie from "./Movie";
import Search from "./Search";

const API_KEY = "65525897";
const MOVIE_API_URL = `https://www.omdbapi.com/?s=man&apikey=${API_KEY}`;

const initialState = {
  loading: true,
  movies: [],
  errorMessage: null
};

const reducer = (state, action) => {
  switch (action.type) {
    case "SEARCH_MOVIES_REQUEST":
      return {
        ...state,
        loading: true,
        errorMessage: null
      };
    case "SEARCH_MOVIES_SUCCESS":
      return {
        ...state,
        loading: false,
        movies: action.payload
      };
    case "SEARCH_MOVIES_FAILURE":
      return {
        ...state,
        loading: false,
        errorMessage: action.error
      };
    default:
      return state;
  }
};

const App = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    fetch(MOVIE_API_URL)
      .then(response => response.json())
      .then(jsonResponse => {
        dispatch({
          type: "SEARCH_MOVIES_SUCCESS",
          payload: jsonResponse.Search
        });
      });
  }, []);

  const search = searchValue => {
    dispatch({
      type: "SEARCH_MOVIES_REQUEST"
    });

    fetch(`https://www.omdbapi.com/?s=${searchValue}&apikey=${API_KEY}`)
      .then(response => response.json())
      .then(jsonResponse => {
        if (jsonResponse.Response === "True") {
          dispatch({
            type: "SEARCH_MOVIES_SUCCESS",
            payload: jsonResponse.Search
          });
        } else {
          dispatch({
            type: "SEARCH_MOVIES_FAILURE",
            error: jsonResponse.Error
          });
        }
      });
  };

  const { movies, errorMessage, loading } = state;

  return (
    <div className="App">
      <div className="Nav">
        <Header text="HOOKED" />
        <Search search={search} />
      </div>
      <p className="App-intro">Sharing a few of our favorite movies</p>
      <div className="movies">
        {loading && !errorMessage ? (
          <span className="loader"></span>
        ) : errorMessage ? (
          <div className="errorMessage">{errorMessage}</div>
        ) : (
          movies.map((movie, index) => (
            <Movie key={`${index}-${movie.Title}`} movie={movie} />
          ))
        )}
      </div>
    </div>
  );
};

export default App;
