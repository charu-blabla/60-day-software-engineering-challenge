# Reverse String

## Approach

The string is reversed **in-place** using two pointers:

* `start` points to the first element.
* `end` points to the last element.
* Swap the elements at `start` and `end`.
* Move `start` forward and `end` backward.
* Continue until the pointers meet.

Python's multiple assignment makes swapping simple:

`s[start], s[end] = s[end], s[start]`

Since the list is modified directly, no extra list is needed.

## Example

For:

`["h", "e", "l", "l", "o"]`

The swaps happen like:

`["o", "e", "l", "l", "h"]`
`["o", "l", "l", "e", "h"]`

Result:

`["o", "l", "l", "e", "h"]`

## Complexity

* **Time Complexity:** O(n) — each element is processed at most once.
* **Space Complexity:** O(1) — the reversal is done in-place.
