#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length <= 2) console.log('No argument');
for (const arg of args) {
  console.log(`${arg}`);
}
