# Subsets — Recursion & Backtracking

## Problem

Given an array of distinct integers, return all possible subsets.

For example:

```text
Input: [1, 2]

Output: [[1, 2], [1], [2], []]
```

## Approach

I used **recursion and backtracking**. For every element, we have two choices:

1. Include the element in the current subset.
2. Exclude the element from the current subset.

The recursive function handles these two possibilities by:

* Adding the current element using `append()`.
* Recursively exploring the next element.
* Removing the element using `pop()` to **backtrack**.
* Recursively exploring the branch where the element is excluded.

When `i` reaches the length of `nums`, a complete subset has been formed and is added to `allSubsets`.

A copy of `ans` is stored using `ans[:]` because `ans` is the same list that keeps changing during backtracking.

## Recursive Tree

For `nums = [1, 2]`:

```text
                    []
                  /    \
               include  exclude
                 [1]      []
                /   \    /   \
             [1,2] [1] [2]   []
```

Each path from the root to a leaf represents one possible subset.

So the final result is:

```text
[[1, 2], [1], [2], []]
```

## Why Backtracking?

`ans` is used as a temporary working list.

For example:

```text
ans = []
  ↓
add 1
  ↓
ans = [1]
  ↓
add 2
  ↓
ans = [1, 2]
  ↓
remove 2
  ↓
ans = [1]
```

After exploring one choice, `pop()` removes it so that we can explore the other choice without creating a completely new working list each time.

## Complexity

For `n` elements, each element has 2 choices (include or exclude), giving `2^n` subsets.

* **Time Complexity:** `O(n × 2^n)` — there are `2^n` subsets and copying a subset can take up to `O(n)`.
* **Space Complexity:** `O(n × 2^n)` — storing all `2^n` subsets, with each subset containing up to `n` elements.
* **Recursion Stack:** `O(n)`.

## Key Learning

This problem helped me understand the **include/exclude pattern**, recursion trees, and the **choose → explore → undo** pattern used in backtracking.
