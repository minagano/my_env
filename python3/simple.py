from tkinter import *

 # ウィンドウを作りCanvasを貼り付ける --- (*1)
win = Tk()
cv = Canvas(win, width = 600, height = 400)
cv.pack()

 # 長方形(矩形)を描画 --- (*2)
cv.create_rectangle(200, 170, 250, 250, fill="red")
cv.create_rectangle(320, 270, 370, 320, fill="green")
cv.create_rectangle(150, 150, 250, 250, fill="yellow")


 # 線を描画 --- (*3)
cv.create_line(10, 90, 580, 90, fill="blue", width=5)
cv.create_line(90, 10, 90, 380, fill="red", width=5)

win.mainloop()


