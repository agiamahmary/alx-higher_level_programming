#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const elmnt of list) {
    if (elmnt === searchElement) {
      i += 1;
    }
  }
  return i;
};
