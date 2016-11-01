from tkinter import *
from config import CSV_PATH, IMG_PATH
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        Label(mainWindow, text="Bericht", width="10").grid(row=1, column=0)
        Label(mainWindow, text="Naam", width="10").grid(row=2, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=1, column=1)
        self.naam = Entry(mainWindow, width="40")
        self.naam.grid(row=2, column=1)

        self.button = Button(mainWindow, text="Verzenden", command=self.onPressVerzenden, width="20")
        self.button.grid(row=3, column=0, columnspan=2)


    def onPressVerzenden(self):

        message = self.message.get()
        naam = self.naam.get()

        if len(message)<=140:
            self.writeFile([message,naam])
        else:
            print("FOUT")


    def writeFile(self, r):
        with open(CSV_PATH, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(r)

        return


mainWindow = Tk()
mainWindow.title("Invoer scherm")
# mainWindow.geometry("450x450")
mainWindow.attributes('-fullscreen', True)
app = MainMenu(mainWindow)
mainWindow.mainloop()