#!/usr/bin/node

const args = process.argv.slice(2);
const argc = args.length;

if (argc === 1) {
  console.log('Argument found');
} else if (argc > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
