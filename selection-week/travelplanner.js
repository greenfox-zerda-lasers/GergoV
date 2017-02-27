// Travel planner for Emarsys
'use strict';

function TravelPlan() {
  this.dependencies = {};
  this.wishList = [];
  this.travelPlan = {};

  this.getDependencies = function (dependencies) {
    // Enter dependencies in object with values:
    // {'PlaceName':'DependencyName', ...}
    // NOTE:
    // 1. Both values must be of type text.
    // 2. Values can't be the same.
    this.dependencies = dependencies;
  };

  this.getWishList = function(wishlist) {
    // Enter travel destinations in array.
    this.wishList = wishlist;
  };

  this.makeTravelPlan = function(dependencies, wishList) {
    // Examine wishList elements.
    wishList.forEach(function(e, i) {
      // Increase item index so that they can be conveniently manipulated.
      let itemIndex = i * wishList.length;
      // Does item have dependency?
      if (dependencies.e) {
        let currentDependency = dependencies.e;
        // Is dependency already on the list?
        if (this.travelPlan.currentDependency) {
          let dependencyIndex = this.travelPlan.currentDependency;
          // Assure item comes before dependency.
          itemIndex = dependencyIndex - 1;
          this.travelPlan.e = itemIndex;
        } else {
          // Put dependency on the list + put item on the list with lower index
          this.travelPlan.currentDependency = itemIndex + 1;
          this.travelPlan.e = itemIndex;
        }
      } else {
        // Item has no dependency
        this.travelPlan.e = itemIndex;
      }
    });

    console.log(this.travelPlan);
  };

};
