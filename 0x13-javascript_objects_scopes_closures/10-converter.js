#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (number) {
    if (number >= 0) {
      if ((number % base) > 10) {
        return String.fromCharCode('A'.charCodeAt(0) + (number % base) - 10);
      }
      return myConverter(Math.floor(number / base)) + (number % base).toString();
    }
    return '';
  }
  return myConverter;
};
