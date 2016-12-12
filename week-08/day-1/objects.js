// JS protyping basics
// From FunFunFiction JS OO video #46

'use strict';

function talk() {
    console.log(this.sound);
};

let animal = {
    talk;
};

let dog = {
    sound: 'Woof!'
};

let prairieDog = {
    howl: function() {
        console.log(this.sound.toUpperCase())
    };
};

Object.setPrototypeOf(dog, animal);
dog.talk()
Object.setPrototypeOf(prairieDog, dog);
prairieDog.howl();