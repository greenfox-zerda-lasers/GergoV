'use strict';

window.alert('Hey, let\'s roll.');

// 1.
var king = document.querySelectorAll('.b325');
console.log('1.: ' + king);

// 2.
var conceited = document.querySelectorAll('.b326');
window.alert('2.: ' + conceited)

// 3.
var businessLamp = document.querySelectorAll('.big');
console.log('3.: ' + businessLamp);

// 4.
var conceitedKing = document.querySelectorAll('.container .asteroid');
conceitedKing.forEach(function(e) {
  window.alert('4.:' + e);
});

// 5. The King', 'The Conceited Man' and 'The Lamplighter'
var noBusiness = document.querySelectorAll('div.asteroid');
noBusiness.forEach(function(e) {console.log('5.: ' + e)});

// 6. The Businessman
var allBizniss = document.querySelectorAll('p.asteroid')
window.alert('6.: ' + allBizniss)
