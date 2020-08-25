#!/usr/bin/python3
import sys
import csv
import shutil

shutil.copyfile("../config.py", "config.py")
import config

sys.path.append(config.applicationHome)
import src.evaluator as E

if __name__ == "__main__":
  evaluator = E.JumbledEvaluator           (
    qtypes         = config.items,
    rollNumberFile = config.rollNumberFile )
  results = evaluator.evaluate()
  for rollNumber in results:
    if(type(results[rollNumber]) == E.Score):
      print(rollNumber, "\t", results[rollNumber].total)
    else:
      print(rollNumber, "\t", results[rollNumber])

  print("total marks = ", evaluator.referenceScore)
