# Expression Trees & Postfix Evaluation (HW2)

This repository contains solutions for Problems 1–4:

1) Construct an expression tree from a postfix token list (comma-separated input file).  
2) Print prefix / infix / postfix expressions using tree traversals.  
3) Evaluate a postfix expression using a custom stack (space-separated string input).  
4) Edge cases control  

> **Note:** Run commands from the project root directory (the folder that contains `src/`).

---

## Project Structure

- `src/node.py`  
  Binary tree node definition used by the expression tree.

- `src/expression_tree.py`  
  Problem 1: `build_expression_tree(postfix_tokens)` builds an expression tree and returns the root node.

- `p1_construct_tree.csv`  
  Problem 1 input file (one postfix expression per line; comma-separated tokens, often quoted).

- `src/p1_io.py`  
  CSV parsing helper: `parse_postfix_csv(file_path)` → `List[List[str]]`.

- `src/p1_runner.py`  
  Runner for Problem 1: reads `p1_construct_tree.csv`, builds a tree per line, and prints the root.  
  Run in PowerShell:  
  `python -m src.p1_runner`

- `src/traversals.py`  
  Problem 2: traversal functions that return lists:
  - `to_prefix_list(root)`
  - `to_infix_list(root)` (with parentheses as separate elements)
  - `to_postfix_list(root)`  
  Run in PowerShell:  
  `python -c "from src.expression_tree import build_expression_tree; from src.traversals import to_prefix_list,to_infix_list,to_postfix_list; r=build_expression_tree(['3','4','+','2','*']); print('Prefix:', to_prefix_list(r)); print('Infix:', to_infix_list(r)); print('Postfix:', to_postfix_list(r))"`

- `src/stack.py`  
  Custom Stack implementation (manually managed `top` index).

- `src/postfix_eval.py`  
  Problem 3: `evaluate_postfix(postfix_expr)` evaluates a space-separated postfix expression using the custom stack.  
  Run in PowerShell:  
  `python -c "from src.postfix_eval import evaluate_postfix; print(evaluate_postfix('5 1 2 + 4 * + 3 -'))"`

---

## Environment / Setup

Python 3.x recommended.

## AI statement:
In homework 2 assignment, AI is used to
1) help me learn how to use git, what are the basic commands, in what stage of the coding workflow that I can leave a comment and push.
2) help me learn more about markdown format and rearranged this file with me. 