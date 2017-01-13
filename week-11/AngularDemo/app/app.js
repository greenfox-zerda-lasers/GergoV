// Display cats from giphy
'use strict';

// Angular
var catFinder3000 = angular.module('catFinder3000', []);

catFinder3000.controller('renderCats', function($scope) {

  // NOTE: TEST $scope.catNames = ['Paws','Peanut','Charlie','Misty','Coco'];

  getCatGifs("funny", 0, function(data) {
    console.log("Set: ", data);
    $scope.imageData = data;
  });

});


// AJAX API request
function getCatGifs(query, offset, callback) {
  var catGifList = [];

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
