// create a function that when called alerts "I'm delayed" after 1 second

function imDelayed () {
  setTimeout(function() {
    console.log('I\'m Delayed!');
  }, 3000);
};

imDelayed();
