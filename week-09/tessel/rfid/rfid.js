var tessel = require('tessel');
var rfidlib = require('rfid-pn532');
var opn = require('opn');
var request = require('request');

var users = require('./users.json');
var rfid = rfidlib.use(tessel.port['A']);

rfid.on('ready', function (version) {
  console.log('Ready to read RFID card');

  rfid.on('data', function(card) {
    var userID = card.uid.toString('hex')
    // console.log('Card read, UID:', userID);
    // var user = users[userID];
    console.log(card);
  });
});

rfid.on('error', function (err) {
  console.error(err);
});

// Open Window
function showYourRepo(user) {
  var opn = require('opn');
  var gitURL = 'http://github.com/' + user;
  opn('http://github.com/' + user);
};

// GitHub API request
function lookUpRepos(user) {
    request.get('https://api.github.com/users/' + user, function (error, response, body) {
      if (!error && response.statusCode == 200) {
        console.log(body) // Show response
      }
    });

};

function printRepoCount() {
  var responseObj = JSON.parse(this.responseText);
  console.log(responseObj.name + " has " + responseObj.public_repos + " public repositories!");
}
