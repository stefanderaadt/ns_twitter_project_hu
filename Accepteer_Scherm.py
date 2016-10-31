from tkinter import *
import csv

class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)

        self.grid()
        self.create_GUI()

    def create_GUI(self):
        self.label = Label(mainWindow, text=MainMessage(), width="75",height = "3", background=KleurTweet())
        self.label.grid(row=0, column=0, sticky=W)
        for i in range(len(TweetOntvangen())):
            self.label = Label(mainWindow, text=TweetOntvangen()[i], width="100", anchor='w')
            self.label.grid(row=1+i, column=0, sticky=W)

def TweetOntvangen():


        with open("C:/Users/jeffrey/Dropbox/PycharmProjects/ns_twitter_project_hu2/data/tweets.csv ", "r") as MyCsvFile:
            tweet = 0
            reader = csv.DictReader(MyCsvFile)
            OntvangenTweets = []
            for row in reader:
                OntvangenTweets.append(row['tweet'])
        return OntvangenTweets
def IsTweetOntvangen():
    if len(TweetOntvangen()) != 0:
        Tweet = 1
    else:
        Tweet = 0
    return Tweet

def MainMessage():
    bericht = ""
    if IsTweetOntvangen()== 0:
        bericht = 'U heeft geen bericht ontvangen.'
    if IsTweetOntvangen()== 1:
        bericht = "U heeft een bericht.\n Dit zijn de berichten:"
    return( bericht)

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
mainWindow.configure(background="grey")
mainWindow.mainloop()


