#!/usr/bin/env bash
# Fetch the envelope-focused reference documents for the domain-knowledge condition
# (experiment_config.py: INCLUDE_ENVELOPE_DOCS). They are public but not re-hosted here.
set -euo pipefail
cd "$(dirname "$0")/../references"
mkdir -p envelope_docs && cd envelope_docs
get() { [ -s "$1" ] || curl -fsSL --retry 3 -o "$1" "$2"; echo "$1 $(wc -c < "$1") bytes"; }
# RDH Building Science, Embodied Carbon Analysis: Spray Foam Assemblies (2025): wall assemblies, A1-A3 per m2
get rdh2025.pdf    "https://res.cloudinary.com/elastochem/image/upload/v1766159206/RDH_EmbodiedCarbon_Rev3_ga4gjq.pdf"
# Carbon Leadership Forum, 2023 North American Material Baselines (EPD-based product baselines)
get clf2023.pdf    "https://digital.lib.washington.edu/researchworks/bitstreams/cf14fcca-501e-4a97-8257-b951e893a5ff/download"
# Arup and Saint-Gobain, The carbon footprint of facades: significance of glass
get arup_glass.pdf "https://arup.com/globalassets/downloads/insights/the-carbon-foot-print-of-facades-the-significance-of-glass.pdf"
# Zargar, Impacts of Fenestration Materials on the Embodied Carbon of Buildings, UBC Sustainability Scholars 2022
get ubc2022.pdf    "https://sustain.ubc.ca/sites/default/files/2022-018_Research%20on%20the%20impacts%20of%20Innovative%20Fenestration%20Materials_Zargar.pdf"
