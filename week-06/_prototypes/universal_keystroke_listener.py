import tkinter as tk  # using Python 3
size = 200

m = tk.Tk()
canvas = tk.Canvas(m, width=size, height=size, bg='tomato')
canvas.pack()

def key_press_listener(event):
	print('Key pressed is', event.keysym)
	# call model funcion with event.keysym

m.bind('<Key>', key_press_listener) # Listens to Q key

m.mainloop()
