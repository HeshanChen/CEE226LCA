#!/usr/bin/env bash
# Download the four background papers used by the "domain knowledge" condition from the
# course reference repo (eunicehjung/CEE226-BuildingLCA-LLM) into references/1.pdf-4.pdf.
# 4.pdf on that repo's main branch is an empty 2-byte file; the intended paper
# (Rezaei, Bulle & Lesage 2019) is taken from the commit where it was uploaded as 5.pdf.
set -euo pipefail
cd "$(dirname "$0")/../references"
RAW=https://raw.githubusercontent.com/eunicehjung/CEE226-BuildingLCA-LLM
MAIN=f9b934a4f7418331a62f09d8fc4e449c1a5a7a65
FIRST=13e8585353c70fc3a0fe9eea3afbd22990774ac6
curl -fsSL -o 1.pdf "$RAW/$MAIN/references/1.pdf"   # Monahan & Powell 2011
curl -fsSL -o 2.pdf "$RAW/$MAIN/references/2.pdf"   # Basbagill et al. 2013
curl -fsSL -o 3.pdf "$RAW/$MAIN/references/3.pdf"   # Takano et al. 2014
curl -fsSL -o 4.pdf "$RAW/$FIRST/references/5.pdf"  # Rezaei et al. 2019
ls -l 1.pdf 2.pdf 3.pdf 4.pdf
