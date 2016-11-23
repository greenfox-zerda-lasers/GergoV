import tkinter as tk
root = tk.Tk()

floor_image = tk.PhotoImage(file = "../img/floor.gif")
floor = tk.Label(image = floor_image)
#floor.grid(row=0, column=0)
floor.place(0, 0)

hero_image = tk.PhotoImage(file = "../img/hero-down.gif")
hero = tk.Label(image = hero_image)
#hero.grid(row=0, column=0)
hero.place(0, 0)

root.mainloop()
