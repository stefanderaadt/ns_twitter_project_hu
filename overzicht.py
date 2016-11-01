from tkinter import *
import twitter

xbox = 600
ybox = 700

class MainMenu(Frame):
    # Init wordt standaard opgestart bij het aanroepen van deze class
    def __init__(self, master):

        # Code van tkinter om het scherm te laten werken
        super(MainMenu, self).__init__(master)

        # self is de eigen istance van deze class waar op dit moment mee wordt gewerkt
        # Hierdoor zijn de variabelen en definitions makkelijk te bereiken binnen de class

        # Maak een twitter variabel aan die vast zit aan het mainmenu object met self
        self.twitter = twitter.Twitter()

        # Maak een grid aan op het scherm zodat we makkelijk de posities van bijvoorbeeld labels kunnen instellen
        # uitleg: http://effbot.org/tkinterbook/grid.htm
        self.grid()

        # Roep de definition create_GUI() hieronder aan om de GUI op te starten
        self.create_GUI()

    # Alle definitions binnen een python class hebben als eerste variabel het eigen object/instance (self).
    # dit gebeurt vanzelf en hoef je verder niets voor te doen.
    def create_GUI(self):
        self.listbox = Listbox(mainWindow, width=xbox, height=ybox , font=("Georgia", 16))
        self.listbox.grid(row=4, column=0, columnspan=8)

        self.updateListbox()

    def updateListbox(self):
        self.listbox.delete(0, END)

        tweets = self.twitter.getFeed()

        p = 0
        for tweet in tweets:

            self.listbox.insert(END, tweet['text'])
            self.listbox.insert(END, tweet['created_at'])

            p += 1


# Begin programma

# Maak een nieuw scherm aan via TKinter(imp
mainWindow = Tk()

# Zet de titel van het scherm
mainWindow.title("Tweets")

# Zet de grote van het scherm
mainWindow.geometry("600x700")

# Maak een object aan van de class MainMenu(Frame) hierboven en geef het scherm mainWindow mee
# Dit start alle code in class MainMenu
app = MainMenu(mainWindow)

# Start de mainloop als het scherm is aangemaakt in de MainMenu class
mainWindow.mainloop()