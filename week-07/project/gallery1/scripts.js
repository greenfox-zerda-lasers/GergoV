'use strict';

var imageCache = [
  {
    url: 'joshua-tree-national-park-74399_1280.jpg',
    title: 'Joshua Tree',
    description: 'The desert is endless. Look at the dunes spreading all over the horizon.'
  },
  {
    url: 'beach-84631_1280.jpg',
    title: 'Sandy beach',
    description: 'This is the perfect place for a holiday. Or a perfect poster on your wall in a housing estate apartment in the 1980\'s.'
  },
  {
    url: 'iceberg-404966_1280.jpg',
    title: 'Iceberg',
    description: 'Iceberg, Rosenberg... I don\'t really care.'
  },
  {
    url: 'lake-65443_1280.jpg',
    title: 'Lake',
    description: 'Want to take a dive?'
  },
  {
    url: 'prairie-679016_1920.jpg',
    title: 'Prairie',
    description: 'Prairie wolves roam these endless prairies praying for prey.'
  },
  {
    url: 'sunset-1700877_1280.jpg',
    title: 'Sunset',
    description: 'End of the day. Good-bye!'
  },
  {
    url: 'the-scenery-679011_1280.jpg',
    title: 'Scenery',
    description: 'Ahm, some really nice view. What else to say.'
  },
];

function getImageCount () { 
	return imageCache.length; 
};

var mainImage = document.querySelector('.main-image');
var currentTitle = mainImage.querySelector('h2');
var currentDescription = mainImage.querySelector('p');

var button = document.querySelectorAll('.side-nav-button');

var thumbsBar = document.querySelector('.image-thumbnail-bar');

function generateThumbs() {
  imageCache.forEach(function(e, i) {
    var newThumb = document.createElement('div')
    newThumb.setAttribute('class', 'thumbnail');
    newThumb.setAttribute('thumb-index', i);
		newThumb.setAttribute('alt', e.title);
    var thumbImgValue = 'background-image: url(./src/' + e.url + ')';
    newThumb.setAttribute('style', thumbImgValue);
    thumbsBar.appendChild(newThumb);
    newThumb.addEventListener('click', clickThumb);
  });
};

function clickThumb() {
  var clickedThumbIndex = this.getAttribute('thumb-index');
  mainImageSetter(clickedThumbIndex);
};

function mainImageSetter(clickedThumbIndex) {
	var mainImageToThis = imageCache[clickedThumbIndex].url;
	mainImage.style.backgroundImage = 'url(./src/' + mainImageToThis + ')';
	
	currentTitle.innerText = imageCache[clickedThumbIndex].title;
	currentDescription.innerText = imageCache[clickedThumbIndex].description;
	
};

mainImageSetter(0);
generateThumbs();
