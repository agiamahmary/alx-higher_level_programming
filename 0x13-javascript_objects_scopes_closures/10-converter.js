#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (number) {
    if (number < base) {
      if (number <= 10) {
        return number.toString();
      }
      return String.fromCharCode('A'.charCodeAt(0) + (number % base) - 10);
    }
    if ((number % base) > 10) {
      return myConverter(Math.floor(number / base)) + String.fromCharCode('A'.charCodeAt(0) + (number % base) - 10);
    }
    return myConverter(Math.floor(number / base)) + (number % base).toString();
  }
  return myConverter;
};
