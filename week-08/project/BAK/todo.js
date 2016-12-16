'use strict';

// __MAIN INTERFACE__

var inputFieldAddButton = document.getElementById('add-todo-button');
var inputFieldElement = document.getElementById('submit-todo-field');

inputFieldAddButton.addEventListener('click', function () {
    addNewTask(inputFieldElement.value);
});

var todoList = document.querySelector('ul');

// Dynamic
var todoCheckBox = document.getElementById('list-item');
var todoDeleteButton = document.getElementById('list-item-remove')

// Server I/O - read + View: render

function getWholeList() {

  let getList = new XMLHttpRequest();
  getList.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);

  getList.setRequestHeader("Content-type", "application/json");

  getList.send(null);
  getList.onreadystatechange = initGetData;

  function initGetData() {
    if (getList.readyState === XMLHttpRequest.DONE && getList.status == 200) {
      var todoData = JSON.parse(getList.response);
      renderDisplay(todoData);
    };
  };
};

function renderDisplay(data) {
  // todoList.innerHTML = '' // clear list
  data.forEach(function(e, i) {
    var itemToView = document.createElement('li');

    var todoLabel = document.createElement('label');
    todoLabel.setAttribute('class', 'todo-item');
    todoLabel.setAttribute('for', 'list-item-' + i);

    var todoText = document.createElement('p');
    todoText.textContent = e.text;

    var removeTodo = document.createElement('input');
    removeTodo.setAttribute('type', 'button');
    removeTodo.setAttribute('id', 'list-item-remove');

    var checkBox = document.createElement('input');
    checkBox.setAttribute('type', 'checkbox');
    checkBox.setAttribute('name', 'complete-item');
    checkBox.setAttribute('id', 'list-item-' + i);
    if (e.completed === true) {
      checkBox.setAttribute('checked', 'checked');
    } else if (e.completed === false) {
      checkBox.removeAttribute('checked','checked');
    };

    var spriteSpan = document.createElement('span');

    // append elements
    todoList.appendChild(itemToView);
    itemToView.appendChild(todoLabel);
    todoLabel.appendChild(todoText);
    todoLabel.appendChild(removeTodo);
    todoLabel.appendChild(checkBox);
    todoLabel.appendChild(spriteSpan);

    // Click listeners

    // Needed to add event listeners to both label and icon (span)
    // because without it whole
    spriteSpan.addEventListener('click', function() {
      changeTaskStatus(e.id, e.text, e.completed);
    });
    todoText.addEventListener('click', function() {
      changeTaskStatus(e.id, e.text, e.completed);
    });

    // removal
    removeTodo.addEventListener('click', function() {
      deleteTask(e.id);
    });

  });
  console.log('Display Rendered!')
  console.log(data.length + ' items displayed.');
};

// *** FUNCTION DEFINITIONS ***

function addNewTask(task){
  let postList = new XMLHttpRequest();
  postList.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(JSON.stringify({text: task}));
  postList.onreadystatechange = postReady;

  function postReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response))
    };
  };
};

function deleteTask(id){
  let postList = new XMLHttpRequest();
  postList.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(null);
  postList.onreadystatechange = delReady;

  function delReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response));
    };
  };
};

function changeTaskStatus(id, string, status){
  // NOTE: Must send with current string.

  let postList = new XMLHttpRequest();
  postList.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(JSON.stringify({text: string, completed: !status}));
  postList.onreadystatechange = putReady;

  function putReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response))
    };
  };
};


// MAIN LOOP
getWholeList();
