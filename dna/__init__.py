#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: A domain-specific language
(transcription between UTF-8 and binary)
based on YAML.
"""

import argparse
import sys

from .core import utf8_to_dna

__version__ = "0.1.0"


def main() -> None:
    """
    The main function.
    """
    parser = argparse.ArgumentParser(
        prog="dna",
        description=(
            "+------------------------------------------+\n"
            "|                    DNA                   |\n"
            "|        A domain-specific language        |\n"
            "| (transcription between UTF-8 and binary) |\n"
            "|              based on YAML.              |\n"
            "+------------------------------------------+"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=str,
        help="The path of the input YAML file."
    )
    parser.add_argument(
        "-i",
        "--input-file",
        type=str,
        help="The path of the input YAML file."
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        help="The path of the output YAML file."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Print the version number of %(prog)s and exit.",
        version=f"%(prog)s {__version__}"
    )

    command_args = parser.parse_args()
    path_to_yaml = (
        command_args.path
        if command_args.path else command_args.input_file
    )

    if not path_to_yaml:
        parser.print_usage()
        sys.exit(1)

    if command_args.output_file:
        utf8_to_dna(path_to_yaml, command_args.output_file)
        print(f"Saved to the file: {command_args.output_file}")


if __name__ == "__main__":

    main()
