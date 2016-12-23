
var Ajax = function (){

	this.APIEndpoint = 'https://mysterious-dusk-8248.herokuapp.com/';

	this.list = function(callback) {
		this.open('GET', 'todos', false, callback);
	}

	this.post = function(postData, callback) {
		this.open('POST', 'todos', postData, callback);
	}

	this.update = function(postData, id, callback) {
		this.open('PUT', 'todos/' + id, postData, callback);
	}

	this.del = function(id, callback) {
		this.open('DELETE', 'todos/' + id, false, callback);
	}

	this.open = function(method, resource, data, callback) {
		var xhr = new XMLHttpRequest();
		data = (data) ? data : null;
		xhr.open( method, this.APIEndpoint + resource )

		if( method !== 'DELETE' ) {
			xhr.setRequestHeader('Content-Type', 'application/json');
		}

		xhr.send( JSON.stringify(data) );
		xhr.onreadystatechange = function (rsp) {
			if( xhr.readyState === XMLHttpRequest.DONE ) {
				callback( JSON.parse(xhr.response) );
			}
		}
	}
} 
