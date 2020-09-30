class QType:
  def __init__(self, items):
    self.name       = items['name']
    self.type       = items['properties']['qtype']
    self.totalMarks = float(items['properties']['marks'])
  def toList(self):
    d=[]
    d.append(self.name)
    d.append(self.type)
    d.append(self.totalMarks)
    return d
class MCQQType(QType):

  def __init__(self, items):
    QType.__init__(self, items)
    self.options = int(items['properties']['options'])

  def toList(self):
    d=[]
    d.extend(super(MCQQType, self).toList())
    d.append(self.options)
    return d

  def __str__(self):
    return "q.MCQQType(items = { 'name' :'" + str(self.name) +"','properties':{'qtype':'"+str(self.type)+ "', 'marks':'"+str(self.totalMarks)+"','options':'"+str(self.options)+"'}})"
  @property
  def latexTemplate(self):
    s = ""
    s += "\\begin{enumerate}" + "\n"
    for i in range(self.options):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    return s

class MTFQType(QType):
  def __init__(self, items):
    QType.__init__(self, items)
    self.left = int(items['properties']['left'])
    self.right = int(items['properties']['right'])

  def toList(self):
    d=[]
    d.extend(super(MTFQType, self).toList())
    d.append(self.left)
    d.append(self.right)
    return d

  def __str__(self):
    return "q.MTFQType(items = { 'name' :'" + str(self.name) +"','properties':{'qtype':'"+str(self.type)+ "', 'marks':'"+str(self.totalMarks)+"','left':'"+str(self.left)+"','right':'"+str(self.right)+"'}})"

  @property
  def latexTemplate(self):
    s = "\n"
    s += "Match the following:" + "\n"
    s += "\\begin{center}" + "\n"
    s += "\\begin{tabular}{c@{\\hspace{1cm}}c}" + "\n"
    s += "\\begin{minipage}{0.40\\textwidth}" + "\n"
    s += "\\begin{enumerate}" + "\n"
    for i in range(self.left):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    s += "\\end{minipage}" + "\n"
    s += "&" + "\n"
    s += "\\begin{minipage}{0.40\\textwidth}" + "\n"
    s += "\\begin{enumerate}[label=(\\Alph*)]" + "\n"
    for i in range(self.right):
      s += "\t" + "\\item option " + str(i + 1) + "\n"
    s += "\\end{enumerate}" + "\n"
    s += "\\end{minipage}" + "\n"
    s += "\\end{tabular}" + "\n"
    s += "\\end{center}" + "\n"
    return s

class FIBQType(QType):
  def __init__(self,items):
    QType.__init__(self, items) 

  def toList(self):
    d=[]
    d.extend(super(FIBQType, self).toList())
    return d

  def __str__(self):
    return "q.FIBQType(items = { 'name' :'" + str(self.name) +"','properties':{'qtype':'"+str(self.type)+ "', 'marks':'"+str(self.totalMarks)+"'}})"

  @property
  def latexTemplate(self):
    s = "\n"
    s += "Fill in the blanks:" + "\n"
    return s

