function updateTask(id, string){
  let xhr = new XMLHttpRequest();
  xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  xhr.setRequestHeader("Content-type", "application/json");

  xhr.send(JSON.stringify({text: string, completed: true}));
  xhr.onreadystatechange = putReady;

  function putReady(rsp) {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(xhr.response)) // NOTE: for debug
    };
  };
};
