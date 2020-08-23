#!/usr/bin/python3
import os
import random
import functools
from src.boilerplate.gui import GUIGeneartor


class AIGenerator:
  def __init__(self,
      applicationHome,
      courseName,
      courseCode,
      assessmentName,
      items,
      numOfItems,
      rollNumbers,
      numOfAIs = -1,
      itemBankDir = "../item-bank/",
      AIDir = "assessment-instruments/",
      aitoibi_file = "AItoIBI.csv"
  ):
    self.applicationHome = applicationHome
    self.courseName      = courseName
    self.courseCode      = courseCode
    self.assessmentName  = assessmentName
    self.items           = items
    self.numOfItems      = numOfItems
    self.rollNumbers     = rollNumbers
    if(numOfAIs == -1):
      self.numOfAIs      = len(rollNumbers)
    else:
      self.numOfAIs      = numOfAIs
    self.itemBankDir     = itemBankDir
    self.AIDir           = AIDir
    self.aitoibi_file    = aitoibi_file

    with open(self.applicationHome + "src/tex/h1.tex", "r") as fin:
      self.h1 = fin.read()
    with open(self.applicationHome + "src/tex/h1.1.tex", "r") as fin:
      self.h1_1 = fin.read()
    with open(self.applicationHome + "src/tex/h2.tex", "r") as fin:
      self.h2 = fin.read()
    with open(self.applicationHome + "src/tex/h3.tex", "r") as fin:
      self.h3 = fin.read()
    with open(self.applicationHome + "src/tex/b2.tex", "r") as fin:
      self.footer = fin.read()
    self.responseTable = self.getResponseTable()

  def getResponseTable(self):
    tableHeader = "\\begin{center}\n" + \
                  "\\textbf{Response Table}\n" + \
                  "\\begin{tabular}{| l | p{1cm} | p{1cm} | p{1cm} | p{1cm} |" + \
                  " p{1cm} | p{1cm} | p{1cm} | p{1cm} | p{1cm} | p{1cm} |}\n" + \
                  "\\hline"

    tableFooter = "\\end{tabular}\n" + \
                  "\\end{center}"
    lines = ""
    for itemNum in range(1, self.numOfItems + 1):
      line = "\\cellcolor{Gray!10}" + str(itemNum) + "& & & & & & & & & & \\\\\n" + \
             "\hline\n"
      lines += line

    return tableHeader + lines + tableFooter


  # Generate a single headless assessment instrument. It is a LaTeX file with the 
  # initial part missing.
  def genAI(self, aiCode, fout, config):
    title = "\\title{" + self.courseName + "\\\\" +  self.assessmentName + "}\n"

    allItems = self.items[:]
    self.shuffle(allItems)
    items = allItems[:self.numOfItems]
    stritems = ""
    for item in items:
      itemFileName = self.itemBankDir + "/" + item + ".tex"
      item = "\n" + "\\input{" + itemFileName + "}" + "\n"
      stritems += item
    ai = self.h1 + title + self.h1_1 + aiCode + self.h2 + self.responseTable + \
           self.h3 + stritems + self.footer
    fout.write(ai)
    gui = GUIGeneartor(items, aiCode, config)
    return items

  # Generate all assessment instruments.
  def genAIs(self, config):
    self.AItoIBI = {}
    aiCodes = self.generateAICodes()
    for aiCode in aiCodes:
      texFile = self.AIDir + aiCode + ".tex"
      with open(texFile, "w") as fout:
        self.AItoIBI[aiCode] = self.genAI(aiCode, fout, config)
      packageDirectory = "packages/" + aiCode
      if(not os.path.exists(packageDirectory)):
        os.mkdir(packageDirectory)
      os.system("pdflatex -output-directory=" +
                  packageDirectory + " " + texFile)

  def writeAItoIBI(self):
    with open(self.aitoibi_file, "w") as fout:
      for ai in self.AItoIBI:
        row = ai + "," + functools.reduce(
                lambda x, y: x + "," + y,
                self.AItoIBI[ai][1:], self.AItoIBI[ai][0])
        fout.write(row + "\n")

class SimpleAIGenerator(AIGenerator):

  def __init__(self,
      applicationHome,
      courseName,
      courseCode,
      assessmentName,
      items,
      rollNumbers,
      itemBankDir,
      AIDir
  ):
    AIGenerator.__init__(self,
      applicationHome = applicationHome,
      courseName      = courseName,
      courseCode      = courseCode,
      assessmentName  = assessmentName,
      items           = items,
      numOfItems      = len(items),
      numOfAIs        = 1,
      rollNumbers     = rollNumbers,
      itemBankDir     = itemBankDir,
      AIDir           = AIDir
    )

  def generateAICodes(self):
    return ["assessment-instrument"]

  def shuffle(self, allItems):
     pass

class JumbledAIGenerator(AIGenerator):

  def __init__(self,
      applicationHome,
      courseName,
      courseCode,
      assessmentName,
      items,
      numOfItems,
      rollNumbers,
      itemBankDir,
      AIDir
  ):
    AIGenerator.__init__(self,
      applicationHome = applicationHome,
      courseName      = courseName,
      courseCode      = courseCode,
      assessmentName  = assessmentName,
      items           = items,
      numOfAIs        = 1,
      numOfItems      = numOfItems,
      rollNumbers     = rollNumbers,
      itemBankDir     = itemBankDir,
      AIDir           = AIDir
    )

  def generateAICodes(self):
    return self.rollNumbers

  def shuffle(self, allItems):
    random.shuffle(allItems)
