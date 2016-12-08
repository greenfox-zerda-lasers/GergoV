var bookmarklet = document.querySelector('a');

function replaceH1s () {
  var headings = document.querySelectorAll('h1');
  headings.forEach(function(e) {
    e.textContent = 'BLAH!';
});
}

// bookmarklet.addEventListener('click', replaceH1s);

 // <a href="javascript:alert('Hello!');">Drag me in the bookmarks bar!</a>
