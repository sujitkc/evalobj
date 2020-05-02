#!/usr/bin/python3
import csv

class CSVReader:

  # Procedure to read roll numbers from CSV file
  @staticmethod
  def readRollNumbers(fname):
    reader = csv.reader(open(fname, 'r'))
    rows = list(reader)
    rows.pop(0)
    return [row[0] for row in rows]

  @staticmethod
  def readRNtoAI(fname):
    return list(csv.reader(open(fname, 'r')))

  @staticmethod
  def readAItoIBIFile(fname):
    return list(csv.reader(open(fname, 'r')))

if __name__ == "__main__":
  reader = CSVReader().readAItoQP('/Users/vibhavagarwal/Desktop/evalobj/src/AItoQP.csv')
  print(list(reader))
