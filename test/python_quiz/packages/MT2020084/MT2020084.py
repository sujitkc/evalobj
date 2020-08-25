from tkinter import *
from take_exam import letsQuiz
root = Tk()
root.title('CHAOS_EXAM_GUI')
root.geometry("700x600")
frame1 = Frame(root)
f = open('response/theory_answers.csv', 'w+')
ques = [['MCQ', 1.0, 4, 0, 'item14'], ['MCQ', 1.0, 4, 0, 'item33'], ['MCQ', 1.0, 4, 0, 'item40'], ['MCQ', 1.0, 4, 0, 'item38'], ['MCQ', 1.0, 4, 0, 'item16'], ['MCQ', 1.0, 4, 0, 'item50'], ['MCQ', 1.0, 4, 0, 'item31'], ['MCQ', 1.0, 4, 0, 'item1'], ['MCQ', 1.0, 4, 0, 'item17'], ['MCQ', 1.0, 4, 0, 'item49'], ['MCQ', 1.0, 4, 0, 'item51'], ['MCQ', 1.0, 4, 0, 'item2'], ['MCQ', 1.0, 4, 0, 'item11'], ['MCQ', 1.0, 4, 0, 'item5'], ['MCQ', 1.0, 4, 0, 'item55'], ['MCQ', 1.0, 4, 0, 'item46'], ['MCQ', 1.0, 4, 0, 'item42'], ['MCQ', 1.0, 4, 0, 'item13'], ['MCQ', 1.0, 4, 0, 'item23'], ['MCQ', 1.0, 4, 0, 'item21']]
quiz = letsQuiz(root, ques, frame1)
message_label1 = Label(text="IIITB EXAM PORTAL\nPYTHON QUIZ - [prep term]\n", font = ( "Arial", "25"), padx=40, pady=20)
message_label2 = Label(root, text="Click 'Continue' to begin the exam.", wraplength=250)
button1 = Button(root, text ="Continue", command=lambda:[message_label1.pack_forget(),message_label2.pack_forget(),button1.pack_forget(),quiz.packheader()], width=16, bg="teal")
message_label1.pack()
message_label2.pack()
button1.pack()
root.protocol("WM_DELETE_WINDOW", root.iconify)
root.mainloop()
