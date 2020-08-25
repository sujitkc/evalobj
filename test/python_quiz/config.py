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
items = [MCQType("item1","MCQ",4, 1.0), MCQType("item2","MCQ",4, 1.0), MCQType("item3","MCQ",4, 1.0), MCQType("item4","MCQ",4, 1.0), MCQType("item5","MCQ",4, 1.0), MCQType("item7","MCQ",4, 1.0), MCQType("item8","MCQ",4, 1.0), MCQType("item9","MCQ",4, 1.0), MCQType("item10","MCQ",4, 1.0), MCQType("item11","MCQ",4, 1.0), MCQType("item12","MCQ",4, 1.0), MCQType("item13","MCQ",4, 1.0), MCQType("item14","MCQ",4, 1.0), MCQType("item15","MCQ",4, 1.0), MCQType("item16","MCQ",4, 1.0), MCQType("item17","MCQ",4, 1.0), MCQType("item18","MCQ",4, 1.0), MCQType("item19","MCQ",4, 1.0), MCQType("item20","MCQ",4, 1.0), MCQType("item21","MCQ",4, 1.0), MCQType("item22","MCQ",4, 1.0), MCQType("item23","MCQ",4, 1.0), MCQType("item24","MCQ",4, 1.0), MCQType("item25","MCQ",4, 1.0), MCQType("item26","MCQ",4, 1.0), MCQType("item27","MCQ",4, 1.0), MCQType("item28","MCQ",4, 1.0), MCQType("item29","MCQ",4, 1.0), MCQType("item30","MCQ",4, 1.0), MCQType("item31","MCQ",4, 1.0), MCQType("item32","MCQ",4, 1.0), MCQType("item33","MCQ",4, 1.0), MCQType("item34","MCQ",4, 1.0), MCQType("item35","MCQ",4, 1.0), MCQType("item36","MCQ",4, 1.0), MCQType("item37","MCQ",4, 1.0), MCQType("item38","MCQ",4, 1.0), MCQType("item39","MCQ",4, 1.0), MCQType("item40","MCQ",4, 1.0), MCQType("item41","MCQ",4, 1.0), MCQType("item42","MCQ",4, 1.0), MCQType("item43","MCQ",4, 1.0), MCQType("item44","MCQ",4, 1.0), MCQType("item45","MCQ",4, 1.0), MCQType("item46","MCQ",4, 1.0), MCQType("item47","MCQ",4, 1.0), MCQType("item48","MCQ",4, 1.0), MCQType("item49","MCQ",4, 1.0), MCQType("item50","MCQ",4, 1.0), MCQType("item51","MCQ",4, 1.0), MCQType("item52","MCQ",4, 1.0), MCQType("item53","MCQ",4, 1.0), MCQType("item54","MCQ",4, 1.0), MCQType("item55","MCQ",4, 1.0), ]
numOfAIs = 195
itemsPerAI = 20
