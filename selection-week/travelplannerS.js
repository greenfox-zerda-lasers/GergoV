// Travel planner for Emarsys - main logic
'use strict';

// wishList: ['PlacName1', 'PlaceName2'...]; dependencies: {'PlaceName':'VisitBeforeThis'}
const sampleTrip = ['Milan', 'Budapest', 'Berlin', 'Munich', 'Rome', 'Prague', 'Vienna', 'Krakow', 'Madrid'];
const visitBefore = {'Rome': 'Milan', 'Milan': 'Vienna', 'Munich': 'Vienna', 'Prague': 'Budapest'};

makeTravelPlan(visitBefore, sampleTrip);

function makeTravelPlan(dependencies, wishList) {
  let travelPlan = {};

  // Examine wishList elements.
  wishList.forEach( function(e, i) {

    // Increase item index so that they can be conveniently manipulated.
    let itemIndex = i * wishList.length;
    console.log("Item: " + e + " TempIndex: " + itemIndex);

    // Does item have dependency?
    if (dependencies[e]) {
      let currentDependency = dependencies[e];
      console.log("Best before: " + currentDependency);

      // Is dependency on the wish list?
      if (wishList.indexOf(dependencies[e]) != -1) {

        // Is dependency already on the travelPlan?
        if (travelPlan[currentDependency]) {
          let dependencyIndex = travelPlan[currentDependency];
          // Assure item comes before dependency and put it there.
          itemIndex = dependencyIndex - 1;
          travelPlan[e] = itemIndex;
        } else { // dependency not yet on travelPlan:

          // Put dependency on the travelplan + put item on the travelplan with lower index
          travelPlan[currentDependency] = itemIndex + 1;
          travelPlan[e] = itemIndex;
          console.log(currentDependency + " wasn't on plan, added.");
        }
      }

    } else {

      // Destination has no dependency OR it is not on the wish list
      // Add destination to travelPlan
      travelPlan[e] = itemIndex;
    }

    console.log(travelPlan);
  });

  console.log('Final: ', travelPlan);
};
