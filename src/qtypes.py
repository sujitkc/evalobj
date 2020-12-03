class QType:
  def __init__(self, name,t,n, tm):
    self.name       = name
    self.type       = t
    self.domainSize = n
    self.totalMarks = float(tm)
    print(self.name)

class MCQType(QType):
  def __init__(self, name, t, n, tm):
    QType.__init__(self, name, t, n, tm)

  def __str__(self):
    return "MCQType(\"" + self.name + "\"," +"\""+str(self.type) + "\"" + "," +str(self.domainSize) + ", " + str(self.totalMarks) + ")"

  @property
  def latexTemplate(self):
    s = ""
    s += "\\begin{enumerate}" + "\n"
    for i in range(self.domainSize):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    return s

class MTFQType(QType):
  def __init__(self, name, t, n1, n2, tm):
    QType.__init__(self, name, t, n1, tm)
    self.rangeSize = n2

  def __str__(self):
    return "MTFQType(\"" + self.name + "\"," +"\""+str(self.type) + "\"" + ","+ str(self.domainSize) + ", " + str(self.rangeSize) + ", " + str(self.totalMarks) + ")"

  @property
  def latexTemplate(self):
    s = "\n"
    s += "Match the following:" + "\n"
    s += "\\begin{center}" + "\n"
    s += "\\begin{tabular}{c@{\\hspace{1cm}}c}" + "\n"
    s += "\\begin{minipage}{0.40\\textwidth}" + "\n"
    s += "\\begin{enumerate}" + "\n"
    for i in range(self.domainSize):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    s += "\\end{minipage}" + "\n"
    s += "&" + "\n"
    s += "\\begin{minipage}{0.40\\textwidth}" + "\n"
    s += "\\begin{enumerate}[label=(\\Alph*)]" + "\n"
    for i in range(self.rangeSize):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    s += "\\end{minipage}" + "\n"
    s += "\\end{tabular}" + "\n"
    s += "\\end{center}" + "\n"

    return s
