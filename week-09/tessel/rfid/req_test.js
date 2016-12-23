var request = require('request');

function lookUpRepos(user) {
    request.get('https://api.github.com/users/' + user, function (error, response, body) {
      if (!error && response.statusCode == 200) {
        console.log(body) // Show response
      }
    });
};

lookUpRepos('geritwo');
