import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=800)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

window.mainloop()
