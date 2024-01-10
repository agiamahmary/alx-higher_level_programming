#!/usr/bin/node
// prints a string

const args = process.argv;
let num1 = 1;

if (args.length === 3) {
  num1 = Math.floor(Number(args[2]));
}

function factorial (a) {
  if (a < 1) return 1;
  return a * factorial(a - 1);
}

console.log(factorial(num1));
