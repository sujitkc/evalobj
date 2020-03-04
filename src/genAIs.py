#!/usr/bin/python3
import random
import functools

class AIGenerator:
  def __init__(self,
      items,
      numOfQuestions,
      numOfAIs,
      s = "../examples/simple/quizzes/q1/item-bank/",
      d = "../examples/simple/quizzes/q1/assessment-instruments/",
      aitoibi_file = "AItoIBI.csv"
  ):
    self.items          = items
    self.numOfQuestions = numOfQuestions
    self.numOfAIs       = numOfAIs
    self.src_dir        = s
    self.dest_dir       = d
    self.aitoibi_file   = aitoibi_file

  # Generate a single headless assessment instrument. It is a LaTeX file with the 
  # initial part missing.
  def genAI(self, fout):
    with open("b2.tex", "r") as fin:
      foot = fin.read()
    allItems = self.items[:]
    random.shuffle(allItems)
    items = allItems[:self.numOfQuestions]
    for item in items:
      with open(self.src_dir + item + ".tex", "r") as fin:
        question = "\n" + fin.read()
      fout.write(question)
    fout.write(foot)
    return items

  # Generate all assessment instruments.
  def genAIs(self):
    self.AItoIBI = {}
    for i in range(1, self.numOfAIs + 1):
      AI = "ai" + str(i)
      with open(self.dest_dir + AI + ".tex", "w") as fout:
        self.AItoIBI[AI] = self.genAI(fout)

  def writeAItoIBI(self):
    with open(self.aitoibi_file, "w") as fout:
      for ai in self.AItoIBI:
        row = ai + "," + functools.reduce(lambda x, y: x + "," + y, self.AItoIBI[ai][1:], self.AItoIBI[ai][0])
        fout.write(row + "\n")

if __name__ == "__main__":
  items = ["item" + str(qnum) for qnum in range(1, 16)]
  aig = AIGenerator(items, 5, 3)
  aig.genAIs()
  aig.writeAItoIBI()
