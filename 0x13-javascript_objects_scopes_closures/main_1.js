#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(16);

for (var index = 0; index < 100; index++) {
    console.log(("" + myConverter(index)).toLowerCase());
}
