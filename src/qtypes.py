class QType:
  def __init__(self, name, n, tm):
    self.name       = name
    self.domainSize = n
    self.totalMarks = float(tm)

class MCQType(QType):
  def __init__(self, name, n, tm):
    QType.__init__(self, name, n, tm)

  def __str__(self):
    return "MCQType(\"" + self.name + "\", " + str(self.domainSize) + ", " + str(self.totalMarks) + ")"

  @property
  def latexTemplate(self):
    s = ""
    s += "\\begin{enumerate}" + "\n"
    for i in range(self.domainSize):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    return s

class MTFQType(QType):
  def __init__(self, name, n1, n2, tm):
    QType.__init__(self, name, n1, tm)
    self.rangeSize = n2

  def __str__(self):
    return "MTFQType(\"" + self.name + "\", " + str(self.domainSize) + ", " + str(self.rangeSize) + ", " + str(self.totalMarks) + ")"

  @property
  def latexTemplate(self):
    return "empty question"
