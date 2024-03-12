#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let i;
    if (!c) {
      c = 'X';
    } else {
      c = 'C';
    }
    for (i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
