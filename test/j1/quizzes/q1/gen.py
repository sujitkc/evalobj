#!/usr/bin/python3
import random
import functools
import sys

import config

sys.path.append(config.applicationHome)
from src.genAIs import AIGenerator
import src.genQPs as Q

if __name__ == "__main__":
  itemNames = [ i.name for i in config.items ]
  aig = AIGenerator(config.applicationHome, items=itemNames, numOfQuestions=config.QperQP, numOfAIs=config.numOfAIs)
  aig.genAIs()
  aig.writeAItoIBI()

  AIs = ["ai" + str(qnum) for qnum in range(1, config.numOfAIs + 1)]
  qpg = Q.QPGenerator(
          applicationHome=config.applicationHome,
          course=config.courseCode, 
          assessment=config.assessmentName,
          AIs=AIs,
          numOfQuestions=config.QperQP,
          QPperAI=config.QPperAI  )
  qpg.genQPs()
  print(qpg.AItoQP)
  qpg.writeAItoQP()
