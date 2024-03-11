#!/usr/bin/node

const argv = process.argv.slice(2);
const message = 'C is fun';
let i = 0;

if (!argv[0]) {
  console.log('Missing number of occurrences');
} else if (!isNaN(argv[0])) {
  for (i = 0; i < parseInt(argv[0]); i++) {
    console.log(message);
  }
}
