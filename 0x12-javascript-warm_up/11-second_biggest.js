#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length === 2) console.log(0);
let num1 = 1;
let max  = Math.floor(Number(args[2]));
for (let x in args.splice(2)) {
  num1 = Math.floor(Number(x));
  if (num1 > max) max = num1;
}
