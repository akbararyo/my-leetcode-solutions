# 4 Longest Substring Without Repeating Characters

**Link:** [LeetCode Problem 3](https://leetcode.com/problems/longest-substring-without-repeating-characters)

## Problem

Given a string `s`, find the length of the **longest substring** without duplicate characters.

## Examples

### Example 1

**Input:** `s = "abcabcbb"`

**Output:** `3`

**Explanation:** The answer is `"abc"`, with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

### Example 2

**Input:** `s = "bbbbb"`

**Output:** `1`

**Explanation:** The answer is `"b"`, with the length of 1.

### Example 3

**Input:** `s = "pwwkew"`

**Output:** `3`

**Explanation:** The answer is `"wke"`, with the length of 3. Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Test Cases to Consider

- `" "` (single space)
- `"dvdf"`
- `"ckilbkd"`
- `"tmmzuxt"`

## Notes

- The answer must be a **substring** (contiguous), not a subsequence.
- The maximum string size is at most 5 × 10⁴.
- Brute force approaches may not pass due to time constraints.

## Acceptance

- **Accepted:** 9,382,740 / 24.1M
- **Acceptance Rate:** 38.9%

## Companies

This problem is frequently asked by multiple companies (refer to LeetCode for current list).
