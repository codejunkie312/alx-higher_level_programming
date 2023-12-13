#!/usr/bin/node
const nbOccurences = (list, searchElement) => {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count += 1;
    }
  }
  return count;
};
module.exports.nbOccurences = nbOccurences;
