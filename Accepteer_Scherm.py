from tkinter import *
from tkinter import messagebox
import csv
import twitter
import csv

from config import CSV_PATH


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
        self.refresh()


    def create_GUI(self):
        r = ''
        self.label1 = Label(mainWindow, text=self.MainMessage()[0], width="2000", height="1",
                            background=self.KleurTweet(), anchor='w')
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(mainWindow, text=self.MainMessage()[1], width="2000", height="1",
                            background=self.KleurTweet(), anchor='w')
        self.label2.grid(row=1, column=0, sticky=W)
    def refresh(self):
        #self.button
        for b in self.button:
            b.grid_forget()

        self.list = self.TweetOntvangen()

        for i in range(len(self.list)):
            self.button.append(Button(mainWindow,
                                 text=(self.list[i][0] + " ontvangen door, " + self.list[i][1]),
                                 command= lambda i=i: self.Onpress(i), width="2000", anchor='w'))
            print(self.list[i][0])

            self.button[i].grid(row=2 + i, column=0, sticky=W)

    def TweetOntvangen(self):
        # Alle Tweets met daarbij de verzender word uit een CSV-bestand naar een list geschreven
        with open("data/tweets.csv ", "r") as MyCsvFile:
            reader = csv.DictReader(MyCsvFile)
            OntvangenTweets = []
            for row in reader:
                OntvangenTweets.append([row['tweet'], row['plaatser']])
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

    def Onpress(self, i):
        result = messagebox.askquestion("Tweet versturen", "Wilt u deze tweet versturen?", icon="warning")
        if result == 'yes':
            #self.twitter.postTweet(self.list[i][0])
            self.list.remove(self.list[i])
            print(self.list)
            self.TweetVerwijderen()
            self.refresh()
        else:
            print("b")
            self.list.remove(self.list[i])
            return

    def TweetVerwijderen(self):
        #with open("data/tweets.csv", "w") as MyCsvFile:
            #fieldnames  = ['tweet', 'plaatser']
            #writer = csv.DictWriter(MyCsvFile, fieldnames=fieldnames)
            #writer.writeheader()
            #print(self.list)
            #for i in range(len(self.list)):
            #    writer.writerow(self.list[i][0])

        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f , delimiter=',')
            writer.writerow(['tweet', 'plaatser'])
            for row in self.list:
                writer.writerow(row)


    def FormaatKiezen(self):
        # screen = str(input("screenformaat? Je kunt invullen:\nFullscreen\nFormaat in HxB bijvoorbeeld 1920x1080\n")).lower()
        # if screen == 'fullscreen':
        #     return mainWindow.attributes('-fullscreen', True)
        # else:
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
mainWindow.configure(background=kleur)
mainWindow.mainloop()
