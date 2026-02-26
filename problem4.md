# Problem 4 — Edge Case Handling (Summary for Problems 1–3)

This section explains how edge cases are handled across **Problem 1 (tree construction)**, **Problem 2 (traversal printing)**, and **Problem 3 (postfix evaluation with a custom stack)**.  
For each case, I describe the **trigger**, the **handling behavior**, and the **reason**.

---

## 1) Empty postfix expressions

**Where**
- Problem 1: `build_expression_tree(postfix_tokens)`
- Problem 3: `evaluate_postfix(postfix_expr)`
- (Problem 2) Traversals: `to_prefix_list(None)`, `to_infix_list(None)`, `to_postfix_list(None)`

**Trigger**
- Empty token list (Problem 1), e.g., `[]`
- Empty/whitespace-only input string (Problem 3), e.g., `""`
- Empty tree root (Problem 2), `root is None`

**Handling**
- Problem 1: raise `ValueError` for empty token list.
- Problem 3: raise `ValueError` for empty input string after splitting.
- Problem 2: return `[]` for an empty tree (graceful handling).

**Reason**
- An empty postfix expression cannot produce a valid tree or a numeric result.
- For traversal printing, returning an empty list is a clean “no output” result for an empty tree.

---

## 2) Malformed postfix expressions (insufficient operands, too many operands)

### 2.1 Insufficient operands
**Where**
- Problem 1: `build_expression_tree()`
- Problem 3: `evaluate_postfix()`

**Trigger**
- An operator is encountered but there are fewer than 2 items on the stack.

**Handling**
- Raise `ValueError` (e.g., “not enough operands for operator”).

**Reason**
- All supported operators are binary (`+ - * /`), so each operator needs exactly two operands/sub-expressions.

### 2.2 Too many operands (leftover operands)
**Where**
- Problem 1: after processing all tokens
- Problem 3: after processing all tokens

**Trigger**
- After processing finishes, the stack does not reduce to exactly one item.

**Handling**
- Raise `ValueError` (e.g., “leftover operands after processing/evaluation”).

**Reason**
- A valid postfix expression must collapse to one final result:
  - one root node for the expression tree (Problem 1),
  - one numeric value for evaluation (Problem 3).

---

## 3) Division by zero

**Where**
- Problem 3: `evaluate_postfix()` when applying `/`

**Trigger**
- The division operator is applied with `right_operand == 0`.

**Handling**
- Raise `ZeroDivisionError`.

**Reason**
- This matches Python’s arithmetic behavior and allows test cases to explicitly catch the error.

---

## 4) Invalid tokens (non-numeric operands, unsupported operators)

**Where**
- Problem 1: `build_expression_tree()`
- Problem 3: `evaluate_postfix()`

**Trigger**
- A token is neither:
  - a supported operator (`+ - * /`), nor
  - a numeric value parsable by `float(token)`.

**Handling**
- Raise `ValueError` (invalid token).

**Reason**
- “Fail fast” avoids silently ignoring bad input and prevents incorrect results.

---

## 5) Very large numbers or results

**Where**
- Problem 3: `evaluate_postfix()` (numeric parsing and arithmetic)

**Trigger**
- Extremely large operands or intermediate results (e.g., `"1e308 1e308 +"`) can overflow in floating-point arithmetic.

**Handling**
- Operands are parsed as `float`, so very large results may become `inf` (infinity).
- **Fix applied:** the function avoids applying `round()` / integer-casting to non-finite values (`inf`, `-inf`, `nan`) by checking `math.isfinite(result)` first.
  - If `result` is not finite, it is returned as-is (as a float), preventing `OverflowError`.

**Reason**
- Floating-point overflow is expected behavior in Python when using `float`.
- The assignment focus is correct stack logic and validation; the code should handle overflow cases gracefully without crashing due to output formatting.

---

## 6) Negative numbers in the expression

**Where**
- Problem 1: numeric token handling in `build_expression_tree()`
- Problem 3: numeric token handling in `evaluate_postfix()`

**Trigger**
- A negative number appears as a single token (e.g., `-3`, `-2.5`).

**Handling**
- Negative numbers are treated as numeric operands because numeric detection uses `float(token)`.
- The token `"-"` is treated as an operator only when it appears alone as the operator token.

**Reason**
- Under correct tokenization (comma-separated in Problem 1, space-separated in Problem 3), `"-"` (operator) and `"-3"` (number) are unambiguous.

---