from tkinter import *
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        Label(mainWindow, text="Message", width="10").grid(row=0, column=0)


def TweetOntvangen():

    while True:
        with open("/data/tweet.csv", "r") as MyCsvFile:
            reader = csv.reader(MyCsvFile)
            d = dict(reader)
            print(d)



mainWindow = Tk()
mainWindow.title("Accepteer Tweet")
mainWindow.geometry("600x350")
MainMenu(mainWindow)
mainWindow.mainloop()