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

class MTFQType(QType):
  def __init__(self, name, n1, n2, tm):
    QType.__init__(self, name, n1, tm)
    self.rangeSize = n2

  def __str__(self):
    return "MTFQType(\"" + self.name + "\", " + str(self.domainSize) + ", " + str(self.rangeSize) + ", " + str(self.totalMarks) + ")"
