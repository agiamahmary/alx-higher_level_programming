#!/usr/bin/node
// prints a string

const args = process.argv;
const num1 = Math.floor(Number(args[2]));
const num2 = Math.floor(Number(args[3]));

function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
