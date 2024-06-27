import pyquotegen
from tkinter import *

#quote = pyquotegen.get_quote()
#print(quote)
class App():
    def __init__(self):
        super().__init__()
        self.geometry("320x80")
        self.title("Quote generator")

        #Initialize data
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
        self.quote = StringVar(self)

        self.create_widgets()
    
    def create_widgets(self):
        #padding
        paddings = {'padx' : 5, 'paddy' : 5}

        #label
        label = Tk.Label(self, text = "Select quote category:")
        label.grid(column = 0, row = 0, sticky=W, **paddings)

        option_menu = OptionMenu(
            self,
            self.quote,
            self.quote_category[0],
            command=self.option_changed)
        
        option_menu.grid(column=1,row=0,sticky=W, **paddings)

        self.output_label = Tk.Label(self, foreground='black')
        self.output_label.grid(column=0,row=1, sticky=W, **paddings)

        def option_changed(self, *args):
            self.output_label['text'] = f'You have selected :{self.option_var.get()}'
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
        #quote_category = pyquotegen.get_quote()
        #print(quote_category)
