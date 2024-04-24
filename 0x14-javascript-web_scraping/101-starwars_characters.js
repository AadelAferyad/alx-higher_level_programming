#!/usr/bin/node

const arg = process.argv;
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(arg[2].toString());

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchData () {
  let data;
  try {
    data = await makeRequest(url);
  } catch (error) {
    console.log(error);
  }
  const jsonData = JSON.parse(data);
  const characters = jsonData.characters;
  for (let i = 0; i < characters.length; i++) {
    try {
      const characterData = await makeRequest(characters[i]);
      console.log((JSON.parse(characterData)).name);
    } catch (error) {
      console.log(error);
    }
  }
}

fetchData();
