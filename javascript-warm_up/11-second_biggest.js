#!/usr/bin/node

// Get arguments passed from the command line
const rawArgs = process.argv.slice(2);
// Convert each argument to an integer
const convertedArgs = rawArgs.map((arg) => parseInt(arg, 10));
// Remove any values that are NaN
const args = convertedArgs.filter((n) => !isNaN(n));

if (args.length < 2) {
  console.log(0);
} else {
// Sort in descending order
// args = [5, 3, 9, 1]; → [9, 5, 3, 1]
  args.sort((a, b) => b - a);

  // Find the first number that is smaller than the max
  const max = args[0];
  const second = args.find((n) => n < max);

  console.log(second ?? 0);
}
