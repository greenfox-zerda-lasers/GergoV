// This is how it WORKS.

function run(func, arg) {
  func(arg);
}

function greet(name) {
  console.log('Hi ' + name + '!');
}

run(greet, 'Steve'); // "Hi Steve!"
