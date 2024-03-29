from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

questions = ["1.Who is the best mentor in Navgurukul?",
             "\n2.How many students in Navgurukul now ?",
             "\n3.Which course is providing by Navgurukul to student?",
             "\n4.Who is best dancer of Navgurukul",
             "\n5.Guido van Rossum in 1991 designed which language?",
             "\n6.Who is the community manager in Banglor campus?",
             "\n7.Who is the Best person in Navgurukul?",
             "\n8.How many team member is living in our campus?",
             "\n9.Which person is very kind hearted in Navgurukul?",
             "\n10.Which person is got job recently?",
             "\n11.When Archana will go home?",
             "\n12.When archana will come back?",
             "\n13.Who is the first miss Navgurukul?",
             "\n14.Who is the founder of navgurukul?",
             "\n15.Who is the best singer in Navgurukul?"]

first_option = ["Bharti", "120",
                "software engineering", "Pooja gupta and Durga dharve",
                "Javascript", "Samyukta di",
                "Savita di", "10 members", "Sarmistha di", "Pragati rahul",
                "4th April", "12 November",
                "Inme se koi bhi nahi", "Google", "Lalitha"]

second_option = ["Sarmistha", "106 students",
                 "law", "Archana aarya and Neha singh",
                 "Python", "Reena di",
                 "Reena di", "7 members", "Chandani sharma", "Sapna deshmukh",
                 "23rd October", "20 November",
                 "Karishma singh ",
                 "Shaina", "Chandani sharma"]

third_option = ["Anjum", "123",
                "C.A", "Chandani and likitha",
                "Java", "Sana",
                "Ujala parveen", "2 members", "Shubhangi ranjan", "Bharti di",
                "3rd November", "15th November",
                "Rani sharma",
                "Anureadha singh", "Rachana"]

fourth_option = ["Durga dharve", "70",
                 "PHD", "Laxmi and Anshika",
                 "C++", "Neelam di",
                 "Akshara mishra", "8 members", "Sara di", "Sarmistha di",
                 "2nd November",
                 "30 November",
                 "Archana aarya", "Abhishek gupta",
                 "Archana aarya"]

correct_answers = ["Durga dharve", "106 students", "software engineering", "Chandani and likitha", "Python", "Samyukta di",
                   "Reena di", "7 members", "Shubhangi ranjan", "Bharti di", "2nd November", "15th November", "Archana aarya", "Abhishek gupta",
                   "Rachana"]


def select(event):
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']

    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()
    for i in range(15):
        if value == correct_answers[i]:
            if value == third_option[14]:
                def playagain():
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    mixer.music.load('kbc.mp3')
                    mixer.music.play(-1)

                def on_closing():
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image15)
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.wait_visibility()
                root2.grab_set()
                root2.config(bg='pink')
                root2.geometry('500x400+140+30')
                root2.title('You won 1 million Pounds')
                centerimg = PhotoImage(file='center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='pink', fg='black')
                winlabel.pack()

                happyimage = PhotoImage(file='happy.png')
                happYLabel = Label(root2, image=happyimage, bg='pink')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='pink')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='pink', fg='black',
                                         bd=0
                                         , activebackground='pink', cursor='hand2', activeforeground='black',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='pink', fg='black', bd=0
                                     , activebackground='pink', cursor='hand2', activeforeground='black',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=images[i])

        if value not in correct_answers:
            def tryagain():
                mixer.music.load('kbc.mp3')
                mixer.music.play(-1)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()

            def on_closing():
                root1.destroy()
                root.destroy()

            mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.wait_visibility()
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 Pound')
            img = PhotoImage(file='center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='pink', fg='black')
            loselabel.pack()
            sadimage = PhotoImage(file='sad.png')
            sadlabel = Label(root1, image=sadimage, bg='pink')
            sadlabel.place(x=400, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='pink')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='pink', fg='black', bd=0
                                    , activebackground='pink', cursor='hand2', activeforeground='black',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='pink', fg='black', bd=0
                                 , activebackground='pink', cursor='hand2', activeforeground='black',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break


def lifeline50():
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton4.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)

    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)

        progressbarB.config(value=60)

        progressbarC.config(value=40)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=90)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=20)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=50)

        progressbarC.config(value=70)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=20)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=90)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=35)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)


def phoneLifeline():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play()

    phoneLifelineButton.config(image=phoneImageX, state=DISABLED)
    callButton.config(image=callimage)


def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The Answer is {correct_answers[i]}')
            engine.runAndWait()


root = Tk()
root.geometry('1270x652+0+0')
root.resizable(0, 0)
root.title('KON BANEGA CARODPATI BY ARCHANA AARYA')
root.config(bg='pink')

leftFrame = Frame(root, bg='pink', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='pink', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='pink', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='pink', pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='pink')
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file='center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='pink')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')

lifeline50Button = Button(topFrame, image=image50, bd=0, bg='pink', cursor='hand2', activebackground='pink', width=180,
                      height=80, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePolex = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='pink', cursor='hand2', activebackground='pink',
                            width=180, height=80, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImageX = PhotoImage(file='phoneAFriendX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='pink', cursor='hand2', activebackground='pink', width=180,
                     height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, bg='pink', bd=0, activebackground='pink', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)

amountimage = PhotoImage(file='Picture0.png')
image1 = PhotoImage(file='Picture1.png')
image2 = PhotoImage(file='Picture2.png')
image3 = PhotoImage(file='Picture3.png')
image4 = PhotoImage(file='Picture4.png')
image5 = PhotoImage(file='Picture5.png')
image6 = PhotoImage(file='Picture6.png')
image7 = PhotoImage(file='Picture7.png')
image8 = PhotoImage(file='Picture8.png')
image9 = PhotoImage(file='Picture9.png')
image10 = PhotoImage(file='Picture10.png')
image11 = PhotoImage(file='Picture11.png')
image12 = PhotoImage(file='Picture12.png')
image13 = PhotoImage(file='Picture13.png')
image14 = PhotoImage(file='Picture14.png')
image15 = PhotoImage(file='Picture15.png')

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file='lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)


questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), bg='black', fg='white', width=34, height=2,
                        wrap='word',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END, questions[0])




labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='pink', fg='black')
labelA.place(x=60,y=110)

optionButton1 = Button(bottomFrame, text=first_option[0], font=('arial', 18, 'bold'), bg='pink', fg='black',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='black')
optionButton1.place(x=100,y=100)

labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='pink', fg='black')
labelB.place(x=330,y=110)

optionButton2 = Button(bottomFrame, text=second_option[0], font=('arial', 18, 'bold'), bg='pink', fg='black',
                              cursor='hand2',bd=0,activebackground='pink',activeforeground='black')
optionButton2.place(x=370,y=100)

labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='pink', fg='black')
labelC.place(x=60,y=190)

optionButton3 = Button(bottomFrame, text=third_option[0], font=('arial', 18, 'bold'), bg='pink', fg='black',
                             cursor='hand2',bd=0,activebackground='pink',activeforeground='black')
optionButton3.place(x=100,y=180)

labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='pink', fg='black')
labelD.place(x=330,y=190)

optionButton4 = Button(bottomFrame, text=fourth_option[0], font=('arial', 18, 'bold'), bg='pink', fg='black',
                             cursor='hand2',bd=0,activebackground='pink',activeforeground='black')
optionButton4.place(x=370,y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='pink', fg='black')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='pink', fg='black')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='pink', fg='black')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='pink', fg='black')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)
root.mainloop()
