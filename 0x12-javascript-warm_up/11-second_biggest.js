#!/usr/bin/node
console.log(process.argv[2] && process.argv.length > 3 ? process.argv.sort((a, b) => a - b)[process.argv.length - 2] : 0);
