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
    displayData(todoData);
  };
};

function displayData(data) {
  data.forEach(function(e) {
    var itemToView = document.createElement('li');
    itemToView.textContent = 'ID: ' + e.id + ', ' + e.text + ', ' + e.completed;
    todoList.appendChild(itemToView);
  });
  //debugger;
  // generate elements
};

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
