#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (err, response, body) => {
  if (err) {
    throw new Error(err);
  }
  const results = {};
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      if (!(data[i].userId in results)) {
        results[data[i].userId] = 0;
      }
      results[data[i].userId] += 1;
    }
  }
  console.log(results);
});
