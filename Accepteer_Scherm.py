from tkinter import *
from tkinter import messagebox
from config import *
import twitter
import csv
import datetime


class MainMenu(Frame):
    def __init__(self, master):
        super(MainMenu, self).__init__(master)
        self.button = []
        self.list = self.TweetOntvangen()
        self.frame = Frame
        self.grid()
        self.create_GUI()
        self.create_overige_GUI()
        self.twitter = twitter.Twitter()
        self.FormaatKiezen()
        self.timer()

    def create_GUI(self):
        screen_width = mainWindow.winfo_screenwidth()
        self.label1 = Label(mainWindow, text=self.MainMessage()[0], width=screen_width, height="1",
                            background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label1.grid(row=0, column=0, sticky=W)
        self.label2 = Label(mainWindow, text=self.MainMessage()[1], width=screen_width, height="2", background=self.KleurTweet(), anchor='w', font=(FONT, 16))
        self.label2.grid(row=1, column=0, sticky=W)

    def create_overige_GUI(self):

        self.photo = PhotoImage(file=IMG_PATH + "ns_logoklein.png")
        self.nsimage = Button(mainWindow, command=self.Onpressns, image=self.photo, width="200", height="97")
        self.nsimage.place(relx=1, rely=1, anchor=SE)
        self.refreshb = Button(mainWindow, text="Refresh", width=15, height="2", command=self.ref1, bg="#1c1c6b", fg='white')
        # self.refreshb.grid(row=2, column=0, sticky=W)
        self.refreshb.place(relx=1, rely=0.112, anchor=E)
        self.refreshb = Button(mainWindow, text="Refresh", width=15, height="2", command=self.ref1, bg="#1c1c6b", fg='white')
        # self.refreshb.grid(row=2, column=0, sticky=W)
        self.refreshb.place(relx=1, rely=0.112, anchor=E)
        self.exit = Button(mainWindow, text="Exit", width=15, height="2", command= self.quit, bg="#1c1c6b", fg='white')
        # self.refreshb.grid(row=2, column=0, sticky=W)
        self.exit.place(relx=0.939, rely=0.112, anchor=E)


    def Buttons(self):
        screen_width = mainWindow.winfo_screenwidth()
        self.list = self.TweetOntvangen()

        for b in self.button:
            b.destroy()

        self.button = []

        for i in range(len(self.TweetOntvangen())):  # self.list[i][0]
            if i>9:
                break
            self.button.append(Button(mainWindow, text=(self.list[i][0] + ". \nontvangen door: " + self.list[i][1] + " om " + self.list[i][2]),
                                      command=lambda i=i: self.Onpress(i), width=self.buttonWidth(self.list[i][0]), anchor=CENTER, height="2", bg='#1c1c6b', fg='#ffffff', font=(FONT, 15)))
            # self.button[i].grid(row=3 + i, column=0, sticky=W)
            self.button[i].place(relx=0.5, rely=0.20 + (0.082 * i), anchor=CENTER)

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

    def ref1(self):
        self.Buttons()
        self.KleurTweet()
        self.create_GUI()

    def timer(self):
        self.Buttons()
        self.KleurTweet()
        self.create_GUI()
        self.after(15000, self.timer)

    def Onpressns(self):
        messagebox.showinfo("NS bericht", "De NS groet u.")

    def Onpress(self, i):
        result = messagebox.askquestion("Tweet versturen", "Wilt u deze tweet versturen?", icon="warning")
        if result == 'yes':
            messagebox.showinfo("Bericht", "Tweet: " + self.list[i][0] + " van " + self.list[i][1] + " is verstuurd")
            #print(self.list[i][1]+": "+self.list[i][0])
            self.twitter.postTweet(self.list[i][1]+": "+self.list[i][0])
            self.logBestand(self.list[i][0], self.list[i][1], "Verstuurd")
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.timer()
        else:
            messagebox.showinfo("Bericht", "Tweet: " + self.list[i][0] + " van " + self.list[i][1] + " is verwijderd")
            self.logBestand(self.list[i][0], self.list[i][1], "Afgewezen")
            self.list.remove(self.list[i])
            self.TweetVerwijderen()
            self.timer()

    def TweetVerwijderen(self):

        with open(CSV_PATH, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['tweet', 'plaatser', 'tijd'])
            for row in self.list:
                writer.writerow(row)

    def logBestand(self, tweet, plaatser, status):
        with open(LOG_PATH, 'r') as rbestand:
            s = rbestand.read().splitlines()
        with open(LOG_PATH, "w") as bestand:
            for lines in s:
                bestand.write(lines + '\n')
            bestand.write(datetime.datetime.now().strftime("Time: %d-%m-%Y %H:%M:%S, ") + tweet + ', ')
            bestand.write(plaatser + "," + status)

    def FormaatKiezen(self):
        # screen = str(input("screenformaat? Je kunt invullen:\nFullscreen\nFormaat in HxB bijvoorbeeld 1920x1080\n")).lower()
        # if screen == 'fullscreen':
            return mainWindow.attributes('-fullscreen', True)
        # else:
        #     return mainWindow.geometry('1920x1020+0+27')

    def KleurTweet(self):
        if self.IsTweetOntvangen() == 0:
            global kleur
            kleur = "red"
        else:
            kleur = "green"
        return kleur

    # def buttonWidth(self):
    #     width = 50
    #     for i in range(len(self.list)):
    #         if len(self.list[i][0]) > width:
    #             width = len(self.list[i][0])
    #             print(width)
    #     return width
    def buttonWidth(self, tweet):
        width = 75
        if len(tweet) > width:
            width = len(tweet)
        return width

mainWindow = Tk()
mainWindow.title("TweetsCheck MainPanel")
MainMenu(mainWindow)
mainWindow.configure(background='#fcc917')
mainWindow.iconbitmap(IMG_PATH + "Ns.ico")
mainWindow.mainloop()