#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (err, response, body) => {
  if (err) {
    throw new Error(err);
  }
  const data = JSON.parse(body);
  let results = {};
  for (const user in data) {
    if (data[user].completed) {
      if (results[data[user].userId] === undefined) {
        results[data[user].userId] = 1;
      } else {
        results[data[user].userId] += 1;
      }
    }
  }
  console.log(results);
});
