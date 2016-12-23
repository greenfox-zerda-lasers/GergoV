var tessel = require('tessel');
var rfidlib = require('rfid-pn532');

var users = require('./users.json');
var rfid = rfidlib.use(tessel.port['A']);

rfid.on('ready', function (version) {
  console.log('Ready to read RFID card');

  rfid.on('data', function(card) {
    var userID = card.uid.toString('hex')
    console.log('Card read, UID:', userID);
    var user = users[userID];
    console.log(user);
  });
});
