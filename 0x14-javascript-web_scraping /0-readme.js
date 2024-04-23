#!/usr/bin/node
// Reads a README file

const flsys = require('fs');
flsys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
