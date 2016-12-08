var asteroids = document.querySelector('.asteroids');
asteroids.removeChild(asteroids.children[0]);

for (i = 0; i < 3; i++) {
  var theFox = document.createElement('li');
  theFox.textContent = 'The Fox';
  asteroids.appendChild(theFox);
};
