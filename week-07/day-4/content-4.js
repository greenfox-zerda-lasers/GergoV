// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

var nicelist = ['apple', 'banana', 'cat', 'dog'];
var listItems = document.querySelectorAll('li');
listItems.forEach(function(e, i) {
    e.textContent = nicelist[i];
});
