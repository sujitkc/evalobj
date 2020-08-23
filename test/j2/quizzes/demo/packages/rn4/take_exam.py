from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import csv

class letsQuiz:

    def __init__(self, window, ques, frame1):
        self.newWindow = window
        self.ques = ques
        self.question_counter = -1
        self.questions = []
        self.answerbutton = []  # mcq
        self.answerbutton1 = []  # mtf
        self.answers = []
        self.answers1 =[]
        self.frame1 = frame1

        for i in range(len(ques)):
            self.questions.append("Question " + str(i + 1) + " :")

        list = []
        for i in range(len(ques)):
            list.append("")
        csvfile = open('theory_answers.csv', 'wt', newline='')
        obj = csv.writer(csvfile)
        obj.writerows(list)

        self.label1 = Label(self.newWindow, text="IIITB EXAMINATION", font=
        ("Arial", "30"), pady=30)

        self.label2 = Label(self.newWindow, text="Print Instructions", font=
        ("Arial", "24"), pady=30)

        self.start = Button(self.newWindow, text="Start",
                            command=lambda: [self.label2.pack_forget(), self.start.pack_forget(), self.next_question()])

    def packheader(self):
        self.label1.pack()
        self.label2.pack()
        self.start.pack()

    def pack_all(self):
        self.label.pack()

        if (self.ques[self.question_counter][0] == "MCQ"):
            for j in range(self.ques[self.question_counter][2]):
                self.answerbutton[j].pack()

        elif (self.ques[self.question_counter][0] == "MTF"):
            self.frame1.pack()

        self.nextButton.pack(side=RIGHT)
        self.prevButton.pack(side=LEFT)

    def forget_all(self):
        self.label.pack_forget()

        if (self.ques[self.question_counter][0] == "MCQ"):
            for j in range(self.ques[self.question_counter][2]):
                self.answerbutton[j].pack_forget()

        elif (self.ques[self.question_counter][0] == "MTF"):
            self.frame1.pack_forget()

        self.nextButton.pack_forget()
        self.prevButton.pack_forget()

    def quit_window(self):
        self.newWindow.destroy()

    def onclick(self):

        if (self.ques[self.question_counter][0] == "MCQ"):
            ans = ""
            flag = 0
            for i in range(len(self.answers)):
                if (self.answers[i].get() == 1):
                    if (flag != 0):
                        ans += ","
                    flag = 1
                    ans += str(i + 1)

            f = open('theory_answers.csv', "r")
            contents = f.readlines()
            f.close()
            contents[self.question_counter] = "\n"
            contents.insert(self.question_counter, ans)
            f = open('theory_answers.csv', "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()



        elif (self.ques[self.question_counter][0] == "MTF"):

            ans = ""
            flag = 0
            flag1= 0
            for i in range(len(self.answers1)):
                if (flag1 != 0):
                    ans += ","
                flag1 = 1
                ans+='"'
                flag=0
                for j in range(len(self.answers1[i])):
                    if (self.answers1[i][j].get() == 1):
                        if (flag != 0):
                            ans += ","
                        flag = 1
                        ans += str(j + 1)
                ans+='"'
            f = open('theory_answers.csv', "r")
            contents = f.readlines()
            f.close()
            contents[self.question_counter] = "\n"
            contents.insert(self.question_counter, ans)
            f = open('theory_answers.csv', "w")
            contents = "".join(contents)
            f.write(contents)
            f.close()


    def checkbox_status(self):
        f = open('theory_answers.csv', "r")
        contents = f.readlines()
        f.close()
        k = contents[self.question_counter]
        li = list(k.split(","))
        for i in li:
            if (i != ',' and i != '\n'):
                self.answers[int(i) - 1].set(1)

    def checkbox_status1(self):
        f = open('theory_answers.csv', "r")
        contents = f.readlines()
        f.close()
        k = contents[self.question_counter]
        if(k=='\n'):
            return
        li = list(k.split('"'))
        li1=[]
        flag=0
        for i in li:
            if(flag%2!=0):
                li1.append(i)
            flag+=1
        k=0
        for i in li1:
            print(i)
            for j in i:
                if (j != ',' and j != '\n'):
                    self.answers1[k][int(j) - 1].set(1)
            k+=1

    def mcq_question(self):
        self.answers = []
        self.answerbutton = []
        for i in range(self.ques[self.question_counter][2]):
            self.answerbutton.append("")

        for j in range(self.ques[self.question_counter][2]):
            self.answers.append(IntVar())

        self.checkbox_status()
        for j in range(self.ques[self.question_counter][2]):
            self.answerbutton[j] = Checkbutton(self.newWindow, text="option " + str(j + 1), var=self.answers[j])


    def mtf_question(self):
        self.answers=[]        
        self.answers1 = []

        for i in range(self.ques[self.question_counter][2]):
            self.answers=[]
            for j in range(self.ques[self.question_counter][3]):
                self.answers.append(IntVar())
            self.answers1.append(self.answers)

        self.checkbox_status1()

        for i in range(self.ques[self.question_counter][2]):
            for j in range(self.ques[self.question_counter][3]+1):
                if (j == 0):
                    name = chr(65 + i)
                    Label(self.frame1, text=name, borderwidth=1).grid(row=i, column=j)
                else:
                    name = "Option " + str(j)
                    Checkbutton(self.frame1, text=name, var=self.answers1[i][j-1]).grid(row=i, column=j)


    def prev_question(self):
        self.forget_all()
        self.question_counter -= 1
        if (self.question_counter >= 0):

            self.label = Label(self.newWindow, text=self.questions[self.question_counter], font=
            ("Arial", "24"), pady=30)

            if (self.ques[self.question_counter][0] == "MCQ"):
                self.mcq_question()

            elif (self.ques[self.question_counter][0] == "MTF"):
                self.mtf_question()

                            # buttons
            self.prevButton = Button(self.newWindow, text="Prev",
                                     command=lambda: [self.onclick(), self.prev_question()])
            if (self.question_counter + 1 < len(self.ques)):
                self.nextButton = Button(self.newWindow, text="Next",
                                         command=lambda: [self.onclick(), self.next_question()])
            else:
                self.nextButton = Button(self.newWindow, text="Submit",
                                         command=lambda: [self.onclick(), self.next_question()], bg="teal")

            self.pack_all()  # place in the new question
        else:
            self.question_counter = 1
            self.prev_question()

    def next_question(self):
        # clear the screen
        if (self.question_counter != -1):
            self.forget_all()
        self.question_counter += 1

        try:

            self.label = Label(self.newWindow, text=self.questions[self.question_counter], font=
            ("Arial", "24"), pady=30)

            if (self.ques[self.question_counter][0] == "MCQ"):
                self.mcq_question()

            elif (self.ques[self.question_counter][0] == "MTF"):
                self.mtf_question()

                            # buttons
            self.prevButton = Button(self.newWindow, text="Prev",
                                     command=lambda: [self.onclick(), self.prev_question()])
            if (self.question_counter + 1 < len(self.ques)):
                self.nextButton = Button(self.newWindow, text="Next",
                                         command=lambda: [self.onclick(), self.next_question()])
            else:
                self.nextButton = Button(self.newWindow, text="Submit",
                                         command=lambda: [self.onclick(), self.next_question()], bg="teal")

            self.pack_all()  # place in the new question


        except IndexError:
            self.question_counter -= 1
            self.forget_all()

            msg = Label(self.newWindow, text="You have completed the exam, Thank you!! \n-Team CHAOS", font=
            ("Arial", "24"), pady=30)
            quit = Button(self.newWindow, text="Quit", command=lambda: [self.quit_window()], bg="teal")
            msg.pack()
            quit.pack()
