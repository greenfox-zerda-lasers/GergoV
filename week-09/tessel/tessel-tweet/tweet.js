// Node requires
var twitter = require('twitter');

var twitterHandle = '@geritwo';
// The status to tweet
var status = 'Hello world. This a #Tessel 2 speaking.';

// These OAuth credentials are for the dummy @TesselTweet account
// Paste in your own OAuth details if you want to tweet from your own account
var twit = new twitter({
  consumer_key: 'DPZpWnJctDBSkEYA6mZEniZdE',
  consumer_secret: '35YCPouqQmQo8AuK384lkDp3t2lSN2hlbZyKMj2pnJ0VZFwri8',
  access_token_key: '1012381-8CSWoaH2WLBDOQa4XgrgRhl2uH4dnNyMgsgZyouaF5',
  access_token_secret: 'hJ4SFhUXRGIGcGIaDOJtccebwsoHNSaMai0axaj9JDZAD'
});

// Make a tweet!
twit.post('statuses/update', {status: status}, function(error, tweet, response){
  if (error) {
    console.log('error sending tweet:', error);
  } else {
    console.log('Successfully tweeted! Tweet text:', tweet.text);
  }
});
