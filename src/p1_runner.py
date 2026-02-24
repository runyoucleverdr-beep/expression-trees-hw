from __future__ import annotations
from src.p1_io import parse_postfix_csv
from src.expression_tree import build_expression_tree


def main() -> None:
    """
    Runner for Problem 1:
      - Read expressions from p1_construct_tree.csv
      - For each expression:
          build expression tree
          print minimal info for sanity check

    TODO:
      - Set file_path to "p1_construct_tree.csv" (repo root)
      - Call parse_postfix_csv(file_path)
      - Loop through expressions with enumerate
      - Call build_expression_tree(tokens)
      - Print line index and root.value (and optionally tokens)
    """
    
    file_path = "p1_construct_tree.csv" 
    expressions = parse_postfix_csv(file_path)

    for i, tokens in enumerate(expressions, start=1):
        root = build_expression_tree(tokens)
        # Minimal sanity output: line number + root operator/value
        print(f"Line {i}: root={root.value}  tokens={tokens}")

    
    pass


if __name__ == "__main__":
    main()