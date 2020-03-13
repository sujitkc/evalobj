#!/bin/bash

texs=`ls *.tex`
echo ${texs}
for fn in ${texs[@]}; do
  pdflatex $fn
  pdflatex $fn
done

rm *.aux *.out *.log
