// Ptypes in use

function Car(km) {
 this.km = km;
}

Car.prototype.ride = function(km) {
 this.km += km;
}

var volvo = new Car(80000);
volvo.ride(120);
console.log(volvo.km); // 80120
