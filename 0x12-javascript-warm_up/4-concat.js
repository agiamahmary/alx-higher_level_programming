#!/usr/bin/node
// prints a string

const args = process.argv;

if (args.length === 2) {
  console.log('undefined is undefined');
} else if (args.length === 3) {
  console.log(`${args[2]} is undefined`);
} else {
  const str = args[2] + ' is ' + args[3];
  console.log(str);
}
