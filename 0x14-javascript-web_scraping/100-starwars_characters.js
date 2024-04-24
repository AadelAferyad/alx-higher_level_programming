#!/usr/bin/node

const arg = process.argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(arg[2].toString());

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  const jsonData = JSON.parse(body);
  const characters = jsonData.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, res, body) {
      if (err) {
        console.log(err);
        return;
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
