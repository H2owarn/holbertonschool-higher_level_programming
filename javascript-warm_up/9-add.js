#!/usr/bin/node
'use strict';

const args = process.argv.slice(2);
const first = args[0];
const secound = args[1];

function add (a, b) {
  return parseInt(a, 10) + parseInt(b, 10);
}

if (!first || !secound) {
  console.log('Nan');
} else {
  const result = add(first, secound);
  console.log(result);
}
