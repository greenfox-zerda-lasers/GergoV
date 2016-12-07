var student = {
  name: 'Darth Vader',
  age: 42,
  isForceSensitive: true
};

console.log(student.name); // 'Darth Vader'
var key = 'age'
console.log(student[key]); // 42

console.log(Object.keys(student)); // ['name', 'age', 'isForceSensitive']
