#!/usr/bin/python3
import csv

class CSVReader:

  @staticmethod
  def readRNtoQP(fname):
    return list(csv.reader(open(fname, 'r')))

  @staticmethod
  def readAItoQP(fname):
    return list(csv.reader(open(fname, 'r')))

  @staticmethod
  def readAItoIBIFile(fname):
    return list(csv.reader(open(fname, 'r')))

if __name__ == "__main__":
  reader = CSVReader().readAItoQP('/Users/vibhavagarwal/Desktop/evalobj/src/AItoQP.csv')
  print(list(reader))
