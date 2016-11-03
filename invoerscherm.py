from tkinter import *
from tkinter import messagebox
import pygame
from config import CSV_PATH, SOUND_PATH, IMG_PATH, FONT
import csv
import datetime

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    # Maak de GUI aan
    def create_GUI(self):
        self.can = Canvas(mainWindow, bg='#1c1c6b', height=mainWindow.winfo_screenheight(), width=mainWindow.winfo_screenwidth())
        self.can.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.img = PhotoImage(file=IMG_PATH+'ns_logo.png')
        self.img = self.img.subsample(2, 2)

        self.can.create_image(960, 200, image=self.img)# 540, image=self.img)

        self.displayMessage = Label(mainWindow, text="Tweet: ", bg='#1c1c6b', fg="#ffffff", width="140", font=(FONT, 14))
        self.displayMessage.place(relx=0.5, rely=0.38, anchor=CENTER)
        Label(mainWindow, text="Naam", bg='#1c1c6b', fg="#ffffff", width="5", font=(FONT, 14)).place(relx=0.32, rely=0.41, anchor=CENTER)
        Label(mainWindow, text="Tweet", bg='#1c1c6b', fg="#ffffff", width="5", font=(FONT, 14)).place(relx=0.32, rely=0.5, anchor=CENTER)
        self.characters = Label(mainWindow, anchor='w', text="0/140", bg='#1c1c6b', fg="#ffffff", width="20", font=(FONT, 14))
        self.characters.place(relx=0.4, rely=0.59, anchor=CENTER)

        self.naam = Entry(mainWindow, width="50", font=(FONT, 14))
        self.naam.place(relx=0.50, rely=0.41, anchor=CENTER)
        self.naam.bind("<KeyRelease>", self.onKeyRelease)

        self.message = Text(mainWindow, width="50", height="5", font=(FONT, 14))
        self.message.place(relx=0.50, rely=0.5, anchor=CENTER)
        self.message.bind('<Return>', 'break')
        self.message.bind("<KeyRelease>", self.onKeyRelease)

        self.button = Button(mainWindow, text="Verzenden", command=self.onPressVerzenden, width="20", cursor="hand2", font=(FONT, 14))
        self.button.place(relx=0.598, rely=0.59, anchor=CENTER)

    # Key release event om de aantal characters te tellen
    def onKeyRelease(self,o):
        message = self.message.get("1.0", END)
        naam = self.naam.get()

        message = message.strip()
        message = message.replace("\n","")
        naam = naam.strip()

        self.characters['text'] = str(len(naam) + len(": ") + len(message))+"/140"
        self.displayMessage['text'] = "Tweet: "+ naam+": "+message

    # Event voor het verzenden van de tweet naar het accepteer scherm
    def onPressVerzenden(self):

        error = ""

        message = self.message.get("1.0", END)
        naam = self.naam.get()
        tijd = datetime.datetime.now().strftime("%H:%M:%S op %d-%m-%Y")

        message = message.strip()
        message = message.replace("\n","")
        naam = naam.strip()

        if message == "" or naam == "":
            error += "Naam of bericht is leeg!\n"

        if (len(naam) + len(": ") + len(message)) > 140:
            error += "Lengte van tweet is te lang!\n"

        if error=="":
            self.writeFile([message,naam,tijd])
            self.naam.delete(0, 'end')
            self.message.delete('1.0', END)
            self.characters['text']="0/140"
            self.displayMessage['text'] = "Tweet: "
            pygame.mixer.init()
            pygame.mixer.music.load(SOUND_PATH+"ns.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.init()
            pygame.mixer.music.load(SOUND_PATH+"xp.mp3")
            pygame.mixer.music.play()
            messagebox.showinfo("Fout!", error)


    # Functie om bestanden op te slaan
    def writeFile(self, r):
        with open(CSV_PATH, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(r)

        return

# Maak een nieuw TKinter scherm aan
mainWindow = Tk()

# Zet de titel van het scherm
mainWindow.title("Invoer scherm")

# Maak het scherm fulscreen
mainWindow.attributes('-fullscreen', True)

# Initialiseer het scherm
app = MainMenu(mainWindow)

# Zet de header icon naar een NS logo
mainWindow.iconbitmap(IMG_PATH+"Ns.ico")

# Start het scherm op
mainWindow.mainloop()