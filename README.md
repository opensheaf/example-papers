# Example papers for OpenSheaf archives

Test inputs for [opensheaf-py](https://github.com/opensheaf/opensheaf-py)
(the `osheaf` command) and the templates
[archive-template](https://github.com/opensheaf/archive-template) and
[collection-template](https://github.com/opensheaf/collection-template):
papers to deposit, with their sources, PDFs and metadata, chosen so that every
workflow of the tools can be tried, including the unusual ones.

| Folder | What | Tries |
|---|---|---|
| `papers/random-walks/` | an invented LaTeX paper in three versions (`v1`, `submitted`, `v2`), with a bibliography and a figure in a sub-folder | versions, a version found later and placed with `--after`, stages, change notes |
| `papers/heat-notes/` | invented lecture notes written in Markdown (PDF by pandoc) | a source that is not LaTeX |
| `papers/lost-sources/` | an invented paper deposited as a PDF alone, whose source is found later | `--no-source`, then `osheaf complete` |
| `texmacs/` | a TeXmacs paper and two sets of TeXmacs slides from [tm-forge](https://github.com/texmacs/tm-forge), with style files and figures (see `texmacs/README.md`) | TeXmacs sources deposited with their PDF; slides; metadata filled in by hand |
| `arxiv-downloads/` | two invented arXiv papers (`0000.00001`, two versions; `0000.00002`, a single-file source) in the layout written by `osheaf arxiv fetch` | `osheaf arxiv import` offline: per-version licences, comments, macros in abstracts |
| `arxiv-real/` | three real arXiv preprints, CC BY 4.0 or CC0 in every version (4, 2 and 2 versions), downloaded with `osheaf arxiv fetch` (see `arxiv-real/README.md`) | `osheaf arxiv import` on real data |
| `zenodo/` | real slides from Zenodo under CC BY 4.0: a beamer talk with bibliography and figures, and a talk in two versions of 22 files that share 20 (see `zenodo/README.md`) | archiving with metadata filled in by hand; storage of unchanged files once |
| `notices/` | an erratum | `osheaf notice` with a file |
| `deposits/` | YAML descriptions of the deposits (`osheaf deposit --from ...`) | inputs from files |

The invented papers, their PDFs and the fake arXiv records are made by
`make.sh` and `make_arxiv.py` (TeX Live and pandoc; with
`SOURCE_DATE_EPOCH` fixed, the PDFs are rebuilt byte for byte).

## Use

```
git clone https://github.com/opensheaf/example-papers
osheaf init demo --archive-id tag:example.org,2026:demo --name Demo \
  --base-url https://example.org/demo/ --curator "Example, Ada"
osheaf --root demo deposit --from example-papers/deposits/random-walks.yaml
osheaf --root demo arxiv import example-papers/arxiv-downloads
osheaf --root demo collect && osheaf --root demo index && osheaf --root demo verify
```

or run the testing ground of the archive template (`examples/run.sh` there),
which goes through every workflow.

## Licences

- The invented papers, notes, erratum, fake arXiv records and the YAML files:
  CC0 1.0 (public domain); the people in them are invented.
- `texmacs/`: the GNU General Public License, version 3, the licence of
  tm-forge, from which they are copied unchanged; their authors are named in
  `texmacs/README.md` and in the deposits.
- `arxiv-real/` and `zenodo/`: the licences of their authors (CC BY 4.0 or
  CC0), as given in the README of each folder, redistributed unchanged with
  attribution. `open-candidates.md` records how they were found and where
  each licence was read.
