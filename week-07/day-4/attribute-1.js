// Write the image's url to the console.
var rokakoma = document.querySelector('img');
// console.log(rokakoma.src);
console.log(rokakoma.getAttribute('src'));

// Replace the image with a picture of yourself.
rokakoma.setAttribute('src', 'https://farm8.staticflickr.com/7282/buddyicons/55142701@N00_r.jpg')

// Make the link point to the Green Fox Academy website.
var siteLink = document.querySelector('a');
siteLink.setAttribute('href', 'http://greenfoxacademy.com');

// Disable the second button.
var badButton = document.querySelector('.this-one');
badButton.disabled = true

// Replace its text with 'Don't click me!'.
badButton.textContent = 'Don\'t click me!'

/*
var littlePrince = document.querySelector('img');
console.log(littlePrince.getAttribute('src'));
littlePrince.setAttribute('src', 'http://deji.chez.com/dessins/pp1.gif');
*/
