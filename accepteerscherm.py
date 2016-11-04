import csv
import datetime
from tkinter import *
from tkinter import messagebox

import twitter
from config import *


class MainMenu(Frame):
    def __init__(self, master):
        # klaar zetten van variablen
        super(MainMenu, self).__init__(master)
        self.button = []
        self.list = self.TweetOntvangen()
        self.frame = Frame
        self.grid()
        self.create_GUI()
        self.create_overige_GUI()
        self.twitter = twitter.Twitter()
        self.timer()

    def create_GUI(self):
        # Aanmaken van bovenste balk met de info overhoeveel berichten je hebt
        screen_width = mainWindow.winfo_screenwidth()
        self.label1 = Label(mainWindow, text=self.MainMessage()[0], width=screen_width, height="1",
                            background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(mainWindow, text=self.MainMessage()[1], width=screen_width, height="2",
                            background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label2.grid(row=1, column=0, sticky=W)

    def create_overige_GUI(self):
        # aanmaken refresh, exit en ns button
        self.photo = PhotoImage(file=IMG_PATH + "ns_logoklein.png")

        self.nsimage = Button(mainWindow, command=self.Onpressns, image=self.photo, width="200", height="97")
        self.nsimage.place(relx=1, rely=1, anchor=SE)

        self.refreshb = Button(mainWindow, text="Refresh", width=15, height="2", command=self.ref1, bg="#1c1c6b",
                               fg='white')
        self.refreshb.place(relx=1, rely=0.112, anchor=E)

        self.exit = Button(mainWindow, text="Exit", width=15, height="2", command=self.quit, bg="#1c1c6b", fg='white')
        self.exit.place(relx=0.939, rely=0.112, anchor=E)

    def tweetButtons(self):
        # aanmaken van de button voor de tweet die je hbet onvangen.
        self.list = self.TweetOntvangen()

        for b in self.button:
            b.destroy()

        self.button = []

        for i in range(len(self.TweetOntvangen())):  # self.list[i][0]
            if i > 9:
                break
            self.button.append(Button(mainWindow, text=(
                self.list[i][0] + ". \nontvangen door: " + self.list[i][1] + " om " + self.list[i][2]),
                                      command=lambda i=i: self.Onpress(i), width=self.buttonWidth(self.list[i][0]),
                                      anchor=CENTER, height="2", bg='#1c1c6b', fg='#ffffff', font=(FONT, 15)))
            self.button[i].place(relx=0.5, rely=0.20 + (0.082 * i), anchor=CENTER)

    def TweetOntvangen(self):
        # Alle Tweets met daarbij de verzender en tijd van verzenden word uit een CSV-bestand naar een list geschreven
        with open(CSV_PATH, "r") as MyCsvFile:
            reader = csv.DictReader(MyCsvFile)
            OntvangenTweets = []
            for row in reader:
                OntvangenTweets.append([row['tweet'], row['plaatser'], row['tijd']])
        return OntvangenTweets

    def IsTweetOntvangen(self):
        # Kijken of er tweets zijn ontvangen en daar een variable voor returnen
        if len(self.TweetOntvangen()) != 0:
            Tweet = 1
        else:
            Tweet = 0
        return Tweet

    def MainMessage(self):
        # Kijken hoeveel berichten er zijn en dit in een volledige tekst terug sturen
        bericht = ""
        bericht1 = ''
        if self.IsTweetOntvangen() == 0:
            bericht = 'U heeft geen bericht ontvangen.'
        if self.IsTweetOntvangen() == 1:
            if len(self.TweetOntvangen()[0]) > 1:
                bericht = "U heeft " + str(len(self.TweetOntvangen())) + " berichten"
                bericht1 = "Dit zijn de berichten:"
            else:
                bericht = "U heeft een bericht."
                bericht1 = "Dit is uw bericht:"
        return bericht, bericht1

    def ref1(self):
        # refreshen van de widgets
        self.tweetButtons()
        self.KleurTweet()
        self.create_GUI()

    def timer(self):
        # automatisch refreshen van widgets elke 15seconden
        self.tweetButtons()
        self.KleurTweet()
        self.create_GUI()
        self.after(15000, self.timer)

    def Onpressns(self):
        # message box maken met een tekst erin
        messagebox.showinfo("NS bericht", "De NS groet u.")

    def Onpress(self, i):
        # askBox maken warin wordt gevraagt of deze verzenden moet worden, daarna wordt bij ja wordt het bericht verstuurde naar twitter,
        # weggeschrijven naar log, tweet wordt verwijderd uit variable list, Tweet wordt verwijderd uit csv, en GUI wordt gerefreshed.
        # bij nee wordt het bovenstaande uitgevoerd zonder de tweet te versturen
        result = messagebox.askquestion("Tweet versturen", "Wilt u deze tweet versturen?", icon="warning")
        if result == 'yes':
            messagebox.showinfo("Bericht", "Tweet: " + self.list[i][0] + " van " + self.list[i][1] + " is verstuurd")
            self.twitter.postTweet(self.list[i][1] + ": " + self.list[i][0])
            self.logBestand(self.list[i][0], self.list[i][1], "Verstuurd")
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.ref1()
        else:
            messagebox.showinfo("Bericht", "Tweet: " + self.list[i][0] + " van " + self.list[i][1] + " is verwijderd")
            self.logBestand(self.list[i][0], self.list[i][1], "Afgewezen")
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.ref1()

    def TweetVerwijderen(self):
        # Tweet wordt uit CSV verwijdert
        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['tweet', 'plaatser', 'tijd'])
            for row in self.list:
                writer.writerow(row)

    def logBestand(self, tweet, plaatser, status):
        # tweet wordt in log gezet met de tijd van inzetten en of deze is verzonden of afgewezen
        with open(LOG_PATH, 'r') as rbestand:
            s = rbestand.read().splitlines()
        with open(LOG_PATH, "w") as bestand:
            for lines in s:
                bestand.write(lines + '\n')
            bestand.write(datetime.datetime.now().strftime("Time: %d-%m-%Y %H:%M:%S, ") + tweet + ', ')
            bestand.write(plaatser + "," + status)

    def KleurTweet(self):
        # als er geen tweet ontvanen is wordt de kleur van bovenste balk rood en anders is deze groen
        if self.IsTweetOntvangen() == 0:
            global kleur
            kleur = "red"
        else:
            kleur = "green"
        return kleur

    def buttonWidth(self, tweet):
        # als tweet langer is dan in de button past dan wordt de button vergroot
        width = 75
        if len(tweet) > width:
            width = len(tweet)
        return width


mainWindow = Tk()
mainWindow.title("TweetsCheck MainPanel")
MainMenu(mainWindow)
mainWindow.attributes('-fullscreen', True)
mainWindow.configure(background='#fcc917')
mainWindow.iconbitmap(IMG_PATH + "Ns.ico")
mainWindow.mainloop()
