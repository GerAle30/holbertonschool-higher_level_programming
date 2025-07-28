#!/usr/bin/node
// Updates header text to "New Header!!!" when clicking on #update_header

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('update_header').onclick = function () {
    document.querySelector('header').textContent = 'New Header!!!';
  };
});
