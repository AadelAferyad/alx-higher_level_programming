#!/usr/bin/node

const argv = process.argv.slice(2);
let i;
let j;
let message = 'X';
if (!argv[0] || isNaN(argv[0])) {
  console.log('Missing size');
} else {
  for (j = 1; j < parseInt(argv[0]); j++) {
    message += 'X';
  }
  for (i = 0; i < parseInt(argv[0]); i++) {
    console.log(message);
  }
}
