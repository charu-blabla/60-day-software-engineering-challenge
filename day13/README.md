# Valid Anagram

## Approach

The solution checks whether two strings are anagrams by comparing the frequency of each character.

### Steps

1. First, check if both strings have the same length.

   * If their lengths are different, they cannot be anagrams.
2. Create two dictionaries:

   * `freqS` stores the frequency of each character in `s`.
   * `freqT` stores the frequency of each character in `t`.
3. Count how many times each character appears in both strings.
4. Compare the two dictionaries.

   * If they are equal, the strings are anagrams.
   * Otherwise, they are not.

For example:

```text
s = "aabbc"
t = "abcab"

freqS = {a: 2, b: 2, c: 1}
freqT = {a: 2, b: 2, c: 1}

→ True
```

## Complexity

### Frequency Map Approach

* **Time:** `O(n)`
* **Space:** `O(n)`

Each character is processed once, and the dictionaries store the character frequencies.

### Brute Force Approach

A brute-force method could repeatedly search for a matching character in the other string and remove it once found.

* **Time:** `O(n²)`
* **Space:** `O(n)`

This is slower because for each character, we may need to search through the other string.

## Comparison

| Approach      |    Time |  Space |
| ------------- | ------: | -----: |
| Brute Force   | `O(n²)` | `O(n)` |
| Frequency Map |  `O(n)` | `O(n)` |

The **frequency map approach is more efficient** because it avoids repeatedly searching through the strings.
