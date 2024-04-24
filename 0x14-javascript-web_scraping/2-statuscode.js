#!/usr/bin/node

const arg = process.argv;
const request = require('request');

request.get(arg[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response.statusCode);
});
