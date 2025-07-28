#!/usr/bin/node
// Adds class red to header when clicking on #red_header

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').onclick = function () {
    document.querySelector('header').classList.add('red');
  };
});
