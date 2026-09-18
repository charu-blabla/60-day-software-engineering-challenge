# Evaluate Reverse Polish Notation

## Approach

Use a **stack** to evaluate the Reverse Polish Notation (RPN) expression.

* If the token is a number, push it onto the stack.
* If the token is an operator, pop the top two operands.
* Perform the operation and push the result back onto the stack.
* For `-` and `/`, the order is important: `b - a` and `b / a`.
* After processing all tokens, the remaining stack element is the answer.

### Stack Flow

For:

`["2", "1", "+", "3", "*"]`

```text
2        → [2]
1        → [2, 1]
+        → [3]
3        → [3, 3]
*        → [9]
```

**Result:** `9`

## Operators

The solution handles:

* `+` Addition
* `-` Subtraction
* `*` Multiplication
* `/` Division

## Edge Cases

Tested cases include:

* Single number expressions
* Negative numbers
* Different operator combinations
* Subtraction and division where operand order matters
* Expressions with multiple operations

## Complexity

* **Time:** `O(n)` — each token is processed once.
* **Space:** `O(n)` — the stack can contain up to `n` elements.
