from tkinter import *
import twitter

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.twitter = twitter.Twitter()

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        self.label = Label(mainWindow, text="Bericht", width="10")
        self.label.grid(row=0, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=0, column=1)

        tweets = self.twitter.getFeed()

        for tweet in tweets:
            print(tweet['text'])


mainWindow = Tk()
mainWindow.title("Invoer scherm")
mainWindow.geometry("450x450")
app = MainMenu(mainWindow)
mainWindow.mainloop()