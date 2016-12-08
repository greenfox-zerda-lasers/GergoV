'use strict';

var theList = document.querySelector('.asteroids');
theList.removeChild(theList.children[0]);

var newContent = ['apple', 'bubble', 'cat', 'green fox'];
//for (i = 0; i < newContent.length; i++);

newContent.forEach(function(e) {
  var newItem = document.createElement('li');
  newItem.textContent = e;
  theList.appendChild(newItem);
});
