# LeetCode 20 – Valid Parentheses

## Problem Overview

Given a string containing different types of brackets — `()`, `{}`, and `[]` — determine whether the brackets form a valid sequence.

A sequence is valid when:

* Every opening bracket has a corresponding closing bracket.
* Brackets are closed in the correct order.
* Brackets of different types are properly matched.

## Approach

The solution uses a **stack** to keep track of opening brackets.

### Stack Behavior

1. When an opening bracket `(`, `{`, or `[` is encountered, it is pushed onto the stack.
2. When a closing bracket `)`, `}`, or `]` is encountered:

   * Check whether the stack is empty.
   * Compare the closing bracket with the most recent opening bracket at the top of the stack.
   * If they match, remove the opening bracket from the stack.
   * If they do not match, the sequence is invalid.
3. After processing the entire string, the stack must be empty for the sequence to be valid.

The stack works well here because brackets follow a **Last In, First Out (LIFO)** pattern. The most recently opened bracket must always be the first one to close.

## Edge Cases Tested

Some invalid cases that need to be handled:

* `")"` → Closing bracket appears without an opening bracket.
* `"("` → Opening bracket is never closed.
* `"(]"` → Brackets do not match.
* `"([)]"` → Brackets are present but closed in the wrong order.
* `"((("` → Multiple opening brackets remain unmatched.
* `""]"` → Extra closing bracket.

Valid examples include:

* `"()"`
* `"()[]{}"`
* `"{[]}"`
* `"(([]))"`

## Complexity

* **Time Complexity:** `O(n)` — Each bracket is processed once.
* **Space Complexity:** `O(n)` — In the worst case, all characters can be opening brackets and stored in the stack.

## Key Learning

This problem demonstrates how **stacks** can be used to solve problems involving nested structures and matching pairs. The LIFO behavior of a stack naturally matches the way nested brackets need to be opened and closed.
