import tkinter as tk

window = tk.Tk()
window.title('Win, lose or draw?')
canvas1 = tk.Canvas(window, bg='black', width=300, height=300)

line1 = canvas1.create_line(50, 50, 250, 250, fill='white')
oval1 = canvas1.create_oval(50, 100, 100, 250, fill='green')
oval2 = canvas1.create_oval(225, 50, 275, 100, fill='red')
polygon1 = canvas1.create_polygon(150, 250, 250, 250, 300, 275, 250, 300, 150, 300, fill='orange')
filename = tk.PhotoImage(file='img/sum.png')
image1 = canvas1.create_image(300, 100, anchor=tk.NE, image=filename)
rectangle1 = canvas1.create_rectangle(100, 25, 200, 75, fill='pink', outline='red', width=2)
text1 = canvas1.create_text(25, 280, anchor=tk.SW, font='Calibri', text='Hi students!', fill='yellow')
canvas1.pack()
button1 = tk.Button(window, text='Quit', command=window.destroy)
button1.pack()
window.mainloop()