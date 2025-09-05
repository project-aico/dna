<p align="center">
    <img alt="logo" src="https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/assets/logo.svg"
        width="138" />
</p>

# DNA

[![GitHub Actions Workflow Status](https://github.com/ZhanZiyuan/PixelPuzzle/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ZhanZiyuan/PixelPuzzle/blob/main/.github/workflows/python-publish.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/ZhanZiyuan/PixelPuzzle)](https://github.com/ZhanZiyuan/PixelPuzzle/commits/main/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/)
[![PyPI - Version](https://img.shields.io/pypi/v/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/pixelpuzzle)](https://pypi.org/project/pixelpuzzle/#files)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pixelpuzzle)](https://pypistats.org/packages/pixelpuzzle)
[![GitHub License](https://img.shields.io/github/license/ZhanZiyuan/PixelPuzzle)](https://github.com/ZhanZiyuan/PixelPuzzle/blob/main/LICENSE)


DNA: A domain-specific language
(transcription between UTF-8 and binary)
based on YAML.
















## Installation

PixelPuzzle can be installed
from [PyPI](https://pypi.org/project/pixelpuzzle/):

```bash
pip install pixelpuzzle
```

or download the repository and run:

```bash
pip install .
```

as of the repository root folder.

## Examples

- The original image:

    ![The original image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/original.png "original")

- The shuffled image (using the random seed `0721`):

    ![The shuffled image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/shuffled.png "shuffled")

- The recovered image:

    ![The recovered image](https://github.com/ZhanZiyuan/PixelPuzzle/raw/main/examples/recovered.png "recovered")

## Packaging

The binaries are created with
[PyInstaller](https://github.com/pyinstaller/pyinstaller):

```bash
# Package it on Linux
pyinstaller --name PixelPuzzle --onefile -p pixelpuzzle pixelpuzzle/__main__.py

# Package it on Windows
pyinstaller --name PixelPuzzle --onefile --icon python.ico -p pixelpuzzle pixelpuzzle/__main__.py
```



## Copyrights

PixelPuzzle is a free, open-source software package
(distributed under the [GPLv3 license](./LICENSE)).
The sample image used is downloaded from
[satchely doki doki literature club! natsuki](https://yande.re/post/show/465068).
The Python icon is downloaded from
[python.ico](https://github.com/python/cpython/blob/main/PC/icons/python.ico).




