#!/usr/bin/node
// Updates header color to red when clicking on #red_header

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').onclick = function () {
    document.querySelector('header').style.color = '#FF0000';
  };
});
