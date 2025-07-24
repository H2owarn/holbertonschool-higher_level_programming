#!/usr/bin/node

'use strict';

const args = process.argv.slice(2);
const first = args[0];
const secound = args[1];

console.log(`${first ?? 'undefined'} is ${secound ?? 'undefined'}`);
