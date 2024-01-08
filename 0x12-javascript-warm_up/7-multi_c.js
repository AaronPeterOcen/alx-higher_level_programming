#!/usr/bin/node

// script that prints x times “C is fun”
const x = process.argv[2];
let i = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (i < x) {
  console.log('C is fun');
  i++;
}
