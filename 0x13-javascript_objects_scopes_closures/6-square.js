#!/usr/bin/node
const Parent = require('./5-square');

class Square extends Parent {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (!c) {
      c = 'X'
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}
module.exports = Square;
