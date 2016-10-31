from tkinter import *
import twitter

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

        # Maak een label variabel aan die vast zit aan het mainmenu object
        # Alle parameters en uitleg voor bijvoorbeeld het label staan hier: https://www.tutorialspoint.com/python/python_gui_programming.htm
        self.label = Label(mainWindow, text="Bericht", width="10")

        # Instellen op welke positie van het scherm het label komt te staan.
        self.label.grid(row=0, column=0)

        self.message = Entry(mainWindow, width="40")
        self.message.grid(row=0, column=1)

        # Tweets ophalen via twitter API in een dictionary (tweets)
        tweets = self.twitter.getFeed()

        # Tweets uit het dictionary lezen en hier de text van uitprinten per tweet
        for tweet in tweets:
            print(tweet['text'])


# Begin programma

# Maak een nieuw scherm aan via TKinter(import)
mainWindow = Tk()

# Zet de titel van het scherm
mainWindow.title("Invoer scherm")

# Zet de grote van het scherm
mainWindow.geometry("450x450")

# Maak een object aan van de class MainMenu(Frame) hierboven en geef het scherm mainWindow mee
# Dit start alle code in class MainMenu
app = MainMenu(mainWindow)

# Start de mainloop als het scherm is aangemaakt in de MainMenu class
mainWindow.mainloop()