# Create a class the displays the Elevator art and navigation (list of commands)

# Building top
# draw floor, draw nth floor with elevator w/wo passengers
# Building bottom

import gfx

class Display:

    def displayElevator(self, shaftlevels, elevatorlevel, passengers):
        print(gfx.building_top)

        for i in range(shaftlevels, -1, -1):
            if i == 0: # ground floor
                # elevator on floor?
                if elevatorlevel == i:
                    if passengers > 0:
                        print(gfx.shaft_gfloor_wcabin_wpassenger)
                    else:
                        print(gfx.shaft_gfloor_wcabin_opassenger)
                else:
                    print(gfx.shaft_gfloor_ocabin)
            elif i > 0: # not ground floor
                # elevetor on floor?
                if elevatorlevel == i:
                    if passengers > 0:
                        print(gfx.shaft_wcabin_wpassenger)
                    else:
                        print(gfx.shaft_wcabin_opassenger)
                else:
                    print(gfx.shaft_ocabin)

        print(gfx.building_bottom)

    def displayConsole(self):
        print("")
        print("****** [ Commands: ] *******")
        print("*  [i] Passenger get i     *")
        print("*  [o] Passenger get out   *")
        print("*  [u] Move elevator up    *")
        print("*  [d] Move elevator down  *")
        print("****************************")
