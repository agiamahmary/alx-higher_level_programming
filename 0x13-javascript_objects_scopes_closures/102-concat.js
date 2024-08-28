#!/usr/bin/node
const fs = require('fs');
fs.open(process.argv[4], 'w', (err) => {
  if (err) {
    console.log(err);
  }
});
process.argv.slice(2, 4).forEach((file) => {
  fs.open(file, 'r', (err) => {
    if (err) {
      console.log(err);
    }
  });
  fs.readFile(file, (err, data) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(process.argv[4], data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
});
