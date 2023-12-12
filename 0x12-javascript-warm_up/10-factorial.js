#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(process.argv[2] ? factorial(parseInt(process.argv[2])) : 1);
