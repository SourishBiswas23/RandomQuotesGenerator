from tkinter import messagebox
import requests


def generate_quote():

    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
    except Exception as error:
        messagebox.showinfo(title="Oops", message=error)
    else:
        quote = response.json()[0]["q"]
        author = response.json()[0]["a"]
        spaces = "    "
        for _ in quote:
            spaces += " "
        return f'{response.json()[0]["q"]}\n\n{spaces}-{author}'
