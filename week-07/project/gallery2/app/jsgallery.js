'use strict';


// *** Load images and thumbnails ***

function httpGetAsync(url, callback) {
  const xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
      callback(xmlHttp.responseText);
    }
  };
  xmlHttp.open("GET", url, true); // true for asynchronous
  xmlHttp.send(null);
}

function renderImages(images) {
  let imageList = JSON.parse(images); // So that it becomes an array
  let imagesNo = imageList.length;
  console.log(imageList, imagesNo); // NOTE: Debug;
  // NOTE: imageList looks like an array tho not an array.
  imageList.forEach( function(image, index) {
    let currentImage = document.createElement('img');
    currentImage.dataset.index = index;
    currentImage.setAttribute('src', image);
    if (index === 0) {
      mainImage.setAttribute('style', 'background-image: url(' + image + ')');
      currentImage.setAttribute('class', 'thumbnail-active');
    } else {
      currentImage.setAttribute('class', 'thumbnail');
    }
    thumbnailBar.appendChild(currentImage);
  });
}

httpGetAsync('http://localhost:8080/files', renderImages);

// *** Fetch interactive elements ***

const mainImage = document.querySelector('.main-image-display');
const leftBezel = document.querySelector('.main-image-bezel-left');
const rightBezel = document.querySelector('.main-image-bezel-right');

const leftArrow = document.querySelector('#arrow-left');
const rightArrow = document.querySelector('#arrow-right');

const thumbnailBar = document.querySelector('.thumbnail-wrapper');
const thumbnail = document.querySelectorAll('.thumbnail');
const activeThumbnail = document.querySelector('.thumbnail-active');

// *** Handle actions ***

// ** Main image **
// Bezel hover
// Bezel clicks
// ** Thumbs **
// Hover: info popup
// Click: image switch
