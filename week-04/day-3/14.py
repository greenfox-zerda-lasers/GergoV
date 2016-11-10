# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

# create a 300x300 canvas.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300")
canvas.pack()

start = 40
padding = 0

for i in range(start, 320, 20):
    canvas.create_line(i + padding, 0 + padding, 300 - padding, i-start/2 - padding, fill="green")
    canvas.create_line(0 + padding, i + padding, i-start/2 - padding, 300 - padding, fill="purple")

root.mainloop()
