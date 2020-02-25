#!/bin/bash

texs=(q10.tex  q1.tex  q2.tex  q3.tex  q4.tex  q5.tex  q6.tex  q7.tex  q8.tex  q9.tex)

for fn in ${texs[@]}; do
  pdflatex $fn
  pdflatex $fn
done
