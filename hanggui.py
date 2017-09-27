from tkinter import Tk, Label, Button, StringVar, Entry, PhotoImage


class Screen:
    def __init__(self, master, photo):
        self.hasSecret = False
        self.master = master
        master.title("A simple GUI")

        #Label for the hangman image
        self.words = Label(master, image=photo, width=400, height=200, borderwidth=3)
        self.words.pack()
        #Label for the hangman output
        self.prompt = Label(master, text="Welcome to Hangman enter a word")
        self.prompt.pack()
        #Input box for user
        self.text_box = Entry(master,  show="*")
        self.text_box.pack()
        #Submits to program
        self.enter_button = Button(master, text="Enter", command=self.callback)
        self.enter_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def get_char(self):
        char = self.text_box.get()[0]
        return char

    def callback(self):
        if(self.hasSecret):
            self.get_char()
        else:
            self.get_secret_word()
            self.prompt.config(text='Please enter a character')
        self.clear_screen()

    def get_secret_word(self):
        word = self.text_box.get()
        self.text_box.config(show="")
        pri1nt(word)

        return word

    def clear_screen(self):
        self.text_box.delete(0, 'end')


root = Tk()
image = PhotoImage(file="recs/hangman.gif")
hangman = Screen(root, image)
root.mainloop()
