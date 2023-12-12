#!/usr/bin/node
if (parseInt(process.argv[2], 10)) {
  for (let i = 0; i < parseInt(process.argv[2], 10); i++) {
    console.log('X'.repeat(parseInt(process.argv[2], 10)));
  }
} else {
  console.log('Missing size');
}
