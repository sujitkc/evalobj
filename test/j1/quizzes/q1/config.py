applicationHome = "/home/sujit/IIITB/projects/evalobj/"

import sys
sys.path.append(applicationHome)
from src.qtypes import MCQType
from src.qtypes import MTFQType

courseName = "Software Design"
courseCode = "SE101"
assessmentName = "J1"
assessmentHome = "/home/sujit/IIITB/projects/evalobj/test/j1/quizzes/q1/"
rollNumberFile = "/home/sujit/IIITB/projects/evalobj/test/j1/class.csv"
items = [MCQType("item1", 4, 1.0), MCQType("item2", 4, 1.0), MCQType("item3", 4, 1.0), MCQType("item4", 4, 1.0), MCQType("item5", 4, 1.0), MCQType("item6", 4, 1.0), MCQType("item7", 4, 1.0), MCQType("item8", 4, 1.0), MCQType("item9", 4, 1.0), MCQType("item10", 4, 1.0), MCQType("item11", 4, 1.0), MCQType("item12", 4, 1.0), MCQType("item13", 4, 1.0), MCQType("item14", 4, 1.0), MCQType("item15", 4, 1.0), ]
numOfAIs = 3
QPperAI = 2
QperQP = 5
