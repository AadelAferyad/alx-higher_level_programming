#!/usr/bin/node

function factorial (n) {
  if (n === 1 || n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

const argv = process.argv.slice(2);
const argc = argv.length;
let n;
if (!argc) {
  n = 1;
} else {
  n = argv[0];
}
console.log(factorial(n));
