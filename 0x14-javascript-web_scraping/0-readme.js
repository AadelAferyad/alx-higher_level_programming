#!/usr/bin/node

const arg = process.argv;
const fs = require('fs');

try {
  const data = fs.readFileSync(arg[2], 'utf8');
  console.log(data);
} catch (err) {
  console.log(err);
}
