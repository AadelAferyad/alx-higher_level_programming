#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      let i;
      let j;
      let message = c;
      for (j = 0; j < this.size; j++) {
        message += c;
      }
      for (i = 0; i < this.size; i++) {
        console.log(message);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
