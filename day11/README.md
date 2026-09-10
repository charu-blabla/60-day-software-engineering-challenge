# Move Zeroes

## Approach

The goal is to move all `0`s to the end of the array while keeping the order of the non-zero elements unchanged.

I used a **two-step approach**:

1. **Move all non-zero elements to the front**

   * `count` keeps track of the position where the next non-zero element should be placed.
   * Traverse through the array.
   * Whenever a non-zero element is found, place it at `nums[count]` and increment `count`.

2. **Fill the remaining positions with zeroes**

   * After all non-zero elements are placed, `count` represents the position from where zeroes should start.
   * Fill the rest of the array with `0`.

### Example

For:

`[0, 1, 0, 3, 12]`

After moving non-zero elements:

`[1, 3, 12, 3, 12]`

Then fill the remaining positions with zeroes:

`[1, 3, 12, 0, 0]`

### Complexity

* **Time Complexity:** `O(n)` — the array is traversed a constant number of times.
* **Space Complexity:** `O(1)` — no extra array is used; the changes are made in-place.

### Key Idea

Use a pointer (`count`) to keep track of where the next non-zero element belongs, then fill everything after it with zeroes.
