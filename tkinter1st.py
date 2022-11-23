import tkinter as tk

window = tk.Tk()
window.title('My first window')
text1 = tk.Label(window, text='Computer Science is amazing', fg='black')
text1.pack()
button1 = tk.Button(window, text='Quit', command=window.destroy)
button1.pack()
window.mainloop()