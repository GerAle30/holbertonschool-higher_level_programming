#!/usr/bin/node
// Adds a li element to a list when clicking on #add_item

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').onclick = function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
  };
});
