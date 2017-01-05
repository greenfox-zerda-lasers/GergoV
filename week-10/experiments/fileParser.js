const fs = require('fs');

var folder = './_data';
var fileList = fs.readdirSync(folder);

var trackList = fileList.filter( function(file) {
   return file.substr(-4) === ".mp3"; 
});

console.log('All files: ',fileList);
console.log('Mp3s only: ', trackList);

/* FORGET THIS QUICK

fs.readdirSync(folder, function(err, files) {
    
    fileList = files.filter( function(file) { 
        return file.substr(-4) === ".mp3"; 
    });
    console.log(fileList);
    
});

console.log(fileList);
// console.log(list);

*/


