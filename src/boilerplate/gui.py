import os
from src.boilerplate.take_exam import letsQuiz
import shutil
from src.path import Path

class GUIGeneartor():
    def __init__(self, items, aiCode, config ):
        self.items = items
        self.aiCode = aiCode
        self.config = config
        self.data = []
        for i in items:
            for con in config:
                if(con.name == i):
                    self.data.append(con)
        self.applicationHome = Path.applicationHome
        self.ques = []
        for i in self.data:
            d=i.toList()
            self.ques.append(d)
        print(self.ques)
        self.display()

    def display(self):
        packageDirectory = self.applicationHome + "test/python_quiz/packages/"
        if (not os.path.exists(packageDirectory)):
            os.mkdir(packageDirectory)
        aiDirec = packageDirectory + self.aiCode + "/"
        if (not os.path.exists(aiDirec)):
            os.mkdir(aiDirec)
        configSrcFile = aiDirec +self.aiCode+".py"
        if (not os.path.exists(configSrcFile)):
            print("Configuration source file " + configSrcFile + \
                  " not found. Creating ...")
            with open(configSrcFile, "w+") as fout:
                fout.write(str(self))
        else:
            print("Configuration source file " + configSrcFile + \
                  " found. Doing nothing.")
        shutil.copyfile(self.applicationHome + "src/boilerplate/take_exam.py",
                        aiDirec + "take_exam.py")
        shutil.copyfile(self.applicationHome + "src/boilerplate/instructions.txt",
                        aiDirec + "instructions.txt")
        submission= aiDirec + "response/"
        if (not os.path.exists(submission)):
            os.mkdir(submission)


    def __str__(self):
        s = ""
        s += "from tkinter import *" + "\n"
        s += "from take_exam import letsQuiz" + "\n"
        s += "root = Tk()" + "\n"
        s += "root.title('CHAOS_EXAM_GUI')" + "\n"
        s += "root.geometry(\"700x600\")" + "\n"
        s += "frame1 = Frame(root)" + "\n"
        s += "f = open('response/theory_answers.csv', 'w+')" + "\n"
        s += "ques = " + str(self.ques) + "\n"
        s += "quiz = letsQuiz(root, ques, frame1)" + "\n"
        s += "message_label1 = Label(text=\"IIITB EXAM PORTAL\\nPYTHON QUIZ - [prep term]\\n\", font = ( \"Arial\", \"25\"), padx=40, pady=20)" + "\n"
        s += "message_label2 = Label(root, text=\"Click 'Continue' to begin the exam.\", wraplength=250)" + "\n"
        s += "button1 = Button(root, text =\"Continue\", command=lambda:[message_label1.pack_forget(),message_label2.pack_forget(),button1.pack_forget(),quiz.packheader()], width=16, bg=\"teal\")" + "\n"
        s +="message_label1.pack()" + "\n"
        s += "message_label2.pack()" + "\n"
        s += "button1.pack()" + "\n"
        s += "root.protocol(\"WM_DELETE_WINDOW\", root.iconify)" + "\n"
        s += "root.mainloop()" + "\n"
        return s




