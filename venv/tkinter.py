from tkinter import *

window = Tk()
window.title('Pizza Menu')
window.geometry("500x500")
window.configure(bg='Turquoise')


frame1 = Frame(window) #Create frame within Window
frame2 = Frame(window) #Create frame within Window
frame3 = Frame(window) #Create frame within Window
frame4 = Frame(window)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()





def selection():
    selection = prebuilt.curselection()
    if selection[0] == 0:
        message.set("Unknown")
    elif selection[0] == 1:
        message.set("Bacon, sauce mix, avocado")
    elif selection[0] == 2:
        message.set("Cheese, Bacon, Sauce mix")
    elif selection[0] == 3:
        message.set("Nuts, extra cheese, Bacon, ham")

message = StringVar()
message.set("No selection")


pizza_info = Label(frame1, text="Pre-built pizza")
pizza_info.pack(side=LEFT)

prebuilt = Listbox(frame1)
prebuilt.insert(1, '1. Hawaiian')
prebuilt.insert(2, '2. Four Seasons')
prebuilt.insert(3, '3. Regina')
prebuilt.pack(side=LEFT, padx=5)

lbl_selected = Label(frame1, textvariable=message)

btn = Button(window, text="Select", command=selection)
btn.pack(side=TOP)


window.mainloop()


