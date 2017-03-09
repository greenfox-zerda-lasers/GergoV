'use strict';

var galleryControls = (function() {
  var rightBezel = document.querySelector(".main-image-bezel-right");

  rightBezel.addEventListener("mouseover", function changeBgColor);

  function changeBgColor() {
    rightBezel.style.background = "lime";
  }

})()

var setUpControls = (function() {
  // here be dragons
})()
