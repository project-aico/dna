#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: a domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.
"""

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
