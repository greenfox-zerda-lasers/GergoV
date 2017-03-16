// AIRCRAFTS AND CARRIERS

// Basic type data
var aircraftTypes = {'F16': [8, 30], 'F35': [10, 50]};

// 'Classes'
function Aircraft(type) {
  this.type = type;
  this.maxAmmo = aircraftTypes[type][0];
  this.baseDamage = aircraftTypes[type][1];
  this.ammo = 0;
};

function Carrier(ammoStored) {
  this.ammoStored = ammoStored;
  this.aircrafts = [];
  this.healthPoints = 3000;
};

function AmmoError() {
  this.name = 'InsufficientAmmo';
  this.message = 'Insufficient ammo on carrier!';
}

// Methods
Aircraft.prototype.status_report = function() {
  console.log('Type ' + this.type + ', Ammo: ' + this.ammo + ', Base Damage: ' + this.baseDamage + ', All Damage: ' + this.baseDamage*this.ammo);
};

Aircraft.prototype.fill = function(amount) {
  var ammoSpace = this.maxAmmo - this.ammo;
  var remainder = 0;
  if (amount <= ammoSpace) {
    this.ammo += amount;
  } else {
    remainder = amount - ammoSpace;
    this.ammo += ammoSpace;
  };
  return remainder;
};

Aircraft.prototype.fight = function() {
  this.ammoFired = this.ammo;
  this.ammo -= this.ammoFired;
  return this.baseDamage*this.ammoFired;
};

Carrier.prototype.add_aircraft = function(aircraft) {
  this.aircrafts.push(aircraft);
};

Carrier.prototype.status_report = function() {
  var aircraftCount = this.aircrafts.length;
  var totalDamage = 0;
  if (this.healthPoints <= 0) {
    console.log('It\'s dead, Jim. :(');
  } else {
    this.aircrafts.forEach(function(e) {
      totalDamage += e.ammo * e.baseDamage;
    });
    console.log('Aircraft count: ' + aircraftCount + ', Ammo Storage: ' + this.ammoStored + ', Total damage: ' + totalDamage + ', Health Remaining: ' + this.healthPoints);
    console.log('Aircrafts:');
    this.aircrafts.forEach(function(e) {
      e.status_report();
    });
  };
};

Carrier.prototype.fill = function() {
  var ammoNeeded = 0;
  var remainingAmmo = 0;
  this.aircrafts.forEach(function(e) {
    ammoNeeded += (e.maxAmmo - e.ammo);
  });
  if (ammoNeeded > this.ammoStored) {
    throw new AmmoError();
  } else {
    this.aircrafts.reduce(function(a, e) {
      return e.fill(a); // returns remainingAmmo supposedly;
    }, this.ammoStored);
  };
};

Carrier.prototype.fight = function() {
  var totalDamage = 0;
  this.aircrafts.forEach(function(e) {
    totalDamage += e.fight();
  }, this);
  return totalDamage;
};


// Instantiations
var fighter1 = new Aircraft('F16');
var fighter2 = new Aircraft('F16');
var fighter3 = new Aircraft('F35');
var fighter4 = new Aircraft('F16');

var carrier1 = new Carrier(500);

carrier1.add_aircraft(fighter1);
carrier1.add_aircraft(fighter2);
carrier1.add_aircraft(fighter3);
carrier1.add_aircraft(fighter4);


// Type F35, Ammo: 10, Base Damage: 50, All Damage: 500