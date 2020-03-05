#!/usr/bin/python3
import sys
import csv

sys.path.append("/Users/vibhavagarwal/Desktop/evalobj/")
import src.evaluator as E

class Evaluator_PL2020_Q1(E.JumbledEvaluator):

  def __init__(self, courseHome):
    qtypes = [
      E.MCQType(4, 1),         #1
      E.MCQType(4, 1),         #2
      E.MCQType(6, 1),         #3
      E.MCQType(4, 1),         #4
      E.MCQType(5, 1),         #5
      E.MCQType(7, 1),         #6
      E.MCQType(10, 1),         #7
      E.MCQType(5, 1),         #8
      E.MCQType(6, 1),         #9
      E.MCQType(4, 1),         #10
      E.MCQType(4, 1),         #11
      E.MCQType(5, 1),         #12
      E.MCQType(6, 1),         #13
      E.MCQType(6, 1),         #14
      E.MCQType(7, 1),         #15
    ]

    E.JumbledEvaluator.__init__(self, qtypes, courseHome)

if __name__ == "__main__":
#  evaluator = Evaluator_PL2020_Q1("/home/sujit/IIITB/courses/spring2020/PL")
  evaluator = Evaluator_PL2020_Q1("../../../")
  results = evaluator.evaluate()
  for rollNumber in results:
    if(type(results[rollNumber]) == E.Score):
      print(rollNumber, "\t", results[rollNumber].total)
    else:
      print(rollNumber, "\t", results[rollNumber])

  print("total marks = ", evaluator.referenceScore)
