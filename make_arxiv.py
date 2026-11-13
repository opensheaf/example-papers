#!/usr/bin/env python3
"""Build arxiv-downloads/: two invented arXiv papers in the layout written by
`osheaf arxiv fetch`, to try `osheaf arxiv import` offline. The identifiers
0000.00001 and 0000.00002 are not real arXiv identifiers. Run make.sh first
(the PDFs come from papers/). The archives are built reproducibly."""
import gzip, hashlib, io, json, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
P = ROOT / "papers"
OUT = ROOT / "arxiv-downloads"


def targz(files):
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w", format=tarfile.USTAR_FORMAT) as t:
        for name, data in sorted(files.items()):
            info = tarfile.TarInfo(name)
            info.size, info.mtime, info.mode = len(data), 1700000000, 0o644
            t.addfile(info, io.BytesIO(data))
    return gzip.compress(raw.getvalue(), mtime=0)


def record(aid, title, authors, abstract, versions, licence, comments=None, categories="math.PR"):
    vs = "".join(f'<version version="{v}"><date>{d}</date><size>1kb</size>'
                 f'<source_type>D</source_type></version>' for v, d in versions)
    com = f"<comments>{comments}</comments>" if comments else ""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"><GetRecord><record>
<header><identifier>oai:arXiv.org:{aid}</identifier></header>
<metadata><arXivRaw xmlns="http://arxiv.org/OAI/arXivRaw/">
<id>{aid}</id><submitter>Ada Example</submitter>{vs}
<title>{title}</title><authors>{authors}</authors><categories>{categories}</categories>
{com}<license>{licence}</license><abstract>{abstract}</abstract>
</arXivRaw></metadata></record></GetRecord></OAI-PMH>
'''


CCBY = "http://creativecommons.org/licenses/by/4.0/"
ARXIV = "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"
papers = OUT / "papers"
info, download, ids = {}, {}, {}

# 0000.00001: two versions, sources as tar.gz (paper.tex, refs.bib, figures/walk.pdf)
d = papers / "0000.00001"
d.mkdir(parents=True, exist_ok=True)
abstract = ("We study the simple random walk $X_n$ on $\\Z^2$ and prove that it returns to the "
            "origin infinitely often. An invented paper, to test the import from arXiv.")
(d / "record.xml").write_text(record(
    "0000.00001", "Random walks on a fictitious lattice", "Ada Example and Bo Sample", abstract,
    [("v1", "Fri, 1 Mar 2024 10:00:00 GMT"), ("v2", "Sun, 15 Sep 2024 10:00:00 GMT")], CCBY))
for v, folder, comments, lic in (("v1", "v1", "8 pages, 1 figure", ARXIV),
                                 ("v2", "v2", "9 pages, 1 figure; a remark added", CCBY)):
    src = P / "random-walks" / folder
    files = {"paper.tex": (src / "paper.tex").read_bytes(), "refs.bib": (src / "refs.bib").read_bytes(),
             "figures/walk.pdf": (src / "figures" / "walk.pdf").read_bytes()}
    (d / f"{v}-source.tar.gz").write_bytes(targz(files))
    (d / f"{v}.pdf").write_bytes((src / "paper.pdf").read_bytes())
    info[f"0000.00001{v}"] = {"licence": lic, "comments": comments}
ids["0000.00001"] = "fictitious-walks"

# 0000.00002: one version, a single gzipped LaTeX file
d = papers / "0000.00002"
d.mkdir(parents=True, exist_ok=True)
(d / "record.xml").write_text(record(
    "0000.00002", "An old conference paper", "Ada Example",
    "An invented paper whose source is a single LaTeX file, to test the import from arXiv.",
    [("v1", "Mon, 15 Jun 1998 10:00:00 GMT")], "http://arxiv.org/licenses/assumed-1991-2003/",
    categories="math-ph"))
(d / "v1-source.gz").write_bytes(gzip.compress((P / "lost-sources" / "paper.tex").read_bytes(), mtime=0))
(d / "v1.pdf").write_bytes((P / "lost-sources" / "paper.pdf").read_bytes())
info["0000.00002v1"] = {"licence": "http://arxiv.org/licenses/assumed-1991-2003/", "comments": "4 pages"}
ids["0000.00002"] = "old-conference-paper"

for aid in ("0000.00001", "0000.00002"):
    for f in sorted((papers / aid).iterdir()):
        if f.name != "record.xml":
            v, _, kind = f.name.partition(".")
            key = f"{v.split('-')[0]}.{'src' if '-source' in f.name else 'pdf'}"
            download.setdefault(aid, {})[key] = {"file": f.name, "bytes": f.stat().st_size,
                                                 "sha256": hashlib.sha256(f.read_bytes()).hexdigest()}
for name, data in (("version-licences.json", info), ("identifiers.json", ids), ("download.json", download)):
    (OUT / name).write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
print("written", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*") if p.is_file()))
