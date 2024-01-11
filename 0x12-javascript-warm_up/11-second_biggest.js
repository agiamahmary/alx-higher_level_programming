#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let num1;
  let max = Math.floor(Number(args[2]));
  let second = Math.floor(Number(args[2]));
  for (const x of args.splice(2)) {
    num1 = Math.floor(Number(x));
    if (num1 > max) max = num1;
  }
  for (const x of args.splice(2)) {
    num1 = Math.floor(Number(x));
    if (num1 === max) continue;
    if (num1 > second) second = num1;
  }
  console.log(second);
}
