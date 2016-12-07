'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grades: [],
  addgrade: function (grade) {
    this.grades.push(grade);
  },
  getAverage: function () {
    return this.grades.reduce (function(a, b) {
      return a + b;
    }, 0) / this.grades.length;
  }
};
