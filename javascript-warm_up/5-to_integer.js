#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Not a number');
} else {
  args.forEach((arg) => {
  //   - /^[+-]?\d+$/ checks if the argument is a valid integer string (with optional + or -)
    const isNumeric = /^[+-]?\d+$/.test(arg); // regex for integers
    if (isNumeric) {
      const num = parseInt(arg, 10); // converts it from string to integer
      console.log('My number:', num);
    } else {
      console.log('Not a number');
    }
  });
}
