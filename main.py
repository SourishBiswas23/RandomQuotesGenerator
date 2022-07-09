import tkinter
import quotes

FONT = ("FantasqueSansMono Nerd Font", 15, "normal")


def new_quote(*args):
    my_button.config(state="disabled")
    quote = quotes.generate_quote()
    my_label.config(text=quote)
    my_button.config(state="active")


window = tkinter.Tk()
frame = tkinter.Frame(window)
my_label = tkinter.Label(frame)
my_button = tkinter.Button(frame)

window.title("Quotes")
frame.config(padx=50, pady=50)
my_label.config(font=FONT)
my_button.config(text="New Quote", command=new_quote, font=FONT)

frame.grid(row=0, column=0)
my_label.grid(row=1, column=1)
my_button.grid(row=2, column=1)


for widgets in frame.winfo_children():
    widgets.grid_configure(padx=5, pady=5)

window.bind("<Return>", new_quote)
window.mainloop()
