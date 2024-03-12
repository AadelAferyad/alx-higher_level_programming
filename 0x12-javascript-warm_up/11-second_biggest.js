#!/usr/bin/node

const argv = process.argv.slice(2);
const argc = argv.length;
let i;
let j;
let temp;
if (argc < 2) {
  console.log(0);
} else {
  for (i = 0; i < argc; i++) {
    for (j = i + 1; j < argc; j++) {
      if (parseInt(argv[i]) > parseInt(argv[j])) {
        temp = parseInt(argv[i]);
        argv[i] = parseInt(argv[j]);
        argv[j] = temp;
      }
    }
  }
  console.log(argv[argc - 2]);
}
