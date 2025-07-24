#!/usr/bin/node
'use strict';

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const args = parseInt(process.argv[2], 10);
const result = factorial(args);

console.log(result);
