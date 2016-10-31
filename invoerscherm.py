from tkinter import *
import twitter

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.twitter = twitter.Twitter()

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        Label(mainWindow, text="Message", width="10").grid(row=0, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=0, column=1)

        self.button = Button(mainWindow, text="Verzenden", command=self.onPressTweet, width="20")
        self.button.grid(row=2, column=0, columnspan=2)

        self.listbox = Listbox(mainWindow, width=100, height=22)
        self.listbox.grid(row=4, column=0, columnspan=8)

        self.updateListbox()

    def updateListbox(self):
        self.listbox.delete(0, END)

        tweets = self.twitter.getFeed()

        for tweet in tweets:
            self.listbox.insert(END, tweet['text'])

    def onPressTweet(self):

        self.twitter.postTweet(self.message.get())

        self.message.delete(0, END)

        self.updateListbox()


mainWindow = Tk()
mainWindow.title("Invoer scherm")
mainWindow.geometry("450x450")
app = MainMenu(mainWindow)
mainWindow.mainloop()