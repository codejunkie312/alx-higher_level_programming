#!/usr/bin/node
const logMe = (item) => {
  if (typeof logMe.counter === 'undefined') {
    logMe.counter = 0;
  }
  console.log(`${logMe.counter}: ${item}`);
  logMe.counter++;
};
module.exports.logMe = logMe;
