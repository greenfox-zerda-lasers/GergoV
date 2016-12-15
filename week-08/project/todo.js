'use strict';

// Main interface

var inputFieldAddButton = document.getElementById('add-todo-button');
var todoList = document.querySelector('ul');

// Dynamic
var todoCheckBox = document.getElementById('list-item');
var todoDeleteButton = document.getElementById('list-item-remove')

// Server I/O

let getList = new XMLHttpRequest();
getList.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
getList.send(null);
getList.onreadystatechange = initGetData;

function initGetData() {
  if (getList.readyState === XMLHttpRequest.DONE && getList.status == 200) {
    var todoData = JSON.parse(getList.response);
    viewDisplayData(todoData);
  };
};

function viewDisplayData(data) {
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
    checkBox.setAttribute('checked','checked');
    if (e.completed == false) {
      checkBox.removeAttribute('checked','checked');
    };
    var spriteSpan = document.createElement('span');

    // NOTE: Quick view for debugging API I/O
    itemToView.textContent = 'ID: ' + e.id + ', ' + e.text + ', ' + e.completed;
    todoList.appendChild(itemToView);
    itemToView.appendChild(todoLabel);
    todoLabel.appendChild(todoText);
    todoLabel.appendChild(removeTodo);
    todoLabel.appendChild(checkBox);
    todoLabel.appendChild(spriteSpan);

  });
};

function viewAddTask() {
  window.alert('add');
};

function viewCheckTask() {
  window.alert('check');
};

function viewDeleteTask() {
  windows.alert('delete');
};

// Add, Check, Remove

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

function updateTask(id, string){
  let postList = new XMLHttpRequest();
  postList.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(JSON.stringify({text: string, completed: true}));
  postList.onreadystatechange = putReady;

  function putReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response))
    };
  };
};
