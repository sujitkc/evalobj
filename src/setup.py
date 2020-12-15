#!/usr/bin/python3

import sys
import json
import os
import shutil
import functools

import utils
import qtypes
from path import Path

class Configuration:
  def __init__(self, configFile):
    with open(configFile) as f:
      data = json.load(f)

    print(data)

    self.applicationHome = Path.applicationHome

    if("course name" in data):
      self.courseName     = data["course name"]
    else:
      self.courseName = ""
    if("course code" in data):
      self.courseCode     = data["course code"]
    else:
      self.courseCode = ""
    if("assessment name" in data):
      self.assessmentName = data["assessment name"]
    else:
      self.assessmentName = ""
    if("assessment type" in data):
      self.assessmentType = data["assessment type"]
    else:
      self.assessmentType = "simple" #default type is simple
    if("assessment home" in data):
      self.assessmentHome  = data["assessment home"]
    else:
      raise Exception("assessment home not specified in configuration file.")
    if("roll number file" in data):
      self.rollNumberFile = data["roll number file"]
    else:
      raise Exception("roll number file not specified in configuration file.")
    if("items" in data):
      self.items = self.readItems(data["items"])
    else:
      self.items = []

    # Configuration specific only to jumbled quizzes.
    if(self.assessmentType == "jumbled"):
      rollNumbers = utils.CSVReader.readRollNumbers(self.rollNumberFile)
      self.numOfAIs = len(rollNumbers)
      if("number of items per assessment instrument" in data):
        self.itemsPerAI = int(data["number of items per assessment instrument"])
      else:
        self.itemsPerAI = len(self.items)

  def readItems(self, itemsData):
    def readItem(itemData):
      name = itemData["name"]
      properties = itemData["properties"]
      options = int(properties["options"])
      marks   = int(properties["marks"])
      question = itemData["question"]
      qtype = properties["qtype"]
      if(properties["qtype"] == "MCQ"):
        item = qtypes.MCQType(name,qtype, options, marks)
      elif(properties["qtype"] == "MTF"):
        rangeSize = int(properties["range"])
        item = qtypes.MTFQType(name,qtype, options, rangeSize, marks)
      elif(properties["qtype"] == "FIB"):
        item = qtypes.FIBQType(name,qtype,marks)
        
      return item

    return [readItem(i) for i in itemsData]

  def __str__(self):
    s = ""
    s += "applicationHome = \"" + self.applicationHome + "\"\n\n"
    s += "import sys" + "\n"

    s += "sys.path.append(applicationHome)" + "\n"
    s += "from src.qtypes import MCQType" + "\n"
    s += "from src.qtypes import MTFQType" + "\n\n"
    s += "from src.qtypes import FIBQType" + "\n\n"
    s += "courseName = \"" + self.courseName + "\"\n"
    s += "courseCode = \"" + self.courseCode + "\"\n"
    s += "assessmentName = \"" + self.assessmentName + "\"\n"
    s += "assessmentHome = \"" + self.assessmentHome + "\"\n"
    s += "rollNumberFile = \"" + self.rollNumberFile + "\"\n"
    stritems = ""
    # for i in self.items:
    #   stritems += i.name + " : " + i.type + " : " + str(i.domainSize) + " : " + str(i.totalMarks) + ","
    stritems = functools.reduce(lambda x, y: x + y + ", ", [str(i) for i in self.items], "")
    s += "items = [" + stritems + "]\n"
    if(self.assessmentType == "jumbled"):
      s += "numOfAIs = " + str(self.numOfAIs) + "\n"
      s += "itemsPerAI = " + str(self.itemsPerAI) + "\n"
    return s

  def generateProject(self):
    # Check the existence of the directories.
    # Create directories: evaluation, submission, item-bank, assessment-
    # instruments, 
    # Create item stubs in item-bank.
    # Generate file config.py (to be imported by all other scripts)

    if(not os.path.exists(self.assessmentHome)):
      print("Assessment home directory " + self.assessmentHome + " not found.")
      sys.exit(1)
    print("Assessment home directory " + self.assessmentHome + " found.")

    if(not os.path.exists(self.rollNumberFile)):
      print("Roll number file " + self.rollNumberFile + " not found.")
      sys.exit(1)
    print("Roll number file " + self.rollNumberFile + " found.")

    evaluationDirectory = self.assessmentHome + "/evaluation/"
    if(not os.path.exists(evaluationDirectory)):
      print("Evaluation directory " + evaluationDirectory + " not found." \
      " Creating ...")
      os.mkdir(evaluationDirectory)
    else:
      print("Evaluation directory " + evaluationDirectory + \
            " found. Doing nothing.")

    if(not os.path.exists(evaluationDirectory + "evaluate.py")):
      print("Copying evaluate.py to " + evaluationDirectory + " ...")
      if(self.assessmentType == "simple"):
        shutil.copyfile(self.applicationHome + "src/boilerplate/evaluate_simple.py",
          evaluationDirectory + "evaluate.py")
      elif(self.assessmentType == "jumbled"):
        shutil.copyfile(self.applicationHome + "src/boilerplate/evaluate_jumbled.py",
          evaluationDirectory + "evaluate.py")

    itemBank = self.assessmentHome + "/item-bank/"
    if(not os.path.exists(itemBank)):
      print("Item bank " + itemBank + " not found. Creating ...")
      os.mkdir(itemBank)
    else:
      print("Item bank " + itemBank + " found. Doing nothing.")

    # generate item stubs
    for i in self.items:
      itemFile = itemBank + i.name + ".tex"
      if(not os.path.exists(itemFile)):
        print("Item file " + itemFile + " not found. Creating ...")
        with open(itemFile, "w") as fout:
          fout.write("\\question\n")
          fout.write("\\label{q:" + self.courseCode + ":" + self.assessmentName \
            + ":" + i.name + "}\n")
          fout.write(i.latexTemplate)
      else:
        print("Item file " + itemFile + " found. Doing nothing.")

    configSrcFile = self.assessmentHome + "config.py"
    if not os.path.exists(configSrcFile):
      print("Configuration source file " + configSrcFile + \
        " not found. Creating ...")
      with open(configSrcFile, "w") as fout:
        fout.write(str(self))
    else:
      print("Configuration source file " + configSrcFile + \
        " found. Doing nothing.")

    assessmentInstrumentDirectory = self.assessmentHome + "/assessment-instruments/"
    if(not os.path.exists(assessmentInstrumentDirectory)):
      print("Assessment instrument directory " + assessmentInstrumentDirectory \
        + " not found. Creating ...")
      os.mkdir(assessmentInstrumentDirectory)
    else:
      print("Assessment instrument directory " + assessmentInstrumentDirectory \
        + " found. Doing nothing.")

    packagesDirectory = self.assessmentHome + "/packages/"
    if(not os.path.exists(packagesDirectory)):
      print("Packages directory " + packagesDirectory \
        + " not found. Creating ...")
      os.mkdir(packagesDirectory)
    else:
      print("Packages directory " + packagesDirectory \
        + " found. Doing nothing.")

      # Copy gen.py
    if(not os.path.exists(self.assessmentHome + "gen.py")):
      print("Copying gen.py to " + self.assessmentHome + " ...")
      if(self.assessmentType == "simple"):
        shutil.copyfile(self.applicationHome + "src/boilerplate/gen_simple.py", self.assessmentHome + \
          "gen.py")
      if(self.assessmentType == "jumbled"):
        shutil.copyfile(self.applicationHome + "src/boilerplate/gen_jumbled.py", self.assessmentHome + \
          "gen.py")

if __name__ == "__main__":
  if(len(sys.argv) != 2):
    print("Please provide the name of the project configuration file in command", \
      "line.")
    sys.exit(1)
  configFile = sys.argv[1]
  print(configFile)
  config = Configuration(configFile)
  print(config)
  config.generateProject()
