// Music player functions

var tracks = [
  {"title":"Purple_Drift", "artist":"Organoid", "length":123, "src":"./Organoid_-_09_-_Purple_Drift.mp3"},
  {"title":"Yellow Suicide", "artist":"Slow Velvet", "length":123, "src":""},
];

const trackListUL = document.querySelector('ol');
const musicPlayer = document.querySelector('audio');

var displayTracklist = function(tracks) {
  tracks.forEach(function(e, i) {
    var itemToDisplay = document.createElement('li');
    var trackInfo = "track, " + "Title: \"" + e.title + "\", Performer: " + e.artist;
    itemToDisplay.textContent = trackInfo;
    trackListUL.appendChild(itemToDisplay);
    itemToDisplay.addEventListener('click', function() {
      playSelectedTrack(e); // magic call with full db data item
    });
  });
};

var playSelectedTrack = function(trackinfo) {
  console.log("Selected track: " + trackinfo.title);
  musicPlayer.src = trackinfo.src;
}

// Convert Duration to readable:
function readableDuration(seconds) {
    sec = Math.floor( seconds );
    min = Math.floor( sec / 60 );
    min = min >= 10 ? min : '0' + min;
    sec = Math.floor( sec % 60 );
    sec = sec >= 10 ? sec : '0' + sec;
    return min + ':' + sec;
}

// MEDIA EVENT listeners: load, start, end, progress

musicPlayer.addEventListener('loadstart', function() { console.log("Track loaded.") });
musicPlayer.addEventListener('play', function() { console.log("Playing started.") });
musicPlayer.addEventListener('ended', function() { console.log("Track finished.") });
musicPlayer.addEventListener('progress', function() { console.log("Progress signal.") });
musicPlayer.addEventListener('pause', function() { console.log("Track paused.") });

// RUN

// Display tracks
displayTracklist(tracks);

// Then clicky-clicky
