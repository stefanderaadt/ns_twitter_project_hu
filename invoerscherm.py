from tkinter import *
from tkinter import messagebox
import pygame
import random
from config import CSV_PATH, SOUND_PATH
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()
        self.timer()

    def create_GUI(self):
        #self.can = Canvas(mainWindow, bg='red', height=mainWindow.winfo_screenheight(), width=mainWindow.winfo_screenwidth())
        #self.can.place(relx=0.5, rely=0.5, anchor=CENTER)

        Label(mainWindow, text="Bericht", width="10").grid(row=1, column=0)
        Label(mainWindow, text="Naam", width="10").grid(row=2, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=1, column=1)
        self.naam = Entry(mainWindow, width="40")
        self.naam.grid(row=2, column=1)

        self.button = Button(mainWindow, text="Verzenden", command=self.onPressVerzenden, width="20")
        self.button.grid(row=3, column=0, columnspan=2)


    def onPressVerzenden(self):

        error = ""

        message = self.message.get()
        naam = self.naam.get()

        message.strip()
        naam.strip()

        if message == "" or naam == "":
            error += "Naam of bericht is leeg!\n"

        if len(message) > 140:
            error += "Lengte van tweet is te lang!\n"

        if error=="":
            self.writeFile([message,naam])
            self.naam.delete(0, 'end')
            self.message.delete(0, 'end')
            pygame.mixer.init()
            pygame.mixer.music.load(SOUND_PATH+"ns.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.init()
            pygame.mixer.music.load(SOUND_PATH+"xp.mp3")
            pygame.mixer.music.play()
            messagebox.showinfo("Fout!", error)



    def writeFile(self, r):
        with open(CSV_PATH, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(r)

        return

    def timer(self):
        mainWindow.configure(background='#%02x%02x%02x' % (random.randrange(255), random.randrange(255), random.randrange(255)))
        self.after(60000, self.timer)


mainWindow = Tk()
mainWindow.title("Invoer scherm")
mainWindow.geometry("450x450")
#mainWindow.attributes('-fullscreen', True)
app = MainMenu(mainWindow)
mainWindow.mainloop()