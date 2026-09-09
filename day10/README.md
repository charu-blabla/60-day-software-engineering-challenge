# Maximum Subarray

This solution finds the **maximum sum of a contiguous subarray** using **Kadane's Algorithm**.

## Approach

The idea is to keep track of two values:

* `currentSum` → Maximum sum of a subarray ending at the current element.
* `maxSum` → Maximum subarray sum found so far.

For every number, we decide whether to:

1. Start a new subarray from the current number.
2. Add the current number to the previous subarray.

```python
currentSum = max(i, currentSum + i)
```

This chooses whichever option gives a larger sum.

Then we update the overall maximum:

```python
maxSum = max(maxSum, currentSum)
```

## Example

For:

```text
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The maximum subarray is:

```text
[4, -1, 2, 1]
```

Maximum sum:

```text
6
```

## Complexity

* **Time Complexity:** `O(n)` — The array is traversed once.
* **Space Complexity:** `O(1)` — Only two variables are used.
