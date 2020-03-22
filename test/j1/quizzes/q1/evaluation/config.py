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
items = [
  MCQType("item1", 4, 1),         #1
  MCQType("item2", 4, 1),         #2
  MCQType("item3", 6, 1),         #3
  MCQType("item4", 4, 1),         #4
  MCQType("item5", 5, 1),         #5
  MCQType("item6", 7, 1),         #6
  MCQType("item7", 10, 1),         #7
  MCQType("item8", 5, 1),         #8
  MCQType("item9", 6, 1),         #9
  MCQType("item10", 4, 1),         #10
  MCQType("item11", 4, 1),         #11
  MCQType("item12", 5, 1),         #12
  MCQType("item13", 6, 1),         #13
  MCQType("item14", 6, 1),         #14
  MCQType("item15", 7, 1),         #15
]

# items = [MCQType("item1", 4, 1.0), MCQType("item2", 4, 1.0), MCQType("item3", 4, 1.0), MCQType("item4", 4, 1.0), MCQType("item5", 4, 1.0), MCQType("item6", 4, 1.0), MCQType("item7", 4, 1.0), MCQType("item8", 4, 1.0), MCQType("item9", 4, 1.0), MCQType("item10", 4, 1.0), MCQType("item11", 4, 1.0), MCQType("item12", 4, 1.0), MCQType("item13", 4, 1.0), MCQType("item14", 4, 1.0), MCQType("item15", 4, 1.0), ]
numOfAIs = 3
QPperAI = 2
QperQP = 5
