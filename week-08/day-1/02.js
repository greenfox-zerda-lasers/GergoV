'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b) {
  this.a = a;
  this.b = b;
};

Rectangle.prototype.getArea = function () {
  return this.a * this.b;
};

Rectangle.prototype.getCircumference = function () {
  return (this.a*2) + (this.b*2);
};
