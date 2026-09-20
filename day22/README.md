# Implement Queue using Stacks

## Overview

Implemented a **Queue using two stacks** (`s1` and `s2`).

The queue follows **FIFO (First In, First Out)**, while stacks normally follow **LIFO (Last In, First Out)**.

## Approach

* `s1` stores the queue elements in reverse stack order.
* During `push()`, all elements from `s1` are moved to `s2`.
* The new element is pushed into `s1`.
* Elements from `s2` are moved back to `s1`.
* This keeps the **front of the queue at the top of `s1`**.
* Therefore, `pop()` and `peek()` can directly use `s1.top()`.

### Example

For:

`push(1) → push(2) → push(3)`

`s1` will have:

```text
TOP → 1
      2
      3
```

So:

* `peek()` → `1`
* `pop()` → `1`
* Next `pop()` → `2`

## Complexity

* **Push:** O(n)
* **Pop:** O(1)
* **Peek:** O(1)
* **Empty:** O(1)
* **Space:** O(n)

## Reflection

This problem helped me understand how two stacks can be rearranged to simulate **FIFO behavior** while using only stack operations.
