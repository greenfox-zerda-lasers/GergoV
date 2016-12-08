var bookmarklet = document.querySelector('a');

function replaceImgs () {
  var images = document.querySelectorAll('img');
  images.forEach(function(e) {
    e.setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/736x/aa/00/40/aa0040a22096c2fc2d35a91b5fad1d04.jpg');
});
}

// bookmarklet.addEventListener('click', replaceH1s);

 // <a href="javascript:alert('Hello!');">Drag me in the bookmarks bar!</a>
