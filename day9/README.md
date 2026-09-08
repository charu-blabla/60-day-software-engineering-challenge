# Prefix Sum - Complexity Comparison

### Brute Force

For every `sumRange()` query, we loop through all elements between `left` and `right`.

* **Time:** `O(n)` per query
* **Space:** `O(1)`

### Optimized - Prefix Sum

We calculate the prefix sums once in `O(n)`. After that, each range sum only requires a subtraction.

* **Time:** `O(n)` preprocessing + `O(1)` per query
* **Space:** `O(n)`

### Comparison

| Approach    | Time per Query | Space  |
| ----------- | -------------- | ------ |
| Brute Force | `O(n)`         | `O(1)` |
| Prefix Sum  | `O(1)`         | `O(n)` |

The optimized approach is better when there are **many queries**, because each query takes only `O(1)` time.
