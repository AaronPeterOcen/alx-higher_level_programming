#!/usr/bin/node

// Write a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};