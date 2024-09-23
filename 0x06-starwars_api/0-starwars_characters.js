#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// Fetch the film data from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (err, res, body) {
  if (err) {
    console.error('Error fetching film data:', err);
    return;
  }

  let actors;
  try {
    actors = JSON.parse(body).characters;
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
    return;
  }

  if (!actors || !Array.isArray(actors)) {
    console.error('Characters not found in response.');
    return;
  }

  // Function to print characters in exact order
  const exactOrder = (actors, index) => {
    if (index === actors.length) return;

    // Fetch the character data
    request(actors[index], function (err, res, body) {
      if (err) {
        console.error('Error fetching character data:', err);
        return;
      }

      let character;
      try {
        character = JSON.parse(body);
      } catch (parseError) {
        console.error('Error parsing character JSON:', parseError);
        return;
      }

      console.log(character.name);

      // Recursive call to print the next character
      exactOrder(actors, index + 1);
    });
  };

  // Start printing the characters
  exactOrder(actors, 0);
});

