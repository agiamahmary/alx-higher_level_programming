#!/usr/bin/node
exports.converter = function (base) {
  let ans = '';
  const digit = '0123456789abcdef';

  function myConverter (number) {
    while (number > 0) {
      ans += (digit[number % base]).toString();
      number = Math.floor(number / base);
    }
    return ans;
  }
  return myConverter;
};
