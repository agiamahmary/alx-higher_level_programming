#!/usr/bin/node
// prints the second biggest number

const args = process.argv;

if (args.length <= 3) {
  console.log("Not enough numbers provided.");
} else {
  let max = Number(args[2]);
  let second = Number(args[2]);

  for (let i = 3; i < args.length; i++) {
    const num = Number(args[i]);
    
    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num !== max) {
      second = num;
    }
  }

  console.log(second);
}
