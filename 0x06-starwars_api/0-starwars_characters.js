#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Fetch the film data from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (err, res, body) {
  if (err) throw err;

  // Parse the film data
  const actors = JSON.parse(body).characters;

  // Function to print characters in exact order
  const exactOrder = (actors, index) => {
    if (index === actors.length) return;

    // Fetch the character data
    request(actors[index], function (err, res, body) {
      if (err) throw err;
      
      // Print the character's name
      console.log(JSON.parse(body).name);

      // Recursive call to print the next character
      exactOrder(actors, index + 1);
    });
  };

  // Start printing the characters
  exactOrder(actors, 0);
});

