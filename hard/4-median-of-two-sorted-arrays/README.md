# Median of Two Sorted Arrays

**Link:** [LeetCode Problem 4](https://leetcode.com/problems/median-of-two-sorted-arrays)

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

## Examples

### Example 1

**Input:** `nums1 = [1,3]`, `nums2 = [2]`

**Output:** `2.00000`

**Explanation:** merged array = `[1,2,3]` and median is `2`.

### Example 2

**Input:** `nums1 = [1,2]`, `nums2 = [3,4]`

**Output:** `2.50000`

**Explanation:** merged array = `[1,2,3,4]` and median is `(2 + 3) / 2 = 2.5`.

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Acceptance

- **Accepted:** 4,217,468 / 9.1M
- **Acceptance Rate:** 46.4%

## Companies

This problem is frequently asked by multiple companies (refer to LeetCode for current list).

## Notes

- The expected time complexity is **O(log(m+n))**.
- You cannot simply merge the arrays first (that would be O(m+n)).
- Both arrays are already sorted.
- Empty arrays are possible in test cases (e.g., `nums1 = []`, `nums2 = [1]`).
