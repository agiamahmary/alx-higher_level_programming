#!/usr/bin/node

const args = process.argv;

if (args.length !== 3 || isNaN(Number(args[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(Number(args[2]))}`);
}
