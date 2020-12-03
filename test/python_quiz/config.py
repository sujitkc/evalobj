applicationHome = "/home/keshav/Desktop/PE/AutomatedQuiz/"

import sys
sys.path.append(applicationHome)
from src.qtypes import MCQType
from src.qtypes import MTFQType

courseName = "Python-PrepTerm"
courseCode = "SKC-Python"
assessmentName = "Quiz"
assessmentHome = "/home/keshav/Desktop/PE/AutomatedQuiz/test/python_quiz/"
rollNumberFile = "/home/keshav/Desktop/PE/AutomatedQuiz/test/python_quiz/class.csv"
items = [MCQType("item1","MCQ",4, 1.0), MCQType("item2","MCQ",4, 1.0), MTFQType("item3","MTF",3, 4, 1.0), MCQType("item4","MCQ",4, 1.0), ]
numOfAIs = 5
itemsPerAI = 3
