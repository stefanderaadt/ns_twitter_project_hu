from tkinter import *
from tkinter import messagebox
import csv
import twitter


class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.button = []

        self.grid()
        self.create_GUI()
        self.twitter = twitter.Twitter()
        self.TweetOntvangen()
        self.FormaatKiezen()


    def create_GUI(self):
        r = ''
        self.label1 = Label(mainWindow, text=self.MainMessage()[0], width="2000", height="1",
                            background=self.KleurTweet(), anchor='w')
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(mainWindow, text=self.MainMessage()[1], width="2000", height="1",
                            background=self.KleurTweet(), anchor='w')
        self.label2.grid(row=1, column=0, sticky=W)

        for i in range(len(self.TweetOntvangen())):
            self.button.append(Button(mainWindow,
                                 text=(self.TweetOntvangen()[i][0] + " ontvangen door, " + self.TweetOntvangen()[i][1]),
                                 command= lambda i=i: self.Onpress(i), width="2000", anchor='w'))

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
        if len(self.TweetOntvangen()[0]) != 0:
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
                bericht = "U heeft " + str(len(self.TweetOntvangen()[0])) + " berichten"
                bericht1 = "Dit zijn de berichten:"
            else:
                bericht = "U heeft een bericht."
                bericht1 = "Dit is uw bericht:"
        return bericht, bericht1

    def Onpress(self,i):
        result = messagebox.askquestion("Tweet versturen", "Wilt u deze tweet versturen?", icon="warning")
        if result == 'yes':
            print(self.TweetOntvangen()[i][0])
            print(self.TweetOntvangen())
        else:
            print("b")
        return


    def FormaatKiezen(self):
        # screen = str(input("screenformaat? Je kunt invullen:\nFullscreen\nFormaat in HxB bijvoorbeeld 1920x1080\n")).lower()
        # if screen == 'fullscreen':
        #     return mainWindow.attributes('-fullscreen', True)
        # else:
        # return mainWindow.geometry('500x500+1920+200')

        return mainWindow.geometry('500x500')

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
