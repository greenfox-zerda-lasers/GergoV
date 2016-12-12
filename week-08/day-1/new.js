// About the new keyword
// FFF video #50
// https://youtu.be/Y3zzCY62NYc

// This is obsolete code. The class kw using this under the hood. 

function Person(saying) {
    this.saying = saying;
};

Person.prototype.talk = function() {
    console.log('I say:', this.saying);
};


// What new does: 7:47 
// RECREATED: 

function reconstNew(constructor) {
    // 1.: Create new object.
    var obj = {}; 
    // 2. Set the prototype
    Object.setPrototypeOf(obj, constructor.prototype); 
    // 3. Execute the constructor:
    // apply: Similar to bind, but immediately executes the function too.
    var argsArray = Array.prototype.slice.apply(arguments);
    constructor.apply(obj, argsArray.slice(1));
    // 4. Return the created object:
    return obj;
};

var crockford = reconstNew Person('SEMICOLONS!!');
crockford.talk();