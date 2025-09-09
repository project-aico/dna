#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: a domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.
"""

import sys
from pathlib import Path

from dna import main

if __package__ is None and not getattr(sys, "frozen", False):
    path = Path(__file__).resolve()
    sys.path.insert(0, str(path.parent.parent))

if __name__ == "__main__":

    main()
