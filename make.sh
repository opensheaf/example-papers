#!/bin/zsh
# Build the PDFs of the example papers (needs TeX Live and pandoc). With
# SOURCE_DATE_EPOCH fixed, rebuilding gives the same bytes.
set -eu
cd ${0:A:h}/papers
export SOURCE_DATE_EPOCH=1700000000 FORCE_SOURCE_DATE=1
TEX=(pdflatex -interaction=batchmode -halt-on-error)
# the figure, shared by the versions of random-walks
(cd random-walks && $TEX figure.tex >/dev/null && for v in v1 submitted v2; do cp figure.pdf $v/figures/walk.pdf; done)
for v in v1 submitted v2; do
  (cd random-walks/$v && $TEX paper >/dev/null && bibtex -terse paper && $TEX paper >/dev/null && $TEX paper >/dev/null)
done
(cd lost-sources && $TEX paper >/dev/null && $TEX paper >/dev/null)
(cd heat-notes && pandoc notes.md -o notes.pdf --pdf-engine=pdflatex)
# keep only sources and PDFs
find . \( -name "*.aux" -o -name "*.log" -o -name "*.bbl" -o -name "*.blg" -o -name "*.out" \) -delete
rm -f random-walks/figure.pdf
echo built: $(find . -name "*.pdf" | sort)
