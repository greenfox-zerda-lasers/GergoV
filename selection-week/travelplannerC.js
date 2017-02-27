// Travel planner main logic

'use strict';

const input = [
  'u',
  'v',
  'w',
  'x',
  'y',
  'z',
];

const ruleset = {
  v: 'w',
  w: 'z',
  x: 'u',
  y: 'v',
};

const out = [];

input.forEach(function (e) {

  let eCheck = out.indexOf(e);
  let vCheck = out.indexOf(ruleset[e]);
  let ruleCheck = ruleset[e];

  if (!ruleCheck && eCheck === -1) { // No rule, element not present: Add element
    out.push(e);
  }
  if (ruleCheck) { // Rule present
    if (eCheck === -1 && vCheck === -1) {
    // element not present, value not present: add both
      out.push(ruleset[e]);
      out.push(e);
    } else if (eCheck !== -1 && vCheck === -1) {
    // element present, value not present: add value before element
      out.splice(eCheck, 0, ruleset[e]);
    } else {
    // element not present, value present: add element after value
      out.splice(vCheck + 1, 0, e);
    }
  }
  console.log(out);
});

console.log(out);
