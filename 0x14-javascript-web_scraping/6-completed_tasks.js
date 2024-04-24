#!/usr/bin/node

const arg = process.argv;
const request = require('request');

request(arg[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }
  const jsonFormat = JSON.parse(body);
  const dic = {};
  for (let i = 0; i < jsonFormat.length; i++) {
    if (jsonFormat[i].completed === true) {
      if (!dic[jsonFormat[i].userId.toString()]) {
        dic[jsonFormat[i].userId.toString()] = 0;
      }
      dic[jsonFormat[i].userId.toString()] = 1 + dic[jsonFormat[i].userId.toString()];
    }
  }
  console.log(dic);
});
