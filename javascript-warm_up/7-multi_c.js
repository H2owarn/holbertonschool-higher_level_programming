#!/usr/bin/node

const args = process.argv.slice(2);
const isInteger = /^[+-]?\d+$/.test(args);

if (isInteger) {
  const num = parseInt(args, 10);
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i += 1;
  }
} else {
  console.log('Missing number of occurrences');
}
