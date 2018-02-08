#!/bin/bash

pandoc -s kai_blumberg_msc_thesis.md -o kai_blumberg_msc_thesis.docx --bibliography bib.bib --csl=international-journal-of-systematic-and-evolutionary-microbiology.csl --toc --toc-depth=4 -V geometry:margin=1in --listings -H listings-setup.tex --variable urlcolor=cyan metadata.yaml

pandoc -s kai_blumberg_msc_thesis.md -o kai_blumberg_msc_thesis.pdf --bibliography bib.bib --csl=international-journal-of-systematic-and-evolutionary-microbiology.csl --toc --toc-depth=4 -V geometry:margin=1in --listings -H listings-setup.tex --variable urlcolor=cyan metadata.yaml
