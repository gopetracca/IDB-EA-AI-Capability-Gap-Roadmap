# -*- coding: utf-8 -*-
"""Loader for the verified source register.

The register itself is DATA and lives in `model/sources.json` — edit it there.
This module only reads it and exposes the same names the builders have always used,
so `build_prov.py` is unchanged.

Governed by ADR-0010 (alias D10) — provenance is graded by whether a reviewer can open it.

Grades: A openly available, dated, versioned, standards body or public authority
        B openly available and dated, but vendor-published or non-normative
        C available but undated / superseded / flagged historical / paywalled
        D non-public, or not a publication at all - unusable as evidence externally
"""
import json
import os

# run.py assembles a flat working directory, so sources.json sits alongside this file.
# Fall back to the repository layout when imported directly from build/.
_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATES = [
    os.path.join(_HERE, "sources.json"),
    os.path.join(_HERE, os.pardir, "model", "sources.json"),
]
for _p in _CANDIDATES:
    if os.path.exists(_p):
        _PATH = _p
        break
else:
    raise IOError("sources.json not found in: " + ", ".join(_CANDIDATES))

with open(_PATH, encoding="utf-8") as _f:
    _DOC = json.load(_f)

ACCESS_DATE = _DOC["access_date"]
GRADES = _DOC["grades"]

# Tuple order the builders index positionally. Do not reorder.
FIELDS = ["id", "short", "title", "publisher", "edition", "date", "url", "access",
          "type", "locus_form", "grade", "status", "caution"]

SOURCES = [tuple(s[k] for k in FIELDS) for s in _DOC["sources"]]

# raw provenance string -> (source id, locus already stated in the string)
NORMALIZE = {k: (v["source"], v["locus"]) for k, v in _DOC["normalize"].items()}

# a raw string that cites two things at once contributes a second pair
EXTRA_FROM = {k: (v["source"], v["locus"]) for k, v in _DOC["extra_from"].items()}
