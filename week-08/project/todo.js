'use strict';

// Main interface

var inputFieldAddButton = document.getElementById('add-todo-button');
var todoList = document.querySelector('ul');

// Dynamic
var todoCheckBox = document.getElementById('list-item');
var todoDeleteButton = document.getElementById('list-item-remove')

// XHR

let xhr = new XMLHttpRequest();
xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos?api_key=63r17w0', true);
xhr.send(null);

xhr.onreadystatechange = initData;
