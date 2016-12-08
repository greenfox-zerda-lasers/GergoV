'use strict';

var killerContent = document.querySelector('.dog').textContent;
var allParagraphs = document.querySelectorAll('p');
allParagraphs.forEach(function(e) { e.textContent = killerContent });
