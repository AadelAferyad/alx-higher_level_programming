#!/usr/bin/node

const argv = process.argv.slice(2);
if (!argv[0] || isNaN(argv[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv[0]);
}
