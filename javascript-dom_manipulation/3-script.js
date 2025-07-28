#!/usr/bin/node
// Toggles header class between red and green

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('toggle_header').onclick = function () {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  };
});
