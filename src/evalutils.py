import csv

class RollnumberReader:
  def __init__(self, courseHome):
    self.courseHome = courseHome

  # Procedure to read roll numbers from CSV file
  def readRollNumbers(self):
    reader = csv.reader(open(self.courseHome + "/class.csv", 'r'))
    rows = list(reader)
    rows.pop(0)
    return [row[0] for row in rows]
