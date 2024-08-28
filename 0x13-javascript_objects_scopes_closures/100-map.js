#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((elmnt, idx) => elmnt * idx);
console.log(list);
console.log(newList);
