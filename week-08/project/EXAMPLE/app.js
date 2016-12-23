'use strict';

var App = function () {

	this.ajax = new Ajax();
	
	this.UI = {
		root: document.querySelector('.entries ul'),
		submit: document.querySelector('.data-entry button'),
		input: document.querySelector('.data-entry input')
	}

	/**
	 * Our entry point that will run on startup
	 */
	this.init = function() {
		this.addUIEvents();
		this.getItems();
	}

	/**
	 * Handles the ajax response display
	 */
	this.renderItems = function( todoItems ) {
		this.UI.root.innerHTML = ''; // todo: remove event listeners
		todoItems.forEach( this.createItem.bind(this) );
	}

	/**
	 * Generates a new todo item
	 * @param item: object
	 */
	this.createItem = function( todoEntry ) {
		var item = document.createElement('li');		
		var text = document.createElement('span');
		var actionWrapper = document.createElement('div');
		var iconTrash = document.createElement('i');
		var iconCheck = document.createElement('i');

		text.textContent = todoEntry.text;
		actionWrapper.className = "actions";
		iconTrash.className = 'trash ion-ios-trash-outline';

		if( todoEntry.completed ) {
			iconCheck.className = 'check checked ion-checkmark-circled';
		} else {
			iconCheck.className = 'check ion-ios-circle-outline';
		}

		actionWrapper.appendChild(iconTrash);
		actionWrapper.appendChild(iconCheck);
		item.appendChild(text);
		item.appendChild(actionWrapper);

		this.UI.root.appendChild(item);
		this.addItemEvents(item, todoEntry);
	}


	/**
	 * Add events to the todo item
	 */
	this.addItemEvents = function( itemNode, todoEntry ) {
		var pass = this;

		itemNode.querySelector('.trash').addEventListener('click', function(){
			pass.deleteItem( todoEntry.id, function(){
				this.parentNode.parentNode.remove();
			}.bind(this));
		});

		itemNode.querySelector('.check').addEventListener('click', function(){
			this.classList.toggle('ion-checkmark-circled');
			this.classList.toggle('ion-ios-circle-outline');
			this.classList.toggle('checked');

			todoEntry.completed = this.classList.contains('checked');
			pass.checkItem( todoEntry );
		});
	}


	/**
	 * Adds events to the input field and the button
	 */
	this.addUIEvents = function() {
		this.UI.submit.addEventListener('click', this.submitItem.bind(this));

		this.UI.input.addEventListener('keyup', function(e){
			if( e.keyCode === 13 ) {
				this.submitItem(this.UI.input.value)
				this.UI.input.value = '';
			}
		}.bind(this));
	}

	/**
	 * AJAX Communications dispatchers
	 * ---
	 * Todo: move them somewhere else
	 */
	this.getItems = function() {
		this.ajax.list( this.renderItems.bind(this) );
	}

	/**
	 * Push data to server
	 */
	this.submitItem = function( inputText ) {
		this.ajax.post({
			text: inputText
		}, this.getItems.bind(this) );
	}

	/**
	 * Update item state
	 */
	this.checkItem = function( itemData ) {
		this.ajax.update( itemData, itemData.id, function( rsp ){
			console.log(rsp);
		});
	}

	/**
	 * Delete item
	 */
	this.deleteItem = function( id, callback ) {
		this.ajax.del( id, callback );
	}
	
	// START THE APP AUTOMATICALLY
	this.init();
}

var Todo = new App(); 
