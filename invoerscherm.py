from tkinter import *
from config import CSV_PATH
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

        self.csv_dict = self.readFile()

    def create_GUI(self):
        Label(mainWindow, text="Bericht", width="10").grid(row=0, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=0, column=1)

        self.button = Button(mainWindow, text="Verzenden", command=self.onPressVerzenden, width="20")
        self.button.grid(row=1, column=0, columnspan=2)


    def onPressVerzenden(self):

        message = self.message.get()

        if len(message)<=140:
        
        else:
            print("FOUT")


    def writeFile(self,d):

        return

    def readFile(self):
        with open(CSV_PATH, 'r') as f:
            reader = csv.reader(f)
            d = dict(reader)

        return d

mainWindow = Tk()
mainWindow.title("Invoer scherm")
mainWindow.geometry("450x450")
app = MainMenu(mainWindow)
mainWindow.mainloop()