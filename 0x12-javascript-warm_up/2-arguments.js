#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length <= 2) console.log('No argument');
else console.log((args.length === 3) ? 'Argument found' : 'Arguments found');
