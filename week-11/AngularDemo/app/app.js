// Display cats from giphy
'use strict';

// Angular
var catFinder3000 = angular.module('catFinder3000', []);

catFinder3000.controller('renderCats', function($scope) {

  // TODO:
  // Get query
  // Initiate request

  getCatGifs("funny", 0, function(data) {
    // NOTE: Fot debug, see data in console:
    console.log("Set: ", data);

    var catGifData = [];
    data.forEach(function(e){
      var catGif = {
        "thumbStill" : e.images.fixed_height_still.url,
        "thumb" : e.images.fixed_height.url,
        "gif" : e.images.downsized.url,
        "embed": e.embed_url
      };
      catGifData.push(catGif);
    });

    $scope.imageData = catGifData;
  });

});


// AJAX API request
function getCatGifs(query, offset, callback) {

  let apiReq = "http://api.giphy.com/v1/gifs/search?q=" + query + "+cat&api_key=dc6zaTOxFJmzC&limit=8&offset=" + offset

  let xhr = new XMLHttpRequest();
  xhr.open('GET', apiReq, true);
  xhr.send(null);

  xhr.onreadystatechange = initData;

  function initData() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      var giphy = JSON.parse(xhr.response);
      callback(giphy.data);
    };
  };

};
