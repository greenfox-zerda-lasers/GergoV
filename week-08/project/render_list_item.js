// JSON to html render attempt

function renderListItem(parent, pattern) {
  pattern.forEach(function(e) {
    // create tag
    var currentElement = document.createElement(e.tag);

    // set attributes
    for (var prop in e.attributes(function{
      currentElement.setAttribute(prop, e.attributes[prop]);
    });

    //create children
    e.children.forEach(function (e){
      var childName = e;
      examplePattern.forEach(function(f) {
        if (childName == f.name) {
          renderListItem(currentElement, // NOTE: i gave up at this point)
          // NOTE: Structure doesn't make recursive calls possible
        };
      });
    });

    parent.appendChild(currentElement);

  });
  var currentElement = document.createElement('')
}

var examplePattern = [
  {
    name: 'todo-li',
    tag: 'li',
    attributes: {},
    children: ['todo-1abel']
  },
  {
    name: 'todo-label',
    tag: 'label',
    attributes: {
      class: 'todo-item',
      for: 'list-item'
    },
    children: ['remove-button', 'todo-checkbox', 'span']
  },
  {
    name: 'remove-button',
    tag: 'input',
    attributes: {
      type: 'button',
      id: 'list-item-remove',
    },
    children: []
  },
  {
    name: 'todo-checkbox',
    tag: 'input',
    attributes: {
      type: 'checkbox',
      name: 'complete-item',
      id: 'list-item'
    },
    children: []
  },
  {
    name: 'span',
    tag: 'span',
    attributes: {},
    children: []
  }];
