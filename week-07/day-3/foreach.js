var myNiceArray = ['Jock', 'Jr', 'Ray', 'Samantha', 'Bobby', 'Pamela'];

myNiceArray.forEach(function(e, f) {
  console.log(e, f);
});

var out = myNiceArray.map(function(a) {
  return a;
});
console.log(out)
