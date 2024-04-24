#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  try {
    fs.writeFileSync(argv[3], body, 'utf-8');
  } catch (err) {
    console.log(err);
  }
});
