#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const printCharacters = (characters, index) => {
  if (index === characters.length) {
    return;
  }
  request(characters[index], (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
};

request(url, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
