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
    # Create directories: evaluation, submission, item-bank, assessment-instruments, question-papers
    # Create item stubs in item-bank.
    # Generate file config.py (to be imported by all other scripts)
    # Copy files: genAIs.py, genQPs.py

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
      print("Evaluation directory " + evaluationDirectory + " not found. Creating ...")
      os.mkdir(evaluationDirectory)
    else:
      print("Evaluation directory " + evaluationDirectory + " found. Doing nothing.")

    itemBank = self.assessmentHome + "/item-bank/"
    if(not os.path.exists(itemBank)):
      print("Item bank " + itemBank + " not found. Creating ...")
      os.mkdir(itemBank)
    else:
      print("Item bank " + itemBank + " found. Doing nothing.")

    assessmentInstrumentDirectory = self.assessmentHome + "/assessment-instruments/"
    if(not os.path.exists(assessmentInstrumentDirectory)):
      print("Assessment instrument directory " + assessmentInstrumentDirectory + " not found. Creating ...")
      os.mkdir(assessmentInstrumentDirectory)
    else:
      print("Assessment instrument directory " + assessmentInstrumentDirectory + " found. Doing nothing.")

    questionPapersDirectory = self.assessmentHome + "question-papers/"
    if(not os.path.exists(questionPapersDirectory)):
      print("Question papers directory " + questionPapersDirectory + " not found. Creating ...")
      os.mkdir(questionPapersDirectory)
    else:
      print("Question papers directory " + questionPapersDirectory + " found. Doing nothing.")
    print("Copying gen_pdf.sh to " + questionPapersDirectory + " ...")

    if(not os.path.exists(questionPapersDirectory + "gen_pdf.sh")):
      print("Copying gen_pdf.sh to " + questionPapersDirectory + " ...")
      shutil.copyfile(self.applicationHome + "src/gen_pdf.sh", questionPapersDirectory + "gen_pdf.sh")

    if(not os.path.exists(self.assessmentHome + "gen.py")):
      print("Copying gen.py to " + self.assessmentHome + " ...")
      shutil.copyfile(self.applicationHome + "src/gen.py", self.assessmentHome + "gen.py")

    # generate item stubs
    for i in self.items:
      itemFile = itemBank + i.name + ".tex"
      if(not os.path.exists(itemFile)):
        print("Item file " + itemFile + " not found. Creating ...")
        with open(itemFile, "w") as fout:
          fout.write("\\question\n")
          fout.write("\\label{q:" + self.courseCode + ":" + self.assessmentName + ":" + i.name + "}\n")
      else:
        print("Item file " + itemFile + " found. Doing nothing.")

    source_genAIsFile = self.applicationHome + "genAIs.py"
    source_genQPsFile = self.applicationHome + "genQPs.py"
    destination_genAIsFile = self.assessmentHome + "genAIs.py"
    destination_genQPsFile = self.assessmentHome + "genQPs.py"

    if(not os.path.exists(destination_genAIsFile)):
      print(destination_genAIsFile + " not found. Copying ...")
      shutil.copyfile(source_genAIsFile, destination_genAIsFile)

    if(not os.path.exists(destination_genQPsFile)):
      print(destination_genQPsFile + " not found. Copying ...")
#      shutil.copyfile(source_genQPsFile, destination_genQPsFile)
      self.gen_genQPs(destination_genQPsFile)

    configSrcFile = self.assessmentHome + "config.py"
    if(not os.path.exists(configSrcFile)):
      print("Configuration source file " + configSrcFile + " not found. Creating ...")
      with open(configSrcFile, "w") as fout:
        fout.write(str(self))
    else:
      print("Configuration source file " + configSrcFile + " found. Doing nothing.")

  def gen_genAIs(self, fname):
    text = "#!/usr/bin/python3" + "\n" +                                  \
      "import random" + "\n" +                                            \
      "import functools" + "\n" +                                         \
      "import sys" + "\n" +                                               \
      "sys.path.append(\"/home/sujit/IIITB/projects/evalobj/\")" + "\n" + \
      "from src.genAIs import AIGenerator" + "\n" +                       \
      "import config" + "\n\n" +                                          \
      "if __name__ == \"__main__\":" + "\n" +                             \
      "  itemNames = [\"ai\" + str(qnum) for qnum in range(1," +              \
      str(len(self.items)) +                                              \
      ")]" + "\n" +                                                       \
      "  qpg = Q.QPGenerator(\"" +                                        \
      self.courseName +                                                   \
      "\", \"" +                                                          \
      self.assessmentName +                                               \
      "\", AIs, numOfQuestions=" +                                        \
      str(self.QperQP) +                                                  \
      ", QPperAI=" +                                                      \
      str(self.QPperAI) +                                                 \
      "  )" + "\n" +                                                      \
      "  qpg.genQPs()" + "\n" +                                           \
      "  print(qpg.AItoQP)" + "\n" +                                      \
      "  qpg.writeAItoQP()" + "\n"
    with open(fname, "w") as fout:
      fout.write(text)

  def gen_genQPs(self, fname):
    text = "#!/usr/bin/python3\n" +                                       \
      "sys.path.append(\"/home/sujit/IIITB/projects/evalobj/\")" + "\n" + \
      "import src.qpgen as Q" + "\n" +                                    \
      "import config" + "\n" +                                            \
      "if __name__ == \"__main__\":" + "\n" +                             \
      "  AIs = [\"ai\" + str(qnum) for qnum in range(1," +                \
      str(len(self.items)) +                                              \
      ")]" + "\n" +                                                       \
      "  qpg = Q.QPGenerator(\"" +                                        \
      self.courseName +                                                   \
      "\", \"" +                                                          \
      self.assessmentName +                                               \
      "\", AIs, numOfQuestions=" +                                        \
      str(self.QperQP) +                                                  \
      ", QPperAI=" +                                                      \
      str(self.QPperAI) +                                                 \
      "  )" + "\n" +                                                      \
      "  qpg.genQPs()" + "\n" +                                           \
      "  print(qpg.AItoQP)" + "\n" +                                      \
      "  qpg.writeAItoQP()" + "\n"
    with open(fname, "w") as fout:
      fout.write(text)

if __name__ == "__main__":
  if(len(sys.argv) != 2):
    print("Please provide the name of the project configuration file in command line.")
    sys.exit(1)
  configFile = sys.argv[1]
  print(configFile)
  config = Configuration(configFile)
  print(config)
  config.generateProject()
