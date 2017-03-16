// Mp3 file parser for FoxPlayer init

const fs = require('fs');
const mm = require('musicmetadata');


var folder = './_data/';
var fileList = fs.readdirSync(folder);
var trackPathList = [];

// Filter mp3 files from contents of target folder
var mp3List = fileList.filter( function(file) {
return file.substr(-4) === ".mp3";
});

// Add full path to filenames
mp3List.forEach( function(e) {
    trackPathList.push(folder + e);
});

console.log(trackPathList);

// Track metadata parser

var trackListMetaData = [];

trackPathList.map(function(trackPath){
    var parser = new mm(fs.createReadStream(trackPath));
    parser.on('metadata', function(result) {
      console.log(result);
    });
});

console.log(trackListMetaData);
