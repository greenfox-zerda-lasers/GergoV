// Bookstore Queries

var mysql = require('mysql');
var fs = require('fs');

var detailedRequest = fs.readFileSync('./bookstorequeries.sql').toString();

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'm2st3r',
  database: 'bookstore'
});

con.connect(function(err){
  if(err){
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

// List all book titles from table:
/*
con.query('SELECT book_name from book_mast', function(err, res) {
  if (err) throw err;

  for (var i = 0; i < res.length; i++) {
  console.log(res[i].book_name);
};
});
*/

// List all books with its name, authors name, category name, publishers name and price:

con.query(detailedRequest, function(err, res) {
  if (err) throw err;

  for (var i = 0; i < res.length; i++) {
    console.log('Title: ', res[i].book_name, ' Category: ', res[i].cate_descrip, ' Author: ', res[i].aut_name, ' Publisher: ', res[i].pub_name, ' Price: ', res[i].book_price);
  }
});


con.end(function(err){
  // term.
});
