#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: a domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.
"""

import argparse
import sys

from .core import transcode_dna

__version__ = "0.3.0"


def main() -> None:
    """
    The main function.
    """
    parser = argparse.ArgumentParser(
        prog="dna",
        description=(
            "+--------------------------------------------------+\n"
            "|                        DNA                       |\n"
            "|            A domain-specific language            |\n"
            "| (transcription between UTF-8 text and DNA bases) |\n"
            "|                  based on YAML.                  |\n"
            "+--------------------------------------------------+"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "-m",
        "--mode",
        default="encode",
        type=str,
        choices=["encode", "decode"],
        help=(
            "Choose the mode of transcoding.\n"
            "encode: UTF-8 to bases; decode: bases to UTF-8.\n"
            "The default is: %(default)s"
        )
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

    if not command_args.input_file:
        parser.print_usage()
        sys.exit(1)

    if command_args.output_file:
        transcode_dna(command_args.input_file, command_args.output_file)
        print(f"Saved to the file: {command_args.output_file}")


if __name__ == "__main__":

    main()
