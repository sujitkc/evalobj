from tkinter import *
from take_exam import letsQuiz
root = Tk()
root.title('CHAOS_EXAM_GUI')
root.geometry("700x600")
frame1 = Frame(root)
f = open('response/theory_answers.csv', 'w+')
ques = [['MCQ', 1.0, 4, 0, 'item25'], ['MCQ', 1.0, 4, 0, 'item12'], ['MCQ', 1.0, 4, 0, 'item36'], ['MCQ', 1.0, 4, 0, 'item53'], ['MCQ', 1.0, 4, 0, 'item7'], ['MCQ', 1.0, 4, 0, 'item38'], ['MCQ', 1.0, 4, 0, 'item43'], ['MCQ', 1.0, 4, 0, 'item31'], ['MCQ', 1.0, 4, 0, 'item32'], ['MCQ', 1.0, 4, 0, 'item29'], ['MCQ', 1.0, 4, 0, 'item44'], ['MCQ', 1.0, 4, 0, 'item10'], ['MCQ', 1.0, 4, 0, 'item9'], ['MCQ', 1.0, 4, 0, 'item51'], ['MCQ', 1.0, 4, 0, 'item37'], ['MCQ', 1.0, 4, 0, 'item17'], ['MCQ', 1.0, 4, 0, 'item28'], ['MCQ', 1.0, 4, 0, 'item52'], ['MCQ', 1.0, 4, 0, 'item39'], ['MCQ', 1.0, 4, 0, 'item1']]
quiz = letsQuiz(root, ques, frame1)
message_label1 = Label(text="IIITB EXAM PORTAL\nThis quiz is conducted by - \n", font = ( "Arial", "25"), padx=40, pady=20)
message_label2 = Label(root, text="Click 'Continue' to begin the exam.", wraplength=250)
button1 = Button(root, text ="Continue", command=lambda:[message_label1.pack_forget(),message_label2.pack_forget(),button1.pack_forget(),quiz.packheader()], width=16, bg="teal")
message_label1.pack()
message_label2.pack()
button1.pack()
root.protocol("WM_DELETE_WINDOW", root.iconify)
root.mainloop()
