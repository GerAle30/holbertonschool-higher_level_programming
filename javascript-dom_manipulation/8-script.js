#!/usr/bin/node
// Fetches hello translation in French and displays it
// Works when imported from head tag

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
