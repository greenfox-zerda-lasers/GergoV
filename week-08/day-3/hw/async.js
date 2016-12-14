'use strict';

window.onload = function(){
  var http = new XMLHttpRequest();
  
  http.onreadystatechange = function(){
      if(http.readyState == 4 && http.status == 200){
          console.log(JSON.parse(http.response));
      };
  };
  
  http.open("GET", "./data/example.json", true);
  http.send();
  console.log(http)
};



