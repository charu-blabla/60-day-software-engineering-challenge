# Top K Frequent Elements

## Approach

The solution uses a **hash map (dictionary)** to count how many times each number appears in the array.

1. Create a dictionary `freq` to store each number and its frequency.
2. Iterate through `nums` and update the frequency of each number.
3. Sort the dictionary items based on:

   * Frequency in **descending order**.
   * Number in **ascending order** when frequencies are equal.
4. Take the first `k` elements from the sorted list.
5. Return those `k` numbers.

### Example

For:

`nums = [1,1,1,2,2,3]`, `k = 2`

The frequency map becomes:

`{1: 3, 2: 2, 3: 1}`

After sorting:

`[(1,3), (2,2), (3,1)]`

The first 2 elements are:

`[1, 2]`

## Complexity

* **Time:** `O(n + m log m)`

  * `n` = number of elements in `nums`
  * `m` = number of unique elements
  * Counting frequencies takes `O(n)`.
  * Sorting the unique elements takes `O(m log m)`.

* **Space:** `O(m)`

  * The frequency dictionary stores each unique element.
