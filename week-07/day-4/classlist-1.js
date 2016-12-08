var stuffINeed = document.querySelectorAll('body p');

// Does the third p have a cat class?
// If so, alert 'YEAH CAT!'

if (stuffINeed[2].classList.contains('cat')) {
    window.alert('YEAH CAT!');
};

// If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
if (stuffINeed[3].classList.contains('dolphin')) {
    stuffINeed[0].textContent = 'pear'
};

// If the first p has an 'apple' class, replace cat's content with 'dog'
window.alert('Now watch.');
if (stuffINeed[0].classList.contains('apple')) {
    stuffINeed[2].textContent = 'dog'
};

// Make apple red
// stuffINeed[0].classList.add('red');
var apple = document.querySelector('.apple');
apple.classList.add('red');

// Make balloon less balloon-like
var balloon = document.querySelector('.balloon');
balloon.classList.remove('balloon');
