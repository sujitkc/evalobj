applicationHome = "/home/keshav/Desktop/PE/AutomatedQuiz/"

import sys
sys.path.append(applicationHome)
from src.qtypes import MCQType
from src.qtypes import MTFQType

courseName = "Software Design"
courseCode = "SE101"
assessmentName = "demo"
assessmentHome = "/home/keshav/Desktop/PE/AutomatedQuiz/test/j2/quizzes/demo/"
rollNumberFile = "/home/keshav/Desktop/PE/AutomatedQuiz/test/j2/class.csv"
items = [MTFQType("item1","MTF",4, 7, 1.0), MCQType("item2","MCQ",4, 1.0), MCQType("item3","MCQ",4, 1.0), MCQType("item4","MCQ",4, 1.0), MCQType("item5","MCQ",4, 1.0), ]
numOfAIs = 4
itemsPerAI = 3
