<p align="center">
    <img alt="logo" src="https://github.com/project-aico/dna/raw/main/assets/DNA_small.svg"
        width="160" />
</p>

# DNA

[![GitHub Actions Workflow Status](https://github.com/project-aico/dna/actions/workflows/python-publish.yml/badge.svg)](https://github.com/project-aico/dna/blob/main/.github/workflows/python-publish.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/project-aico/dna)](https://github.com/project-aico/dna/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dnadsl)](https://pypi.org/project/dnadsl/)
[![PyPI - Version](https://img.shields.io/pypi/v/dnadsl)](https://pypi.org/project/dnadsl/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/dnadsl)](https://pypi.org/project/dnadsl/#files)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dnadsl)](https://pypistats.org/packages/dnadsl)
[![GitHub License](https://img.shields.io/github/license/project-aico/dna)](https://github.com/project-aico/dna/blob/main/LICENSE)

A domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.

## Transcoding

Please refer to [coding.py](https://github.com/project-aico/dna/blob/main/dna/coding.py):

```python
DNA_TO_BIN = {
    "A": "00",
    "C": "01",
    "G": "10",
    "T": "11"
}

BIN_TO_DNA = {
    v: k
    for k, v in DNA_TO_BIN.items()
}

DNA_COMPLEMENT = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}
```

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

## Usage

Run `dna --help` for help:

```bash
$ dna --help
usage: dna [-h] [-m {encode,decode}] [-i INPUT_FILE] [-o OUTPUT_FILE] [-v]

+--------------------------------------------------+
|                        DNA                       |
|            A domain-specific language            |
| (transcription between UTF-8 text and DNA bases) |
|                  based on YAML.                  |
+--------------------------------------------------+

options:
  -h, --help            show this help message and exit
  -m {encode,decode}, --mode {encode,decode}
                        Choose the mode of transcoding.
                        encode: UTF-8 to bases; decode: bases to UTF-8.
                        The default is: encode
  -i INPUT_FILE, --input-file INPUT_FILE
                        The path of the input YAML file.
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        The path of the output YAML file.
  -v, --version         Print the version number of dna and exit.
```

## Examples

- [The input UTF-8 text](https://github.com/project-aico/dna/blob/main/examples/input_text.yml):

    ```yaml
    text_utf8: 😄😊
    ```

- [The output DNA bases](https://github.com/project-aico/dna/blob/main/examples/output_bases.yml):

    ```yaml
    text_utf8: 😄😊
    dna:
    positive_strand:
        sequence: TTAAGCTTGCGAGACATTAAGCTTGCGAGAGG
        binary: 11110000 10011111 10011000 10000100 11110000 10011111 10011000 10001010
        text: 😄😊
    negative_strand:
        sequence: AATTCGAACGCTCTGTAATTCGAACGCTCTCC
        binary: 00001111 01100000 01100111 01111011 00001111 01100000 01100111 01110101
        text: "\x0F`g{\x0F`gu"
    ```

- [The input DNA bases](https://github.com/project-aico/dna/blob/main/examples/input_bases.yml):

    ```yaml
    positive_strand: TGAGGCTCGGCATGTTGTGAGATTTTAAGCTTGCAAGTCG
    ```

- [The output UTF-8 text](https://github.com/project-aico/dna/blob/main/examples/output_text.yml):

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
