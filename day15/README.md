# Contains Duplicate

## Approaches

### Brute Force

The brute-force approach uses two loops to compare each element with every other element. If two elements are equal, a duplicate is found.

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(1)`

### Optimized Using Set

The optimized approach converts the array into a set. Since a set only stores unique values, comparing the lengths of the original array and the set determines whether duplicates exist.

* **Time Complexity:** `O(n)` average
* **Space Complexity:** `O(n)`

## Execution Speed Comparison

Both approaches were tested using arrays of different sizes.

 |          Brute Force |         Set |
 | :-------------------: | :----------: |
 |               32ms |      8ms |


*Exact execution times depend on the system and test data.*

## Observations

The set-based approach performs significantly better as the input size increases. The brute-force solution has `O(n²)` time complexity, so its execution time grows rapidly with the size of the input.

The set-based solution has an average time complexity of `O(n)`, making it more suitable for large datasets. It uses additional memory to store the set, but the improvement in execution speed makes this trade-off worthwhile.
