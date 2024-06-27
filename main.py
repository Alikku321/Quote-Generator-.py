import tkinter as tk
from tkinter import ttk
import pyquotegen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x300")
        self.title('Quote generation')

        # initialize data
        self.quote_category = [
            'motivational',
            'inspirational',
            'technology',
            'funny',
            'nature',
            'success',
            'attitude',
            'coding'
        ]

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Select your Category:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.quote_category[0],
            *self.quote_category,
            command=self.option_changed)
        
        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        #Output
        self.output_label = ttk.Label(self, foreground='black')
        self.output_label.grid(column=1, row=1, sticky=tk.W, **paddings)

    def option_changed(self, selected_category):
        quote = pyquotegen.get_quote(selected_category)
        self.output_label['text'] = f'Quote: {quote}'


if __name__ == "__main__":
    app = App()
    app.mainloop()