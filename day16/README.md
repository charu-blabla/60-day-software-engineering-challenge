# Climbing Stairs

## Problem

You are climbing a staircase with `n` steps. At each step, you can climb either **1 step** or **2 steps**.

The goal is to find the total number of distinct ways to reach the top.

For example:

* `n = 2` → `[1,1]`, `[2]` → **2 ways**
* `n = 3` → `[1,1,1]`, `[1,2]`, `[2,1]` → **3 ways**

---

## Brute Force Approach

The brute-force solution uses **recursion**.

```python
if n == 0 or n == 1:
    return 1

return self.climbStairs(n-1) + self.climbStairs(n-2)
```

### How it works

For every step, there are two possibilities:

* Take `1` step → solve `n - 1`
* Take `2` steps → solve `n - 2`

Therefore:

```text
ways(n) = ways(n-1) + ways(n-2)
```

The recursion repeatedly calculates the same values.

For example, calculating `ways(5)` requires calculating `ways(3)` and `ways(2)` multiple times:

```text
                ways(5)
               /       \
          ways(4)      ways(3)
          /    \        /   \
     ways(3) ways(2) ways(2) ways(1)
```

This repeated work makes the solution inefficient for larger values of `n`.

### Complexity

* **Time:** `O(2^n)`
* **Space:** `O(n)` due to the recursion call stack

---

## Optimized Approach

The optimized solution uses **Dynamic Programming** with only three variables:

```python
a = 1
b = 2
c = 0

for i in range(3, n+1):
    c = a + b
    a = b
    b = c

return c
```

### How it works

The number of ways follows the Fibonacci pattern:

```text
n = 1 → 1
n = 2 → 2
n = 3 → 3
n = 4 → 5
n = 5 → 8
...
```

Instead of recalculating previous values recursively, we store only the **last two results**.

For example, for `n = 5`:

```text
a = 1
b = 2

c = a + b = 3
a = 2
b = 3

c = a + b = 5
a = 3
b = 5

c = a + b = 8
```

The final result is `8`.

The important idea is that we do not need to store the entire sequence. We only need the previous two values to calculate the next one.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## Comparison

| Approach    | Time Complexity | Space Complexity | Main Idea                      |
| ----------- | --------------- | ---------------- | ------------------------------ |
| Brute Force | `O(2^n)`        | `O(n)`           | Recursive calculation          |
| Optimized   | `O(n)`          | `O(1)`           | Store only previous two values |

## Key Difference

The brute-force solution repeatedly solves the **same subproblems**, which causes unnecessary computation.

The optimized solution calculates each value **only once** and keeps only the two previous values needed for the next calculation.

Therefore, the optimized solution is significantly more efficient, especially when `n` becomes large.

## Key Learnings

* Recognized the recursive pattern `ways(n) = ways(n-1) + ways(n-2)`.
* Identified repeated calculations in the brute-force approach.
* Used Dynamic Programming to avoid repeated work.
* Optimized space from `O(n)` to `O(1)` by storing only the previous two results.
* Learned that some recursive problems can be converted into efficient iterative solutions.
