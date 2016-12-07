var car = {
  km: 120000,
  ride: function(km) {
    this.km += km;
  }
};

car.ride(200);
console.log(car.km); // 120200
