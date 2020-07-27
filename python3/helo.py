from tkinter import *
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

cv.create_rectangle(150, 150, 250, 250, fill="red")
cv.create_rectangle(320, 270, 370, 320, fill="green")

cv.create_line(10, 90, 580, 90, fill="blue", width=5)
cv.create_line(90, 10, 90, 380, fill="blue", width=5)
win.mainloop()
