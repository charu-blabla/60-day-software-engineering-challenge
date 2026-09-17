# Min Stack

## Overview

Implemented a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in **O(1)** time.

## Approach

Instead of storing only the value, each stack element stores a pair:

```text
{value, minimum_so_far}
```

When pushing a new value, compare it with the current minimum and store the smaller value as the new minimum.

### Example

For:

```text
push(5)
push(3)
push(7)
push(2)
```

The stack stores:

```text
{5, 5}
{3, 3}
{7, 3}
{2, 2}
```

So `getMin()` can directly return the second value from the top pair.

After `pop()` removes `2`, the previous minimum `3` is already stored below it.

## Complexity

* **Push:** O(1)
* **Pop:** O(1)
* **Top:** O(1)
* **Get Minimum:** O(1)
* **Space:** O(n)

## Key Takeaway

Storing the **minimum-so-far** with every element allows the minimum to be retrieved without scanning the stack.
