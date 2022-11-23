import tkinter as tk
import random as rnd

width = 600
height = 600
refresh_time = 10
speed_x = rnd.randint(3, 10)
speed_y = rnd.randint(3, 10)
animate = False

window = tk.Tk()
window.title("Animation")
canvas1 = tk.Canvas(window, bg="black", width=width, height=height)
ball = canvas1.create_oval(100, 100, 150, 150, fill='red')
canvas1.pack()
button1 = tk.Button(window, text='Quit', command=window.destroy)
button1.pack()


def move_ball():
    if animate:
        global speed_x, speed_y
        if canvas1.coords(ball)[2] > width or canvas1.coords(ball)[0] < 0:
            speed_x = - speed_x
        if canvas1.coords(ball)[3] > height or canvas1.coords(ball)[1] < 0:
            speed_y = - speed_y
        canvas1.move(ball, speed_x, speed_y)
        canvas1.after(refresh_time, move_ball)


def start_stop():
    global animate
    if animate:
        animate = False
    else:
        animate = True
        move_ball()


button2 = tk.Button(window, text="Start/Stop", command=start_stop)
button2.pack()
window.mainloop()