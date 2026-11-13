# Openly licensed example papers and slides for OpenSheaf archive tests

Checked on 2026-11-13. Nothing was downloaded. Licences were read from each version's arXiv abstract page (the `abs-license` link next to "view license") or from the Zenodo REST API record of each version. Sizes come from HTTP HEAD `Content-Length` (arXiv) or from the Zenodo API `files[].size`.

Licences accepted: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) and CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/). Anything else (arXiv non-exclusive, NC, ND, SA) was excluded.

How to read the arXiv source type: a source served as `arXiv-IDvN.gz` is a single gzipped TeX file. A source served as `arXiv-IDvN.tar.gz` is a multi-file tarball (figures, .bib or .bbl, style files). The tarballs were not opened, so their exact file lists are not given here.

---

## A. arXiv preprints (every version checked)

### A1. arXiv:2306.11690 (4 versions, CC BY 4.0, single-file source). RECOMMENDED
- Title: A unified approach to the small-time behavior of the spectral heat content for isotropic Lévy processes
- Authors: Kei Kobayashi, Hyunchul Park
- Category: math.PR. Comment: "To appear in Stochastic Processes and their Applications"
- Versions: v1 2023-06-20, v2 2023-07-05, v3 2024-02-27, v4 2024-02-29

| version | licence (read at) | PDF | source |
|---|---|---|---|
| v1 | CC BY 4.0, https://arxiv.org/abs/2306.11690v1 | 221,276 B | single .gz, 15,022 B |
| v2 | CC BY 4.0, https://arxiv.org/abs/2306.11690v2 | 219,498 B | single .gz, 15,033 B |
| v3 | CC BY 4.0, https://arxiv.org/abs/2306.11690v3 | 220,947 B | single .gz, 15,215 B |
| v4 | CC BY 4.0, https://arxiv.org/abs/2306.11690v4 | 220,898 B | single .gz, 15,215 B |

- Attribution: Kei Kobayashi and Hyunchul Park, "A unified approach to the small-time behavior of the spectral heat content for isotropic Lévy processes", arXiv:2306.11690 [v1–v4], https://arxiv.org/abs/2306.11690, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: four small versions. v3 and v4 have the same source size, so it is a good test for near-identical versions.

### A2. arXiv:2303.17827 (2 versions, CC BY 4.0, multi-file source with a figure). RECOMMENDED
- Title: A quantitative central limit theorem for Poisson horospheres in high dimensions
- Authors: Zakhar Kabluchko, Daniel Rosen, Christoph Thäle
- Categories: math.PR math.MG. Comment: "10 pages, 1 figure"
- Versions: v1 2023-03-31, v2 2024-03-07

| version | licence (read at) | PDF | source |
|---|---|---|---|
| v1 | CC BY 4.0, https://arxiv.org/abs/2303.17827v1 | 878,031 B | tar.gz, 535,530 B |
| v2 | CC BY 4.0, https://arxiv.org/abs/2303.17827v2 | 900,614 B | tar.gz, 536,343 B |

- Attribution: Zakhar Kabluchko, Daniel Rosen and Christoph Thäle, "A quantitative central limit theorem for Poisson horospheres in high dimensions", arXiv:2303.17827 [v1–v2], https://arxiv.org/abs/2303.17827, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: 10 pages. The PDF is close to the 1 MB limit, and most of the roughly 0.5 MB source is the figure.

### A3. arXiv:2310.18699 (2 versions, CC0, single-file source). RECOMMENDED
- Title: Some new concentration inequalities for the Itô stochastic integral
- Author: Nguyen Tien Dung
- Category: math.PR. Comment: "17 pages. To appear in Bernoulli"
- Versions: v1 2023-10-28, v2 2024-03-06

| version | licence (read at) | PDF | source |
|---|---|---|---|
| v1 | CC0 1.0, https://arxiv.org/abs/2310.18699v1 | 184,933 B | single .gz, 9,898 B |
| v2 | CC0 1.0, https://arxiv.org/abs/2310.18699v2 | 185,593 B | single .gz, 10,164 B |

- Attribution (CC0 requires none; recommended courtesy line): Nguyen Tien Dung, "Some new concentration inequalities for the Itô stochastic integral", arXiv:2310.18699 [v1–v2], https://arxiv.org/abs/2310.18699, dedicated to the public domain under CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/).

### A4. arXiv:2301.13555 (3 versions, CC BY 4.0, multi-file source with a figure). Alternate
- Title: Random matrices associated to Young diagrams
- Authors: Fabio Deelan Cunden, Marilena Ligabò, Tommaso Monni
- Categories: math.PR math-ph math.CO math.MP. Comment: "17 pages, 1 figure". Journal ref: Random Matrices: Theory and Applications 12(04), 2350009 (2023)
- Versions: v1 2023-01-31, v2 2023-09-01, v3 2024-03-13

| version | licence (read at) | PDF | source |
|---|---|---|---|
| v1 | CC BY 4.0, https://arxiv.org/abs/2301.13555v1 | 545,625 B | tar.gz, 161,334 B |
| v2 | CC BY 4.0, https://arxiv.org/abs/2301.13555v2 | 571,571 B | tar.gz, 160,865 B |
| v3 | CC BY 4.0, https://arxiv.org/abs/2301.13555v3 | 571,496 B | tar.gz, 160,873 B |

- Attribution: Fabio Deelan Cunden, Marilena Ligabò and Tommaso Monni, "Random matrices associated to Young diagrams", arXiv:2301.13555 [v1–v3], https://arxiv.org/abs/2301.13555, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

### A5. arXiv:2304.03102 (2 versions, CC BY 4.0, source format changes between versions). Alternate
- Title: Gibbs Properties of the Bernoulli field on inhomogeneous trees under the removal of isolated sites
- Authors: Florian Henning, Christof Külske, Niklas Schubert
- Categories: math.PR math-ph math.MP. Comment: "15 pages, 4 figures". Journal ref: Markov Processes Relat. Fields 29(5), 641–659 (2023)

| version | licence (read at) | PDF | source |
|---|---|---|---|
| v1 | CC BY 4.0, https://arxiv.org/abs/2304.03102v1 | 759,629 B | tar.gz, 41,722 B |
| v2 | CC BY 4.0, https://arxiv.org/abs/2304.03102v2 | 324,994 B | single .gz, 27,443 B |

- Attribution: Florian Henning, Christof Külske and Niklas Schubert, "Gibbs Properties of the Bernoulli field on inhomogeneous trees under the removal of isolated sites", arXiv:2304.03102 [v1–v2], https://arxiv.org/abs/2304.03102, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: v1 is a tarball and v2 is a single file. This is a useful edge case for archive tools.

### A6. Other verified candidates (2 versions each, licence checked on both versions)
| arXiv id | title / authors | licence v1, v2 | PDF v1 / v2 | source |
|---|---|---|---|---|
| 2305.19772 | A note on Serrin's type problem on Riemannian manifolds. Allan Freitas, Alberto Roncoroni, Márcio Santos (math.DG math.AP) | CC BY 4.0, CC BY 4.0 (https://arxiv.org/abs/2305.19772v1, …v2) | 216,711 / 218,505 B | single .gz (15,370 / 15,690 B) |
| 2309.01263 | $P$-log-Sobolev inequalities on $\mathbb{N}$. Bartłomiej Polaczyk (math.PR, 15 pp.) | CC BY 4.0, CC BY 4.0 (https://arxiv.org/abs/2309.01263v1, …v2) | 288,854 / 290,799 B | tar.gz (22,571 / 22,638 B), probably TeX plus .bib or .bbl |
| 2302.09050 | On the intersecting family process. Patrick Bennett, Alan Frieze, Andrew Newman, Wesley Pegden (math.CO math.PR) | CC BY 4.0, CC BY 4.0 (https://arxiv.org/abs/2302.09050v1, …v2) | 427,402 / 447,888 B | single .gz (22,069 / 23,318 B) |
| 2305.12089 | Approximation theorem for the Kawahara operator and its application in control theory. Roberto de A. Capistrano Filho, Luan S. de Sousa, Fernando A. Gallego (math.AP math.OC, 20 pp.) | CC0, CC0 (https://arxiv.org/abs/2305.12089v1, …v2) | 268,992 / 279,646 B | single .gz (21,611 / 21,462 B) |

Attribution pattern for these: `<Authors>, "<Title>", arXiv:<id> [v1–v2], https://arxiv.org/abs/<id>, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)`. For 2305.12089, use "dedicated to the public domain under CC0 1.0" in place of the CC BY clause.

### Excluded
- arXiv:1404.2981 (Hasebe and Kuznetsov, "On free stable distributions"). The current version v2 is CC BY 4.0, but v1 is under the arXiv non-exclusive licence (https://arxiv.org/abs/1404.2981v1). This shows that the OAI-PMH current licence is not enough on its own.

---

## B. Zenodo preprints

### B1. Zenodo concept 10.5281/zenodo.23452787 (2 versions, CC BY 4.0, PDF and TeX in both). RECOMMENDED
- Author: Martino Lupini (University of Bologna, ORCID 0000-0003-1588-7057)
- Resource type: publication / preprint

| version | record / DOI | date | title | licence (read at) | files |
|---|---|---|---|---|---|
| 1 | 23452788 / 10.5281/zenodo.23452788 | 2026-10-18 | The small index property for the random poset | cc-by-4.0, https://zenodo.org/api/records/23452788 | main.pdf 442,717 B; main.tex 38,728 B |
| 2 | 23916046 / 10.5281/zenodo.23916046 | 2026-11-03 | Small index, automatic continuity, and strong boundedness for the random poset | cc-by-4.0, https://zenodo.org/api/records/23916046 | main.tex 47,772 B; main.pdf 419,012 B |

- All versions: https://zenodo.org/api/records/23916046/versions
- Attribution: Martino Lupini, "Small index, automatic continuity, and strong boundedness for the random poset" (v1 titled "The small index property for the random poset"), Zenodo, https://doi.org/10.5281/zenodo.23452787, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: the title changes between versions, and the file names stay the same while their content changes. Both are good archive test cases.

### B2. Zenodo concept 10.5281/zenodo.23284707 (2 versions, CC BY 4.0, PDF only in v1, PDF and TeX in v2). RECOMMENDED
- Title: A three-generated abelian lattice-ordered group without an existentially closed prime extension
- Author: Martino Lupini (Università di Bologna, ORCID 0000-0003-1588-7057)

| version | record / DOI | date | licence (read at) | files |
|---|---|---|---|---|
| 1 (version string "draft-2026-10-10") | 23284708 / 10.5281/zenodo.23284708 | 2026-10-10 | cc-by-4.0, https://zenodo.org/api/records/23284708 | revised-counterexample.pdf 424,160 B |
| 2 | 23863253 / 10.5281/zenodo.23863253 | 2026-11-01 | cc-by-4.0, https://zenodo.org/api/records/23863253 | revised-counterexample.tex 113,146 B; revised-counterexample.pdf 278,720 B |

- Attribution: Martino Lupini, "A three-generated abelian lattice-ordered group without an existentially closed prime extension", Zenodo, https://doi.org/10.5281/zenodo.23284707, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: the sources appear only in v2. This is a useful case.

### B3. Zenodo record 276035 (1 version, CC0, PDF, TeX and .bib). Alternate CC0 item
- Title: Research practices and assessment of research misconduct
- Authors: Chris H. J. Hartgerink, Jelte M. Wicherts (Tilburg University)
- Resource type: publication / article, 2016-08-02. The DOI recorded in the metadata is ScienceOpen's 10.14293/S2199-1006.1.SOR-SOCSCI.ARYSBI.v1, not a Zenodo DOI.
- Licence: cc-zero, read at https://zenodo.org/api/records/276035
- Files: main.pdf 204,158 B; main.tex 44,040 B; library.bib 58,163 B
- Attribution (courtesy): C. H. J. Hartgerink and J. M. Wicherts, "Research practices and assessment of research misconduct", Zenodo record 276035 (https://zenodo.org/records/276035), CC0 1.0.
- Notes: social science, not mathematics. Use it only if a CC0 item with a .bib is wanted on the Zenodo side.

Caution about Zenodo search results: many recent CC-licensed "preprints" with TeX sources on Zenodo are anonymous or apparently AI-generated (Collatz, Hodge, "theory of everything" and similar). These were skipped on purpose.

---

## C. Slides (talks)

arXiv: talks or slides with a CC licence are effectively absent. An API search (`co:slides` in math.PR, math-ph, math.AP) returned only old (2002–2012) items under the default non-exclusive licence, so none are proposed. All candidates below are Zenodo records of resource type "presentation".

### C1. Zenodo 15770056: Mark Wilde, "Resource theory of asymmetric distinguishability" (1 version, CC BY 4.0, beamer source and .bib). RECOMMENDED
- DOI 10.5281/zenodo.15770056, concept DOI 10.5281/zenodo.15770055, dated 2025-06-30. Author: Mark M. Wilde (Cornell, ORCID 0000-0002-3916-4462). Topic: quantum information (math-ph).
- Licence: cc-by-4.0, read at https://zenodo.org/api/records/15770056 (only version: https://zenodo.org/api/records/15770056/versions)
- Files (6, 783 kB total): main-presentation-resource-theory-asym-dist.pdf 408,331 B; resource-theory-asym-dist.tex 42,376 B; Ref.bib 109,714 B; figure PDFs superchannel.pdf 52,838 B, sequential-ch-box-trans.pdf 94,664 B, sequential-ch-box-trans-2.pdf 94,518 B
- Attribution: Mark M. Wilde, "Resource theory of asymmetric distinguishability" (slides), Zenodo, https://doi.org/10.5281/zenodo.15770056, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

### C2. Zenodo concept 10.5281/zenodo.3511868: Conor Houghton, "journal club talk about arxiv /1811.01753" (2 versions, CC BY 4.0, beamer source). RECOMMENDED for versions
- Author: Conor Houghton (University of Bristol). Topic: neuroscience and machine learning (Bayesian networks), mathematical in style.

| version | record / DOI | date | licence (read at) | files |
|---|---|---|---|---|
| 1 | 3511869 / 10.5281/zenodo.3511869 | 2019-10-19 | cc-by-4.0, https://zenodo.org/api/records/3511869 | 22 files: 2019_10_17_journal_club.pdf 597,073 B; 2019_10_17_journal_club.tex 16,743 B; 18 small TikZ .tex fragments (1–2.5 kB each); reconstruction.png 287,461 B; layers.png 94,097 B |
| 2 | 3511948 / 10.5281/zenodo.3511948 | 2019-10-19 | cc-by-4.0, https://zenodo.org/api/records/3511948 | same 22 files; only the main .tex (16,759 B) and the PDF (597,113 B) differ |

- Attribution: Conor Houghton, "journal club talk about arxiv /1811.01753" (slides), Zenodo, https://doi.org/10.5281/zenodo.3511868, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
- Notes: about 1 MB total. Most files are identical between the two versions (identical md5), which makes it a good deduplication test.

### C3. Zenodo 3263985: Conor Houghton, "journal club talk about arxiv 1810.09536" (1 version, CC BY 4.0, small beamer source)
- DOI 10.5281/zenodo.3263985, concept DOI 10.5281/zenodo.3263984, dated 2019-06-30
- Licence: cc-by-4.0, read at https://zenodo.org/api/records/3263985
- Files (4, 329 kB total): 2019_06_27_journal_club.pdf 243,683 B; 2019_06_27_journal_club.tex 12,787 B; lstm.tex 4,108 B; logic.png 76,660 B
- Attribution: Conor Houghton, "journal club talk about arxiv 1810.09536" (slides), Zenodo, https://doi.org/10.5281/zenodo.3263985, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

### C4. Zenodo 21244469: Lars Kastner, "Dark Data in Computer Algebra" (1 version, CC BY 4.0, beamer source and .bib). Use with caution
- DOI 10.5281/zenodo.21244469, concept DOI 10.5281/zenodo.21244468, dated 2026-07-07. Author: Lars Kastner (TU Berlin, ORCID 0000-0001-9224-7761). Topic: mathematics (computer algebra, MaRDI).
- Licence: cc-by-4.0, read at https://zenodo.org/api/records/21244469
- Files (22, about 2.2 MB): talk.pdf 862,026 B; talk.tex 14,976 B; references.bib 4,731 B; fig2a.pdf; and about 18 .png/.jpg images, including screenshots (Google, zbMATH, archive pages), a MaRDI logo and photo-like images (orevkov.jpg, shustin.jpg, cremona.jpg …).
- Caution: the record is CC BY, but some embedded images (logos, screenshots, third-party pictures) are probably not the author's to license. Prefer C1–C3.
- Attribution: Lars Kastner, "Dark Data in Computer Algebra" (slides), Zenodo, https://doi.org/10.5281/zenodo.21244469, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

Not proposed: ILQGS 2026 seminar slides on Zenodo (for example 23197220 Ried, 23512253 Mele, 23966321 Ferrero). They are CC BY 4.0 and versioned, but each record bundles a 90–850 MB mp4 recording, so they are not small.

---

## Recommendation
- arXiv: **2306.11690** (4 versions, single-file TeX, CC BY), **2303.17827** (2 versions, tarball with a figure, CC BY), **2310.18699** (2 versions, single file, CC0). Swap in 2304.03102 if you want the tarball-to-single-file edge case, or 2301.13555 for 3 versions with a figure.
- Zenodo papers: **10.5281/zenodo.23452787** (2 versions, TeX and PDF in both, title change). Optionally add **10.5281/zenodo.23284707** (sources only in v2).
- Slides: **Zenodo 15770056** (Wilde, beamer with .bib) and **concept 10.5281/zenodo.3511868** (Houghton, 2 versions, many shared files). Optionally add 3263985 (smallest).
