from tkinter import *
import twitter
from datetime import datetime
from config import *


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

        self.timer()

    # Alle definitions binnen een python class hebben als eerste variabel het eigen object/instance (self).
    # dit gebeurt vanzelf en hoef je verder niets voor te doen.
    def create_GUI(self):

        self.listbox = Listbox(mainWindow, width=0, height=0 , font=("Georgia", 16))
        self.listbox.grid(row=0, column=1)

        self.updateListbox()

    def updateListbox(self):

        self.img = PhotoImage(file=IMG_PATH + 'ns-logo.png')
        self.img = self.img.subsample(2, 2)

        tweets = self.twitter.getFeed()
        p = 0
        for tweet in tweets:
            nowtijd = datetime.now()
            tijd = datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')

            tuur = tijd.hour
            ntuur = nowtijd.hour
            verschil = ntuur - tuur

            if verschil > 0 and verschil <= 1:
                #self.button = Button(mainWindow, text="Please let it work", width="40")
                #self.button.grid(row=p, column=0)
                self.can = Canvas(mainWindow, bg='#66ccFF', height="156", width="200")
                self.can.grid(row=p, column=0)


                self.can.create_image(95, 80, image=self.img)

                self.listbox = Listbox(mainWindow, width=600, height=4, font=("Comic Sans MS", 20), bg = "#1c1c6b", fg = 'white')
                self.listbox.grid(row=p, column=1)
                # if len(tweet['text']) > 80:
                #     self.listbox.insert(END, "ns_test tweeted:  \n" + tweet['text'], )
                #     self.listbox.insert(END, tweet['created_at'])
                # else:
                self.listbox.insert(END, "ns_test tweeted:  \n" + tweet['text'])
                self.listbox.insert(END, "tweeted on: " + str(tijd.day) + '-' + str(tijd.month) + " // " + str(tijd.hour)+":"+str(tijd.minute))
                p += 1



    def timer(self):
        self.updateListbox()
        self.after(60000, self.timer)


# Begin programma

# Maak een nieuw scherm aan via TKinter(imp
mainWindow = Tk()

# Zet de titel van het scherm
mainWindow.title("Tweets")

# Zet de grote van het scherm

mainWindow.attributes('-fullscreen', True)
mainWindow.configure(background='#fcc917')

# Maak een object aan van de class MainMenu(Frame) hierboven en geef het scherm mainWindow mee
# Dit start alle code in class MainMenu
app = MainMenu(mainWindow)
mainWindow.iconbitmap(IMG_PATH+"Ns.ico")

# Start de mainloop als het scherm is aangemaakt in de MainMenu class
mainWindow.mainloop()

#goddamnit JEffreyyyy