#!/usr/bin/node

let message;

//  script that prints a message depending of the number of arguments passed:
if (process.argv.length === 2) {
  message = 'No argument';
} else if (process.argv.length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
