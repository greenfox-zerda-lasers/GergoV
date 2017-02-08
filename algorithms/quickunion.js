// Basic implementation based on JAVA example

'use strict';

function QuickUnion (arrayLength) {
  this.array = Array(arrayLength);

  for (var i=0; i < this.array.length; i++) {
      this.array[i] = i;
    }

  this.root = function(e) {
    while (e != this.array[e]) {
      e = this.array[e];
      return e;
    }
  };

  this.connected = function (p, q) {
    return this.root(p) == this.root(q);
  };

  this.union = function (p, q) {
    var pid = this.root(p);
    var qid = this.root(q);
    for (i=0; i<this.array.length; i++) {
      if (this.array[i] == pid) {
        this.array[i] = qid;
      }
    }
  }

  this.getGroups = function () {

    // [{root, [node1, .. noden]}, ]
  };
};

var u = new QuickUnion(5);
console.log(u);
u.union(0, 1);
u.union(5, 2);
u.union(2, 3);
