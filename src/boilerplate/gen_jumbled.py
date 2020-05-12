#!/usr/bin/python3
import random
import functools
import sys
import shutil

import config
sys.path.append(config.applicationHome)
from src.genAIs import AIGenerator
import src.genQPs as Q
import src.utils

if __name__ == "__main__":
  itemNames = [ i.name for i in config.items ]
  rollNumbers = src.utils.CSVReader.readRollNumbers(config.rollNumberFile)
  aig = AIGenerator(
          applicationHome = config.applicationHome,
          courseName      = config.courseName,
          courseCode      = config.courseCode,
          assessmentName  = config.assessmentName,
          items           = itemNames,
          numOfItems      = config.itemsPerAI,
          numOfAIs        = len(rollNumbers))
  aig.genAIs()
  aig.writeAItoIBI()
  shutil.copyfile(config.applicationHome + "src/boilerplate/gen_pdf.sh",
     config.assessmentHome + "assessment-instruments/gen_pdf.sh")
