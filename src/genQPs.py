#!/usr/bin/python3
import random
import functools

class QPGenerator:
  def __init__(self,
      applicationHome,
      course,
      assessment,
      AIs, # assessment instruments
      numOfQuestions,
      QPperAI,
      AI_dir = "assessment-instruments/",
      QP_dir = "question-papers/",
      aitoqp_file = "AItoQP.csv"
  ):
    self.applicationHome = applicationHome
    self.course          = course
    self.assessment      = assessment
    self.AIs             = AIs
    self.numOfQuestions  = numOfQuestions
    self.QPperAI         = QPperAI
    self.AI_dir          = AI_dir
    self.QP_dir          = QP_dir
    self.aitoqp_file     = aitoqp_file

    # Generate assessment instrument to question paper map.
    self.AItoQP = {}
    qp_nums = list(range(1, len(self.AIs) * self.QPperAI + 1))
    random.shuffle(qp_nums)
    qp_num = 0
    for ai in self.AIs:
      self.AItoQP[ai] = []
      for i in range(QPperAI):
        self.AItoQP[ai].append(qp_nums[qp_num])
        qp_num += 1

    with open(self.applicationHome + "src/h1.tex", "r") as fin:
      self.h1 = fin.read()
    with open(self.applicationHome + "src/h1.1.tex", "r") as fin:
      self.h1_1 = fin.read()
    with open(self.applicationHome + "src/h2.tex", "r") as fin:
      self.h2 = fin.read()
    with open(self.applicationHome + "src/h3.tex", "r") as fin:
      self.h3 = fin.read()
  #   self.responseTable = self.getResponseTable()

  # def getResponseTable(self):
  #   tableHeader = "\\begin{center}\n" + \
  #                 "\\textbf{Response Table}\n" + \
  #                 "\\begin{tabular}{| l | p{1cm} | p{1cm} | p{1cm} | p{1cm} |" + \
  #                 " p{1cm} | p{1cm} | p{1cm} | p{1cm} | p{1cm} | p{1cm} |}\n" + \
  #                 "\\hline"

  #   tableFooter = "\\end{tabular}\n" + \
  #                 "\\end{center}"
  #   lines = ""
  #   for qnum in range(1, self.numOfQuestions + 1):
  #     line = "\\cellcolor{Gray!10}" + str(qnum) + "& & & & & & & & & & \\\\\n" + \
  #            "\hline\n"
  #     lines += line

  #   return tableHeader + lines + tableFooter

  # Generate a single question paper.
  def genQP(self, ai, qp_num):
    title = "\\title{" + self.course + "\\\\" +  self.assessment + "}\n"

    with open(self.AI_dir + ai + ".tex", "r") as fin:
      aitext = fin.read()
      qp = self.h1 + title + self.h1_1 + str(qp_num) + self.h2 + self.h3 + \
            aitext
    with open(self.QP_dir + "qp" + str(qp_num) + ".tex", "w") as fout:
      fout.write(qp)

  # Generate all question papers.
  def genQPs(self):
    for ai in self.AIs:
      for qp_num in self.AItoQP[ai]:
        self.genQP(ai, qp_num)

  # Write the assessment instrument to question paper map to CSV file.
  def writeAItoQP(self):
    with open(self.aitoqp_file, "w") as fout:
      for ai in self.AItoQP:
        row = ai + "," + \
                functools.reduce(
                  lambda x, y: x + "," + str(y),
                  self.AItoQP[ai][1:],
                  str(self.AItoQP[ai][0])
                )
        fout.write(row + "\n")

if __name__ == "__main__":
  AIs = ["ai" + str(qnum) for qnum in range(1, 4)]
  qpg = QPGenerator("Programming Languages", "Quiz 1", AIs, numOfQuestions=5, QPperAI=2)
  qpg.genQPs()
  print(qpg.AItoQP)
  qpg.writeAItoQP()
