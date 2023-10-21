from tkinter import *
from tkinter.ttk import *
import winsound


food = 10
sound = 10

def hunger():
    global food
    food -= 1
    progress1.config(value=food)
    if food < 7:
        image_label.config(image=fox)
    progress1.config(value=food)
    if food < 0:
        food = 0
    window.after(1000, hunger)

def eat():
    global food
    food += 1
    if food >= 7:
        image_label.config(image=foxsleep)
    progress1.config(value=food)


def music():
    global sound
    sound -= 1
    progress2.config(value=sound)
    window.after(1000, music)

def nomusic():
    global sound
    sound += 1
    if sound >= 7:
        winsound.PlaySound("minecraftsound.wav", winsound.SND_ASYNC)
    progress2.config(value=sound)

window = Tk()
window.title("Тамагочи!")
fox = PhotoImage(file='fox2.PNG')
foxsleep = PhotoImage(file='fox1.PNG')
image_label = Label(window, image=foxsleep)
image_label.pack()
progress1 = Progressbar(window, value=food, maximum=10)
progress1.pack()
button1 = Button(window, text="Покормить", width=10, command=eat)
button1.pack()
progress2 = Progressbar(window, value=sound, maximum=10)
progress2.pack()
button2 = Button(window, text="Включить музыку", width=20, command=music)
button2.pack()


window.after(1000, hunger)

mainloop()
