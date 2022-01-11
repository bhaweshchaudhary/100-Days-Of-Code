import tkinter, turtle

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=800)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "I am"


# Button
def button_clicked():
    new_text = mero_input.get()
    my_label["text"] = new_text


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

mero_input = tkinter.Entry(width=10)
mero_input.pack()
print(mero_input.get())

window.mainloop()
