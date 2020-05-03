#!/usr/bin/python3
import random
import functools

class AIGenerator:
  def __init__(self,
      applicationHome,
      courseName,
      courseCode,
      assessmentName,
      items,
      numOfItems,
      numOfAIs,
      s = "item-bank/",
      d = "assessment-instruments/",
      aitoibi_file = "AItoIBI.csv"
  ):
    self.applicationHome = applicationHome
    self.courseName      = courseName
    self.courseCode      = courseCode
    self.assessmentName  = assessmentName
    self.items           = items
    self.numOfItems      = numOfItems
    self.numOfAIs        = numOfAIs
    self.src_dir         = s
    self.dest_dir        = d
    self.aitoibi_file    = aitoibi_file

    with open(self.applicationHome + "src/h1.tex", "r") as fin:
      self.h1 = fin.read()
    with open(self.applicationHome + "src/h1.1.tex", "r") as fin:
      self.h1_1 = fin.read()
    with open(self.applicationHome + "src/h2.tex", "r") as fin:
      self.h2 = fin.read()
    with open(self.applicationHome + "src/h3.tex", "r") as fin:
      self.h3 = fin.read()
    with open(self.applicationHome + "src/b2.tex", "r") as fin:
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
  def genAI(self, aiCode, fout):
    title = "\\title{" + self.courseName + "\\\\" +  self.assessmentName + "}\n"

    allItems = self.items[:]
    random.shuffle(allItems)
    items = allItems[:self.numOfItems]
    stritems = ""
    for item in items:
      item = "\n" + "\\input{../" + self.src_dir + item + ".tex}" + "\n"
      stritems += item
    ai = self.h1 + title + self.h1_1 + aiCode + self.h2 + self.responseTable + \
           self.h3 + stritems + self.footer
    fout.write(ai)
    return items

  # Generate all assessment instruments.
  def genAIs(self):
    self.AItoIBI = {}
    for i in range(1, self.numOfAIs + 1):
      aiCode = "ai" + str(i)
      with open(self.dest_dir + aiCode + ".tex", "w") as fout:
        self.AItoIBI[aiCode] = self.genAI(aiCode, fout)

  def writeAItoIBI(self):
    with open(self.aitoibi_file, "w") as fout:
      for ai in self.AItoIBI:
        row = ai + "," + functools.reduce(
                lambda x, y: x + "," + y,
                self.AItoIBI[ai][1:], self.AItoIBI[ai][0])
        fout.write(row + "\n")
