#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const swapiUrl = `https://swapi.dev/api/films/${movieId}/`;

function fetchMovieCharacters () {
  request(swapiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      function printCharacterNames (index) {
        if (index < characters.length) {
          request(characters[index], (error, response, body) => {
            if (!error && response.statusCode === 200) {
              const characterData = JSON.parse(body);
              console.log(characterData.name);
              printCharacterNames(index + 1);
            } else {
              console.error(error);
            }
          });
        }
      }

      printCharacterNames(0);
    } else {
      console.error(error);
    }
  });
}

fetchMovieCharacters();
