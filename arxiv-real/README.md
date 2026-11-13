# Real arXiv preprints with open licences

Downloaded with `osheaf arxiv fetch` (records, every version's PDF and
source, and every version's licence and comments in `version-licences.json`),
to try `osheaf arxiv import` on real data. Each version's licence was read
from its own arXiv page: all are CC BY 4.0 or CC0, which allow
redistribution. They are redistributed here unchanged, with attribution:

- arXiv:2306.11690 (v1–v4, CC BY 4.0): Kei Kobayashi, Hyunchul Park, *A
  unified approach to the small-time behavior of the spectral heat content
  for isotropic Lévy processes*. https://arxiv.org/abs/2306.11690
- arXiv:2303.17827 (v1–v2, CC BY 4.0): Zakhar Kabluchko, Daniel Rosen,
  Christoph Thäle, *A quantitative central limit theorem for Poisson
  horospheres in high dimensions*. https://arxiv.org/abs/2303.17827
- arXiv:2310.18699 (v1–v2, CC0 1.0): Nguyen Tien Dung, *Some new
  concentration inequalities for the Itô stochastic integral*.
  https://arxiv.org/abs/2310.18699

`identifiers.json` holds the object identifiers chosen for the import. The
search that found them, with the evidence for each licence, is in
`../open-candidates.md`. Known limitation: arXiv gives authors as plain
names, so the importer takes the last word as the family name ("Nguyen Tien
Dung" becomes "Dung, Nguyen Tien"); correct such names by hand when it
matters.
