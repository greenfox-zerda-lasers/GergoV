// Init mp3 files and create filelist

const fs = require('fs');

var fileParser = (function() {
    
    var folder = './_data';
    var fileList = fs.readdirSync(folder);

    var trackList = fileList.filter( function(file) {
    return file.substr(-4) === ".mp3"; 
    });
    
    function getTrackList () {
      return trackList;  
    };
    
    return {
        getFiles : getTrackList
    };
})();

var trackList = fileParser.getFiles();
console.log(trackList);

// Parse mp3 data and fill database (?)
 
