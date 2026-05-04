---
description: |
  [TOPIC] scitex-compat Installation
  [DETAILS] pip install scitex-compat (pure Python, no required deps); smoke verify with import + deprecated.
tags: [scitex-compat-installation]
---

# Installation

## Standard

```bash
pip install scitex-compat
```

Pure-Python; no required runtime dependencies.

## Verify

```bash
python -c "import scitex_compat; print(scitex_compat.__version__)"
python -c "from scitex_compat import deprecated, notify, notify_async; print('ok')"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-compat
cd scitex-compat
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.compat as a submodule
```

This package is intentionally minimal — it holds backwards-compat shims
for old SciTeX module locations. Do not add new features here; add them
in the proper module and, if needed, a one-line shim here.
