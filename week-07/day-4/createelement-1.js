var asteroidList = document.querySelector('ul.asteroids');

// Add an item that says 'The Green Fox' to the asteroid list.
var newAsteroid = document.createElement('li');
newAsteroid.id = 'b555';
newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);

// Add an item that says 'The Lamplighter' to the asteroid list.
var lampLighter = document.createElement('li');
asteroidList.appendChild(lampLighter);
lampLighter.textContent = 'The Lamp Lighter';

// Add a heading saying 'I can add elements to the DOM!' to the .container.
var newHeader = document.createElement('h1');
newHeader.textContent = 'Hey YO!';
var container = document.querySelector('.container');
container.appendChild(newHeader);

// Add an image, any image, to the container.
window.alert('Most jön a róka!')
roka = document.createElement('img')
roka.src = "http://m.cdn.blog.hu/ko/konyves/image/0803/kisherceg5.jpg"
roka.alt = "A Kis Herceg és a róka"
container.append(roka)
