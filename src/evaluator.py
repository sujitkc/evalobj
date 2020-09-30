#!/usr/bin/python3
import sys
import os
import csv
import string
import subprocess
import functools
import traceback
from src.path import Path
import src.utils as utils
import src.qtypes as qtypes


sys.path.append(Path.applicationHome)
  
class QuestionPaper:
  def __init__(self, questions, qtypes):
    self.questions = questions
    self.questionTypes = qtypes

  def evaluate(self, answers, rollNumber="reference"):
    itemScores = []
    for i in range(len(self.questionTypes)):
      itemScore = 0.0
      try:
        question = self.questions[i]
        answer = answers.answers[i]
        if(question != None):
          itemScore = question.evaluate(answer)
        else:
          itemScore = 0
      except IncompatibleLengthError:
        print("Could not evaluate item " + str(i + 1) + " for " + rollNumber)
        raise
      itemScores.append(itemScore)

    return Score(rollNumber, itemScores)

  def __str__(self):
    return "Question Paper(" + str([str(q) for q in self.questions]) + ")"

class AnswerSheet:
  def __init__(self, answers):
    self.answers = answers

  def __str__(self):
    return "Answer Sheet(" + str([str(a) for a in self.answers]) + ")"

class Reader:
  def __init__(self, qtypes):
    self.questionTypes = qtypes

  def __readContents__(self, fileName):
    if(not os.path.isfile(fileName)):
      print(fileName + ": file does not exist.")
      raise FileNotExistsError(fileName)
    with open(fileName, "r") as ifile:
      csvContents = csv.reader(ifile)
      trimmedContents = []
      rowNum = 0
      rows = list(csvContents)
    while(rowNum < len(rows)):
      row = rows[rowNum]
      trimmedRow = [cell for cell in row if cell != ""]
      if(len(trimmedRow) != 0):
        parsedRow = self.parseRow(trimmedRow, rowNum)
        trimmedContents.append(parsedRow)
      else:
        trimmedContents.append(None)
      rowNum += 1
    return trimmedContents

  def parseRow(self, row, i):

    qtype = self.questionTypes[i]
    className = qtype.__class__.__name__
    className = className.replace("QType", "")
    try:
      method = "parseQ" + className
      return getattr(self, method)(row, qtype)
    except:
      return None

  @staticmethod
  def parseMTFRow(row):
    def getChoices(ans):
      splitAns = ans.split(",")
      return [int(s.strip()) for s in splitAns]

    return [getChoices(cell) for cell in row]

class ReferenceReader(Reader):
  def __init__(self, qtypes):
    Reader.__init__(self, qtypes)

  @staticmethod
  def parseMCQ(row, qtype):
    return MCQuestion([int(cell) for cell in row], qtype)

  @staticmethod
  def parseMTF(row, qtype):
    mtfrow = Reader.parseMTFRow(row)
    mcqs = [ReferenceReader.parseMCQ(cell, qtypes.MCQType("MCQ", qtype.rangeSize, qtype.totalMarks / qtype.domainSize )) for cell in mtfrow]
    return MTFQuestion(mcqs, qtype)

  def readQuestionPaper(self, fileName):
    return QuestionPaper(self.__readContents__(fileName), self.questionTypes)
 
class AnswerReader(Reader):
  def __init__(self, qtypes):
    Reader.__init__(self, qtypes)

  @staticmethod
  def parseMCQ(row, qtype):
    return [int(cell) for cell in row]

  @staticmethod
  def parseMTF(row, qtype):
    return Reader.parseMTFRow(row)

  def readAnswers(self, fileName):
    return AnswerSheet(self.__readContents__(fileName))

class IncompatibleLengthError(Exception):
  def __init__(self, e, a):
    self.expected = e
    self.answer   = a

  def __str__(self):
    return "IncompatibleLengthError(expected = " + str(self.expected) + \
             ", answer = " + str(self.answer) + ")"

class FileNotExistsError(Exception):
  def __init__(self, filename):
    Exception.__init__(self, "File " + filename + " doesn't exist.")

class MappingNotFoundError(Exception):
  def __init__(self, mp, val):
    if mp == 'RNtoQP':
      st = "Roll Number: " + str(val) + "."
    elif mp == 'AItoIBI':
      st = "AI: " + str(val) + "."
    elif mp == 'AItoQP':
      st = "Question Paper: " + str(val) + "."
    Exception.__init__(self, mp + "mapping not found for " + st)

class Question:
  def __init__(self, expected, qtype):
    self.expected = expected
    self.questionType = qtype

  @property
  def domainSize(self):
    return self.questionType.domainSize

class MCQuestion(Question):
  def __init__(self, expected, qtype):
    Question.__init__(self,
      expected = expected,
      qtype = qtype)
    self.expectedChoices = self.convert(self.expected)

  # Function to translate [1, 3] to [True, False, True, False, False]
  def convert(self, indices):
    choices = [False] * self.domainSize
    for i in indices:
      choices[int(i) - 1] = True # the - 1 is to deal with the offset of index.
    return choices

  # Given an expected answer and output answer, compare choice by choice.
  # The score is out of 1. It is the fraction of choices that match to the
  # total number of choices.
  def score(self, answer):
    if(len(self.expectedChoices) != len(answer)):
      raise IncompatibleLengthError(len(self.expectedChoices), len(answer))
    score = 0

    zipped = zip(self.expectedChoices, answer)
    for (a, b) in zipped:
      if(a and b):
        score += 1
    print(self.expectedChoices)
    print("test")
    print(answer)
    return float(score) / float(len(self.expected))
    #return float(score) / float(self.domainSize)

  def evaluate(self, answer):
    expectedChoices = self.convert(self.expected)
    if(answer == None):
      return 0
    answerChoices = self.convert(answer)

    if(0 not in answer):
      return self.score(answerChoices) * self.questionType.totalMarks
    else:
      return 0

  def __str__(self):
    return "MCQ(" + str(self.domainSize) + ", " + str(self.expected) + ")"

class MTFQuestion(Question):
  def __init__(self, e, qtype):
    Question.__init__(self, e, qtype)

  @property
  def rangeSize(self):
    return self.questionType.rangeSize

  def evaluate(self, answer):
    def getChoices(ans):
      splitAns = ans.split(",")
      return [int(s.strip()) for s in splitAns]

    if(len(self.expected) != self.domainSize):
      raise IncompatibleLengthError(len(self.expected), len(answer))
    if(len(answer) != self.domainSize):
      raise IncompatibleLengthError(len(self.expected), len(answer))

    zipped = zip(self.expected, answer)
    return sum([q.evaluate(a) for (q, a) in zipped]) * \
            self.questionType.totalMarks

  def __str__(self):
    return "MTF(" + str([str(q) for q in self.expected]) + \
      ", " + str(self.domainSize) + ", " + str(self.rangeSize) + ")"

# Class representing the score of an individual student.
class Score:
  def __init__(self, rollNumber, scores):
    self.rollNumber = rollNumber
    self.itemScores = scores

  @property
  def total(self):
    return functools.reduce(lambda x, y: x + y, self.itemScores, 0.0)

  def __str__(self):
    s = "roll number: " + self.rollNumber + "\n"
    s += "item scores: " + str(self.itemScores) + "\n"
    s += "total score: " + str(self.total) + "\n"
    return s

class Evaluator:
  def __init__(self,
      qtypes,
      rollNumberFile,
      submissions_dir = "submissions/"):
    self.qtypes = qtypes
    self.rollNumberFile = rollNumberFile
    self.submissions_dir = submissions_dir
    self.rollNumbers = utils.CSVReader.readRollNumbers(self.rollNumberFile)
    self.qreader = ReferenceReader(self.qtypes)
    self.questionPaper = self.qreader.readQuestionPaper("theory_answers.csv")
    self.areader = AnswerReader(self.qtypes)
    reference = self.areader.readAnswers("theory_answers.csv")
    self.referenceScore = self.questionPaper.evaluate(reference)

  @property
  def totalMarks(self):
    return self.referenceScore.total

  def getAnswerSheet(self, ansfile, rollNumber):
    return self.areader.readAnswers(ansfile)

  def __evaluate__(self, rollNumber):
    print("evaluating ", rollNumber, " ...")
    try:
      ansfile = self.submissions_dir + rollNumber + "/response/theory_answers.csv"
      if(not os.path.isfile(ansfile)):
        raise FileNotExistsError(ansfile)
      answerSheet = self.getAnswerSheet(ansfile, rollNumber)
      return self.questionPaper.evaluate(answerSheet, rollNumber)
    except FileNotExistsError:
      return Score(rollNumber, [0.0] * 55)
    except IncompatibleLengthError as e:
      return e
    except Exception as e:
      traceback.print_exc(file=sys.stdout)
      return e

  def evaluate(self):
    results = {}

    for rollNumber in self.rollNumbers:
      results[rollNumber] = self.__evaluate__(rollNumber)
    with open("result.csv", "w") as fout:
      for rollNumber in results:
        row = rollNumber
        marks = functools.reduce(lambda x, y: x + ", " + str(y), results[rollNumber].itemScores, "")
        #row += marks
        row += ", " + str(results[rollNumber].total) + "\n"
        fout.write(row)
    return results

# Evaluator with jumbling of questions
class JumbledEvaluator(Evaluator):
  def __init__(
      self,
      qtypes,
      rollNumberFile,
      AItoIBIFile=Path.applicationHome+"test/python_quiz/AItoIBI.csv"):
    self.AItoIBI = utils.CSVReader.readAItoIBIFile(AItoIBIFile)
    Evaluator.__init__(self, qtypes, rollNumberFile)

  def rearrange(self, ai, iresponses):
    itemBankLength = len(self.qtypes)
    oresponses = [[0]] * itemBankLength
    ai2ibi = []
    try:
      for ai_ibi_map in self.AItoIBI:
        if ai in ai_ibi_map:
          ai2ibi = ai_ibi_map[1:]
    except MappingNotFoundError as e:
      e('AItoIBI',ai)
    ai2ibi = [i.split('item')[-1] for i in ai2ibi]
    for i in range(len(ai2ibi)):
      oresponses[int(ai2ibi[i]) - 1] = iresponses.answers[i]
    return AnswerSheet(oresponses)

  # This Answer reader reads the jumbled answers from the submitted response
  # from the roll number, and rearranges it by
  # extracting the assessment instrument corresponding to the given 
  # roll number (which is nothing but the roll number itself)
  # extracting the item to item bank item for each item and rearranging the
  # answer sheet as per that.
  # This answer sheet is returned.
  def getAnswerSheet(self, ansfile, rollNumber):
    jumbledResponses = Evaluator.getAnswerSheet(self, ansfile, rollNumber)
    return self.rearrange(rollNumber, jumbledResponses)
