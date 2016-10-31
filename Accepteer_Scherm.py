from tkinter import *
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        self.label = Label(mainWindow, text=MainMessage()[0], width="2000",height = "1", background=KleurTweet(), anchor='w')
        self.label.grid(row=0, column=0, sticky=W)
        self.label = Label(mainWindow, text=MainMessage()[1], width="2000",height = "1", background=KleurTweet(), anchor='w')
        self.label.grid(row=1, column=0, sticky=W)
        for i in range(len(TweetOntvangen()[0])):
            self.label = Button(mainWindow, text=(TweetOntvangen()[0][i]+ " ontvangen door, "+ TweetOntvangen()[1][i]), width="2000", anchor='w')

            self.label.grid(row=2+i, column=0, sticky=W)

def TweetOntvangen():


        with open("C:/Users/jeffrey/Dropbox/PycharmProjects/ns_twitter_project_hu2/data/tweets.csv ", "r") as MyCsvFile:
            tweet = 0
            reader = csv.DictReader(MyCsvFile)
            OntvangenTweets = []
            GeplaatstDoor = []
            for row in reader:
                OntvangenTweets.append(row['tweet'])
                GeplaatstDoor.append(row["plaatser"])
        return OntvangenTweets,GeplaatstDoor
def IsTweetOntvangen():
    if len(TweetOntvangen()[0]) != 0:
        Tweet = 1
    else:
        Tweet = 0
    return Tweet

def MainMessage():
    bericht = ""
    bericht1 = ''
    if IsTweetOntvangen()== 0:
        bericht = 'U heeft geen bericht ontvangen.'
    if IsTweetOntvangen()== 1:
        if len(TweetOntvangen()[0]) > 1:
            bericht = "U heeft "+str(len(TweetOntvangen()[0]))+" berichten"
            bericht1 = "Dit zijn de berichten:"
        else:
            bericht = "U heeft een bericht."
            bericht1 = "Dit is uw bericht:"
    return bericht, bericht1

def FormaatKiezen():
    # screen = str(input("screenformaat? Je kunt invullen:\nFullscreen\nFormaat in HxB bijvoorbeeld 1920x1080\n")).lower()
    # if screen == 'fullscreen':
    #     return mainWindow.attributes('-fullscreen', True)
    # else:
        return mainWindow.geometry('500x500+1920+200')
def KleurTweet():
    if IsTweetOntvangen()== 0:
        kleur = "red"
    else:
        kleur = "green"
    return kleur




TweetOntvangen()
mainWindow = Tk()
mainWindow.title("TweetsCheck MainPanel")
FormaatKiezen()
MainMenu(mainWindow)
mainWindow.configure(background=KleurTweet())
mainWindow.mainloop()


