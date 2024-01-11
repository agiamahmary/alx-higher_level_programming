#!/usr/bin/node
// prints a string

const args = process.argv;

if (args[2] == undefined) {
  console.log('No argument');
}
for (const arg of args.splice(2)) {
  console.log(`${arg}`);
}
