#!/usr/bin/python3
import random
import functools
import sys
import shutil

import config
sys.path.append(config.applicationHome)
from src.genAIs import JumbledAIGenerator
import src.utils

if __name__ == "__main__":
  itemNames = [ i.name for i in config.items ]
  rollNumbers = src.utils.CSVReader.readRollNumbers(config.rollNumberFile)
  aig = JumbledAIGenerator(
          applicationHome = config.applicationHome,
          courseName      = config.courseName,
          courseCode      = config.courseCode,
          assessmentName  = config.assessmentName,
          items           = itemNames,
          numOfItems      = config.itemsPerAI,
          rollNumbers     = rollNumbers,
          itemBankDir      = config.assessmentHome + "/item-bank/",
          AIDir           = config.assessmentHome + "assessment-instruments/"
  )
  aig.genAIs(config.items)
  aig.writeAItoIBI()
