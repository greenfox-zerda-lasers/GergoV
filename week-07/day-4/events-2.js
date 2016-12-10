'use strict';

var itemList = document.querySelectorAll('li');
var result = document.querySelector('p');

function answer () {
  result.textContent = itemList.length;
};

var button = document.querySelector('button');
button.addEventListener('click', answer);
