import tkinter as tk  # using Python 3
size = 600

m = tk.Tk()
canvas = tk.Canvas(m, width=size, height=size)
canvas.pack()

def thing(event):
	print('Da event iz', event)

m.bind('<q>', thing) # Listens to Q key

m.mainloop()
