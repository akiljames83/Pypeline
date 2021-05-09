#!/bin/bash

# remove old docs if previously generated
rm -rf docs

# generate documentation and place in the documentation folder
pdoc -o docs --html Pypeline

pdoc3 --pdf Pypeline > pdf.md

pandoc --metadata=title:"Pypleine Documentation"               \
           --from=markdown+abbreviations+tex_math_single_backslash  \
           --pdf-engine=xelatex \
           --toc --toc-depth=4 --output=pdf.pdf  pdf.md

rm pdf.md

mv pdf.pdf docs/MIS.pdf