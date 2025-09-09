#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: a domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.
"""

from pathlib import Path

import yaml


def load_yaml_file(file_path: str | Path) -> dict:
    """
    Load the input YAML file.
    """
    with open(file_path, "r", encoding="utf-8") as file_object:
        return yaml.safe_load(file_object)


def save_yaml_file(file_path: str | Path, data: dict) -> None:
    """
    Save the output YAML file.
    """
    with open(file_path, "w", encoding="utf-8") as file_object:
        yaml.dump(data, file_object, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":

    print(__file__)
