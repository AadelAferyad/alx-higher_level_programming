#!/usr/bin/node

const arg = process.argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(arg[2]);

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const jsonFormat = JSON.parse(body);
  console.log(jsonFormat.title);
});
