#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length === 2 || isNaN(Number(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  const num = Math.floor(Number(args[2]));
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
