#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');

try {
  fs.writeFileSync(argv[2], argv[3], 'utf-8');
} catch (err) {
  console.log(err);
}
