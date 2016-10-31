from tkinter import *

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        Label(mainWindow, text="Message", width="10").grid(row=0, column=0)

        self.button = Button(mainWindow, text="BUTTON", command=self.onPressTweet, width="20")
        self.button.grid(row=2, column=0, columnspan=2)

    def onPressTweet(self):



mainWindow = Tk()
mainWindow.title("Venster naam")
mainWindow.geometry("450x450")
MainMenu(mainWindow)
mainWindow.mainloop()
a