from tkinter import *
from weather_display import *
root = Tk()

frame = CustomFrame("Weather Display", row = 0, column= 0)
frame.make_widgets()

root.geometry("550x250")
root.mainloop()