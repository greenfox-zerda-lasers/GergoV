'use strict';


var button = document.querySelector('button');
function turnPartyOn () {
  document.body.setAttribute('class', 'party');
};
function turnPartyOff () {
  document.body.removeAttribute('class', 'party');
};
function toggleParty () {
  if (document.body.hasAttribute('class', 'party')) {
    turnPartyOff();
  } else {
    turnPartyOn();
  };
};
button.addEventListener('click', toggleParty);
