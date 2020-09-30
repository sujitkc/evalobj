applicationHome = "/home/keshav/Desktop/PE/AutomatedQuiz/"

import sys
sys.path.append(applicationHome)
import src.qtypes as q
courseName = "Python-PrepTerm"
courseCode = "SKC-Python"
assessmentName = "Quiz"
assessmentHome = "/home/keshav/Desktop/PE/AutomatedQuiz/test/python_quiz/"
rollNumberFile = "/home/keshav/Desktop/PE/AutomatedQuiz/test/python_quiz/class.csv"
items = [q.MCQQType(items = { 'name' :'item1','properties':{'qtype':'MCQ', 'marks':'1.0','options':'4'}}), q.MTFQType(items = { 'name' :'item2','properties':{'qtype':'MTF', 'marks':'1.0','left':'4','right':'3'}}), q.MCQQType(items = { 'name' :'item3','properties':{'qtype':'MCQ', 'marks':'1.0','options':'4'}}), ]
numOfAIs = 5
itemsPerAI = 2
