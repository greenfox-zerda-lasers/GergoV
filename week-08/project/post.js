function updateTask(id, string){
  let postList = new XMLHttpRequest();
  postList.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);

  postList.setRequestHeader("Content-type", "application/json");

  postList.send(JSON.stringify({text: string, completed: true}));
  postList.onreadystatechange = putReady;

  function putReady(rsp) {
    if (postList.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(postList.response))
    };
  };
};
