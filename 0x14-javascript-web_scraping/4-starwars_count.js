#!/usr/bin/node

const arg = process.argv;
const request = require('request');

request(arg[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const jsonData = JSON.parse(body);
  const list = jsonData.results;
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    for (let j = 0; j < list[i].characters.length; j++) {
      if (list[i].characters[j].indexOf('18') !== -1) {
        count++;
      }
    }
  }
  console.log(count);
});
