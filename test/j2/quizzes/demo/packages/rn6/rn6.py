from tkinter import *
from take_exam import letsQuiz
root = Tk()
root.title('CHAOS_EXAM_GUI')
root.geometry("700x600")
frame1 = Frame(root)
f = open('response/theory_answers.csv', 'w+')
ques = [['MCQ', 1.0, 4, 0, 'item28'], ['MCQ', 1.0, 4, 0, 'item36'], ['MCQ', 1.0, 4, 0, 'item55'], ['MCQ', 1.0, 4, 0, 'item8'], ['MCQ', 1.0, 4, 0, 'item1'], ['MCQ', 1.0, 4, 0, 'item9'], ['MCQ', 1.0, 4, 0, 'item52'], ['MCQ', 1.0, 4, 0, 'item31'], ['MCQ', 1.0, 4, 0, 'item32'], ['MCQ', 1.0, 4, 0, 'item48'], ['MCQ', 1.0, 4, 0, 'item13'], ['MCQ', 1.0, 4, 0, 'item42'], ['MCQ', 1.0, 4, 0, 'item46'], ['MCQ', 1.0, 4, 0, 'item30'], ['MCQ', 1.0, 4, 0, 'item39'], ['MCQ', 1.0, 4, 0, 'item40'], ['MCQ', 1.0, 4, 0, 'item2'], ['MCQ', 1.0, 4, 0, 'item12'], ['MCQ', 1.0, 4, 0, 'item50'], ['MCQ', 1.0, 4, 0, 'item33']]
quiz = letsQuiz(root, ques, frame1)
message_label1 = Label(text="IIITB EXAM PORTAL\nThis quiz is conducted by - \n", font = ( "Arial", "25"), padx=40, pady=20)
message_label2 = Label(root, text="Click 'Continue' to begin the exam.", wraplength=250)
button1 = Button(root, text ="Continue", command=lambda:[message_label1.pack_forget(),message_label2.pack_forget(),button1.pack_forget(),quiz.packheader()], width=16, bg="teal")
message_label1.pack()
message_label2.pack()
button1.pack()
root.protocol("WM_DELETE_WINDOW", root.iconify)
root.mainloop()