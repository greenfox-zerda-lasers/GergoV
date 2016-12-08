'use strict';

var theList = document.querySelector('.asteroids');

theList.removeChild(theList.children[0]);

planetData.forEach(function(e) {
    if (e.asteroid == true) {
		var addThis = document.createElement('li');
		addThis.textContent = e.content;
		addThis.setAttribute('class', e.category);
		theList.appendChild(addThis);
    }
});
