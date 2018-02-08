#!/bin/bash

pandoc -s kai_blumberg_msc_thesis.$1 -o kai_blumberg_msc_thesis.$2 --bibliography bib.bib --csl=international-journal-of-systematic-and-evolutionary-microbiology.csl --toc -V geometry:margin=1in --listings -H listings-setup.tex --variable urlcolor=cyan
