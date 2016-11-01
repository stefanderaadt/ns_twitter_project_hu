from tkinter import *
from tkinter import messagebox
from config import *
import twitter
import csv
import datetime
import termcolor

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.button = []

        self.frame = Frame
        self.grid()
        self.create_GUI()
        self.twitter = twitter.Twitter()
        self.list = self.TweetOntvangen()
        self.FormaatKiezen()
        self.timer()

    def create_GUI(self):
        r = ''
        self.label1 = Label(mainWindow, text=self.MainMessage()[0], width="2000", height="1",
                            background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(mainWindow, text=self.MainMessage()[1], width="2000", height="2",
                            background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label2.grid(row=1, column=0, sticky=W)

    def refresh(self):
        self.list = self.TweetOntvangen()

        for b in self.button:
            b.destroy()

        self.button = []

        for i in range(len(self.list)):
            self.button.append(Button(mainWindow,
                                      text=(str(1+i)+". Tweet: "+ self.list[i][0] + ". ontvangen door: " + self.list[i][1] + " om " + self.list[i][2]),
                                      command=lambda i=i: self.Onpress(i), width="2000", anchor='w', height="2",font=(FONT, 13)))

            self.button[i].grid(row=2 + i, column=0, sticky=W)

    def TweetOntvangen(self):
        # Alle Tweets met daarbij de verzender word uit een CSV-bestand naar een list geschreven
        with open(CSV_PATH, "r") as MyCsvFile:
            reader = csv.DictReader(MyCsvFile)
            OntvangenTweets = []
            for row in reader:
                OntvangenTweets.append([row['tweet'], row['plaatser'], row['tijd']])
        return OntvangenTweets

    def IsTweetOntvangen(self):
        if len(self.TweetOntvangen()) != 0:
            Tweet = 1
        else:
            Tweet = 0
        return Tweet

    def MainMessage(self):
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

    def timer(self):
        self.refresh()
        self.KleurTweet()
        self.create_GUI()
        self.after(1500, self.timer)

    def Onpress(self, i):
        result = messagebox.askquestion("Tweet versturen", "Wilt u deze tweet versturen?", icon="warning")
        if result == 'yes':
            self.twitter.postTweet(self.list[i][0])
            self.logBestand(self.list[i][0], self.list[i][1])
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.refresh()
        else:
            messagebox.showinfo("Bericht", "Tweet: " + self.list[i][0] + " van " + self.list[i][1] + " is verwijderd")
            self.logBestand(self.list[i][0], self.list[i][1])
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.refresh()

    def TweetVerwijderen(self):

        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['tweet', 'plaatser'])
            for row in self.list:
                writer.writerow(row)

    def logBestand(self, tweet, plaatser):
        with open(LOG_PATH, 'r') as rbestand:
            s = rbestand.read().splitlines()
        with open(LOG_PATH, "w") as bestand:
            for lines in s:
                bestand.write(lines + '\n')
            bestand.write(datetime.datetime.now().strftime("Time: %d-%m-%Y %H:%M:%S, ") + tweet + ', ')
            bestand.write(plaatser)

    def FormaatKiezen(self):
        screen = str(input("screenformaat? Je kunt invullen:\nFullscreen\nFormaat in HxB bijvoorbeeld 1920x1080\n")).lower()
        if screen == 'fullscreen':
            return mainWindow.attributes('-fullscreen', True)
        else:
            return mainWindow.geometry('500x500+200+200')

    def KleurTweet(self):
        if self.IsTweetOntvangen() == 0:
            global kleur
            kleur = "red"
        else:
            kleur = "green"
        return kleur


mainWindow = Tk()
mainWindow.title("TweetsCheck MainPanel")
MainMenu(mainWindow)
mainWindow.configure(background='#fcc917')
mainWindow.iconbitmap(IMG_PATH+"Ns.ico")
mainWindow.mainloop()
