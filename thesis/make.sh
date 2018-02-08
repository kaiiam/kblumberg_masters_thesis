#!/bin/bash

pandoc -s kai_blumberg_msc_thesis.$1 -o kai_blumberg_msc_thesis.$2 --bibliography bib.bib --csl=international-journal-of-systematic-and-evolutionary-microbiology.csl --toc --toc-depth=4 -V geometry:margin=1in --listings --pdf-engine=xelatex --variable urlcolor=cyan metadata.yaml --template=latex.template -V fontsize=11pt
