#!/usr/bin/python3

import sys
import json
import os
import shutil
import functools

import qtypes

class Configuration:
  def __init__(self, configFile):
    with open(configFile) as f:
      data = json.load(f)

    print(data)

    self.applicationHome = "/home/sujit/IIITB/projects/evalobj/"

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
    if("number of assessment instruments" in data):
      self.numOfAIs = int(data["number of assessment instruments"])
    else:
      self.QperQP = len(self.items)
    if("number of questions per question paper" in data):
      self.QperQP = int(data["number of questions per question paper"])
    else:
      self.QperQP = len(self.items)
    if("number of question papers per assessment instrument" in data):
      self.QPperAI = int(data["number of question papers per assessment instrument"])
    else:
      self.QPperAI = 1

  def readItems(self, itemsData):
    def readItem(itemData):
      name = itemData["name"]
      properties = itemData["properties"]
      options = int(properties["options"])
      marks   = int(properties["marks"])
      if(properties["qtype"] == "MCQ"):
        item = qtypes.MCQType(name, options, marks)
      elif(properties["qtype"] == "MTF"):
        rangeSize = item(properties["range"])
        item = qtypes.MTFType(name, options, rangeSize, marks)
      return item

    return [readItem(i) for i in itemsData]

  def __str__(self):
    s = ""
    s += "applicationHome = \"" + self.applicationHome + "\"\n\n"
    s += "import sys" + "\n"

    s += "sys.path.append(applicationHome)" + "\n"
    s += "from src.qtypes import MCQType" + "\n"
    s += "from src.qtypes import MTFQType" + "\n\n"

    s += "courseName = \"" + self.courseName + "\"\n"
    s += "courseCode = \"" + self.courseCode + "\"\n"
    s += "assessmentName = \"" + self.assessmentName + "\"\n"
    s += "assessmentHome = \"" + self.assessmentHome + "\"\n"
    s += "rollNumberFile = \"" + self.rollNumberFile + "\"\n"
    stritems = functools.reduce(lambda x, y: x + y + ", ", [str(i) for i in self.items], "")
    s += "items = [" + stritems + "]\n"
    s += "numOfAIs = " + str(self.numOfAIs) + "\n"
    s += "QPperAI = " + str(self.QPperAI) + "\n"
    s += "QperQP = " + str(self.QperQP) + "\n"
    return s

  def generateProject(self):
    # Check the existence of the directories.
    # Create directories: evaluation, submission, item-bank, assessment-
    # instruments, question-papers
    # Create item stubs in item-bank.
    # Generate file config.py (to be imported by all other scripts)
    # Copy gen.py to evaluation, gen_pdfs.sh to question-papers

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
      shutil.copyfile(self.applicationHome + "src/evaluate.py",
        evaluationDirectory + "evaluate.py")

    itemBank = self.assessmentHome + "/item-bank/"
    if(not os.path.exists(itemBank)):
      print("Item bank " + itemBank + " not found. Creating ...")
      os.mkdir(itemBank)
    else:
      print("Item bank " + itemBank + " found. Doing nothing.")

    assessmentInstrumentDirectory = self.assessmentHome + "/assessment-instruments/"
    if(not os.path.exists(assessmentInstrumentDirectory)):
      print("Assessment instrument directory " + assessmentInstrumentDirectory \
        + " not found. Creating ...")
      os.mkdir(assessmentInstrumentDirectory)
    else:
      print("Assessment instrument directory " + assessmentInstrumentDirectory \
        + " found. Doing nothing.")

    questionPapersDirectory = self.assessmentHome + "question-papers/"
    if(not os.path.exists(questionPapersDirectory)):
      print("Question papers directory " + questionPapersDirectory + \
        " not found. Creating ...")
      os.mkdir(questionPapersDirectory)
    else:
      print("Question papers directory " + questionPapersDirectory + \
        " found. Doing nothing.")

    # Copy gen_pdf.sh
    if(not os.path.exists(questionPapersDirectory + "gen_pdf.sh")):
      print("Copying gen_pdf.sh to " + questionPapersDirectory + " ...")
      shutil.copyfile(self.applicationHome + "src/gen_pdf.sh",
        questionPapersDirectory + "gen_pdf.sh")

    # Copy gen.py
    if(not os.path.exists(self.assessmentHome + "gen.py")):
      print("Copying gen.py to " + self.assessmentHome + " ...")
      shutil.copyfile(self.applicationHome + "src/gen.py", self.assessmentHome + \
        "gen.py")

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
    if(not os.path.exists(configSrcFile)):
      print("Configuration source file " + configSrcFile + \
        " not found. Creating ...")
      with open(configSrcFile, "w") as fout:
        fout.write(str(self))
    else:
      print("Configuration source file " + configSrcFile + \
        " found. Doing nothing.")

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
