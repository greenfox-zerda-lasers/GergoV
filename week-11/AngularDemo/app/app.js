// Display cats from giphy
'use strict';

var mainDisplay = document.getElementById('main_display')
var thumbsArea = document.getElementById('thumbs')


let xhr = new XMLHttpRequest();
xhr.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC&limit=16', true);
xhr.send(null);

xhr.onreadystatechange = initData;

function initData() {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    var giphy = JSON.parse(xhr.response);
    // debugger; // NOTE: uncomment this to observe JSON objects
    // call display function here
    display(giphy.data);
  };
};

function display(displayData) {
  displayData.forEach(function(e) {
      var imgThumbURL = e.images.downsized_still.url;
      var imgGifURL = e.images.downsized.url;
      var img2Disp = document.createElement('img');
      img2Disp.setAttribute('src', imgThumbURL);
      img2Disp.setAttribute('class', 'thumbnail');
      thumbsArea.appendChild(img2Disp);
      img2Disp.addEventListener('click', function() {
        displayGIF(imgGifURL);
      });
      img2Disp.addEventListener('mouseenter', function() {
        displayHoverThumb(img2Disp, imgGifURL);
      });
      img2Disp.addEventListener('mouseleave', function() {
        restoreThumb(img2Disp, imgThumbURL);
      });
  });
};

function displayGIF(url) {
  var bigGif = document.getElementById('main_gif');
  bigGif.setAttribute('src', url);
}

function displayHoverThumb(trg, url) {
  trg.setAttribute('src', url);
}

function restoreThumb(trg, url) {
  trg.setAttribute('src', url);
}
