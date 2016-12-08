'use strict';

// 1. Alert the content of the heading.
var headerContent = document.querySelector('h1');
window.alert(headerContent);

// 2. Write the content of the first paragraph to the console.
var firstP = document.querySelector('p');
var firstPContent = firstP.textContent;
console.log(firstPContent);

// 3. Alert the content of the second paragraph.
var secondP = document.querySelector('.other');
window.alert(secondP.textContent);


// 4. Replace the heading's content with 'New content'.
var heading = document.querySelector('h1');
heading.textContent = 'OleOleOle';

// 5. Replace the last paragraph's content with the first paragraph's content.
var lastP = document.querySelector('.result');
lastP.textContent = firstPContent;
