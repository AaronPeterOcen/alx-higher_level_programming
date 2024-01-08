#!/usr/bin/node

//  script that computes and prints a factorial
const argv = process.argv;
const num = parseInt(argv[2]);
function factorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
