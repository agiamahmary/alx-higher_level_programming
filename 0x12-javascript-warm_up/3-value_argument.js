#!/usr/bin/node
// prints a string

const args = process.argv;

if (isNaN(args[2])) console.log('No argument');
for (const arg of args.splice(2)) {
  console.log(`${arg}`);
}
