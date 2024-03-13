#!/usr/bin/node

const Mylist = require('./100-data').list;
console.log(Mylist);
console.log(Mylist.map((x, i) => x * i));
