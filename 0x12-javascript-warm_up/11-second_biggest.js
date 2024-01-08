#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments.
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}
const arr = args.slice(2).map(Number);
arr.sort((a, b) => a - b);
console.log(arr[arr.length - 2]);
