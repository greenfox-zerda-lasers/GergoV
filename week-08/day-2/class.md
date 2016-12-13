## Blocking

A nem aszinkron feladat blokkolja a böngészőt.
pl. file loop, etc.

'Blocking code'

Pl. script importálása: amíg le nem fut, addig minden áll.
Careful with 3rd party scripts.

## RequestAnimationLoop

A böngésző szól a kódnak, h mikor tud rajzolni.
Nem a frissítéseket nyomja át a kód ha kell, ha nem.

## Using setInterval or setTimeout

You should pass a reference to a function as the first argument for setTimeout or setInterval. This reference may be in the form of:

  An anonymous function
  setTimeout(function(){/* Look mah! No name! */},2000);

  A name of an existing function
  function foo(){...}

  setTimeout(foo, 2000);

  A variable that points to an existing function

  var foo = function(){...};
  setTimeout(foo, 2000);

## DOM load miújság

`document.addEventListener('DOMContentLoaded', fn )`
`window.addEventListener('load', fn )`
