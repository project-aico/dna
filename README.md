<p align="center">
    <img alt="logo" src="https://github.com/project-aico/dna/raw/main/assets/DNA_small.svg"
        width="150" />
</p>

# DNA

[![GitHub Actions Workflow Status](https://github.com/project-aico/dna/actions/workflows/python-publish.yml/badge.svg)](https://github.com/project-aico/dna/blob/main/.github/workflows/python-publish.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/project-aico/dna)](https://github.com/project-aico/dna/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dnadsl)](https://pypi.org/project/dnadsl/)
[![PyPI - Version](https://img.shields.io/pypi/v/dnadsl)](https://pypi.org/project/dnadsl/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/dnadsl)](https://pypi.org/project/dnadsl/#files)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dnadsl)](https://pypistats.org/packages/dnadsl)
[![GitHub License](https://img.shields.io/github/license/project-aico/dna)](https://github.com/project-aico/dna/blob/main/LICENSE)

## Installation

DNA can be installed
from [PyPI](https://pypi.org/project/dnadsl/):

```bash
pip install dnadsl
```

or download the repository and run:

```bash
pip install .
```

as of the repository root folder.

## Examples

- [The input YAML file](https://github.com/project-aico/dna/blob/main/examples/input.yml):

    ```yaml
    text_utf8: ❤️🐶
    ```

- [The output YAML file](https://github.com/project-aico/dna/blob/main/examples/output.yml):

    ```yaml
    text_utf8: ❤️🐶
    dna:
    positive_strand:
        sequence: TGAGGCTCGGCATGTTGTGAGATTTTAAGCTTGCAAGTCG
        binary: 11100010 10011101 10100100 11101111 10111000 10001111 11110000 10011111
        10010000 10110110
        text: ❤️🐶
    negative_strand:
        sequence: ACTCCGAGCCGTACAACACTCTAAAATTCGAACGTTCAGC
        binary: 00011101 01100010 01011011 00010000 01000111 01110000 00001111 01100000
        01101111 01001001
        text: "\x1Db[\x10Gp\x0F`oI"
    ```

## Packaging

The binaries are created with
[PyInstaller](https://github.com/pyinstaller/pyinstaller):

```bash
# Package it on Linux
pyinstaller --name DNA --onefile -p dna dna/__main__.py

# Package it on Windows
pyinstaller --name DNA --onefile --icon python.ico -p dna dna/__main__.py
```

## Copyrights

DNA is a free, open-source software package
(distributed under the [GPLv3 license](./LICENSE)).
The logo used in [README.md](./README.md) is downloaded from
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:DNA_small.svg).
The Python icon is downloaded from
[python.ico](https://github.com/python/cpython/blob/main/PC/icons/python.ico).
