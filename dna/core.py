#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
DNA: a domain-specific language
(transcription between UTF-8 text and DNA bases)
based on YAML.
"""

from pathlib import Path

from .coding import BIN_TO_DNA, DNA_COMPLEMENT, DNA_TO_BIN
from .yaml_io import load_yaml_file, save_yaml_file


def utf8_to_binary(text: str) -> str:
    """
    Convert the UTF-8 text to a binary string,
    grouping each byte with a space.
    """
    return " ".join(f"{byte:08b}" for byte in text.encode("utf-8"))


def remove_binary_spaces(binary: str) -> str:
    """
    Remove spaces from binary strings.
    """
    return binary.replace(" ", "")


def binary_to_utf8(binary: str) -> str:
    """
    Convert the binary string to a UTF-8 text.
    """
    bits = remove_binary_spaces(binary)

    # Handles non-multiple-of-8 lengths by padding with 0.
    bytes_seq = [
        int(bits[i: i + 8].ljust(8, "0"), 2)
        for i in range(0, len(bits), 8)
    ]

    return bytes(bytes_seq).decode("utf-8", errors="replace")


def binary_to_dna(binary: str) -> str:
    """
    Convert the binary string to a strand of DNA
    (every 2 bits to 1 base).
    """
    bits = remove_binary_spaces(binary)

    # Handles non-multiple-of-2 lengths by padding with 0.
    return "".join(
        BIN_TO_DNA[bits[i: i + 2].ljust(2, "0")]
        for i in range(0, len(bits), 2)
    )


def dna_to_binary(dna_seq: str) -> str:
    """
    Convert the strand of DNA to a binary string
    (every 4 bases to 8 bits + 1 space delimiter).
    """
    bits = "".join(DNA_TO_BIN[base] for base in dna_seq)
    return " ".join(bits[i: i + 8] for i in range(0, len(bits), 8))


def complement_dna(dna_seq: str) -> str:
    """
    Generate a complementary strand of DNA.
    """
    return "".join(DNA_COMPLEMENT[base] for base in dna_seq)


def transcode_dna(input_file: str | Path, output_file: str | Path) -> None:
    """
    Conversion between UTF-8 text and DNA bases.
    """
    text_utf8 = load_yaml_file(input_file).get("text_utf8", None)
    dna_positive = load_yaml_file(input_file).get("positive_strand", None)

    if text_utf8 and dna_positive:
        raise ValueError(
            "Input YAML cannot contain both 'text_utf8' "
            "and 'positive_strand'. "
            "Please provide only one."
        )
    elif text_utf8:
        # encoding mode: UTF-8 to DNA
        dna_positive = binary_to_dna(utf8_to_binary(text_utf8))
    elif dna_positive:
        # decoding mode: DNA to UTF-8
        text_utf8 = binary_to_utf8(dna_to_binary(dna_positive))
    else:
        raise ValueError(
            "Input YAML must contain either "
            "'text_utf8' or 'positive_strand'."
        )

    bin_positive = dna_to_binary(dna_positive)
    dna_negative = complement_dna(dna_positive)
    bin_negative = dna_to_binary(dna_negative)

    output_text = {
        "text_utf8": text_utf8,
        "dna": {
            "positive_strand": {
                "sequence": dna_positive,
                "binary": bin_positive,
                "text": binary_to_utf8(bin_positive),
            },
            "negative_strand": {
                "sequence": dna_negative,
                "binary": bin_negative,
                "text": binary_to_utf8(bin_negative),
            },
        },
    }

    save_yaml_file(output_file, output_text)


if __name__ == "__main__":

    print(__file__)
