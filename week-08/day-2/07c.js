// Based on the previous example create an array of images taken from flickr
// https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/

// Display a progress bar while the images are loading
// You can create your own or use the built in HTML5 version:
// https://developer.mozilla.org/en/docs/Web/HTML/Element/progress

var body = document.body;
var imageList = ['https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/',
                 'https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/',
                 'https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/'];

function displayImages () {
  // Create progressbar
  var progressBar = document.createElement('progress');
  progressBar.setAttribute('value', 0);
  progressBar.setAttribute('max', 100);
  body.append.progressBar;

  //Load images

  for (i in imageList) {
    var imgToAdd = document.createElement('img');
    imgToAdd.setAttribute('src', imageList[i]);
    body.append(imgToAdd);

    var progressPercent = (i / imageList.length) * 100;
    progressBar.setAttribute('value', progressPercent);
  };

};

displayImages();
