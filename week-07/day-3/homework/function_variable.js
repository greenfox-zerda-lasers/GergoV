function sayHi(name) {
  console.log('Hi, ' + name + '!');
};

sayHi('George');

var hiSayer = function(name) {
  console.log('Hi, I say,' + name + '!');
};

// A bit messy.

var fCaller = function(func, param) {
  func(param);
}

fCaller(hiSayer('George'));
