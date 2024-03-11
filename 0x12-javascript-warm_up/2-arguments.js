#!/usr/bin/node

const args = process.argv.slice(2);
const argc = args.length;

if (argc > 0) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
