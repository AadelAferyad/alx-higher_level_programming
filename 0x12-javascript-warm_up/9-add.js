#!/usr/bin/node

function add (a, b) {
  return (a + b);
}
const argv = process.argv.slice(2);
const argc = argv.length;
if (!argc || argc < 2) {
  console.log(NaN);
} else {
  console.log(add(parseInt(argv[0]), parseInt(argv[1])));
}
