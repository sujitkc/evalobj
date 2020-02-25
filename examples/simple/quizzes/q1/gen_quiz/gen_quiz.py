import random

SRC_DIR = "../item-bank/"
DEST_DIR = "../variants/"

quiz = ["item" + str(qnum) for qnum in range(1, 16)]


def make_qpaper(quiz, fout):
  print "in make_qpaper"
  with open("b1.tex", "r") as fin:
    head = fin.read()

  with open("b2.tex", "r") as fin:
    foot = fin.read()

  fout.write(head)
  for q in quiz[:10]:
    with open(SRC_DIR + q + ".tex", "r") as fin:
      question = fin.read()
    fout.write(question)
  fout.write(foot)

if __name__ == "__main__":
  for i in range(1, 11):

    random.shuffle(quiz)
    print quiz
    with open(DEST_DIR + "q" + str(i) + ".tex", "w") as fout:
      make_qpaper(quiz, fout)
