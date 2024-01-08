#!/usr/bin/node

// script that prints a square
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}
