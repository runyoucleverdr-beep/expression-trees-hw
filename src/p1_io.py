from __future__ import annotations
from typing import List


def parse_postfix_csv(file_path: str) -> List[List[str]]:
    """
    Read Problem 1 input file and convert each line into a list of postfix tokens.

    Input:
      - One expression per line
      - The whole line is commonly quoted, e.g. "3,4,+,2,*"
      - Tokens are separated by commas

    Output:
      - A list where each element is a token-list for one expression line.

    TODO:
      - Open the file (utf-8).
      - Iterate line by line.
      - Strip whitespace and skip empty lines.
      - Remove surrounding quotes if present.
      - Split by comma into tokens.
      - Strip whitespace for each token; ignore empty tokens.
      - Append each token-list to the result.
    """
    expressions: List[List[str]] = []

    # TODO: open file, iterate each line
    # with open(file_path, "r", encoding="utf-8") as f:
    #     for raw_line in f:
    #         ...

    return expressions