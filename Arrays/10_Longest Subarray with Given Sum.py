'''
--------------------------------------------------------
PROBLEM:

Longest Subarray with Sum K

Given an integer array arr[] and an integer k,
find the length of the longest subarray whose
sum of elements is equal to k.

If no such subarray exists, return 0.

--------------------------------------------------------
EXAMPLE 1:

Input:

arr = [10, 5, 2, 7, 1, -10]
k = 15

Output:

6

Explanation:

Possible subarrays with sum = 15:

[10,5]                    -> Length = 2

[5,2,7,1]                 -> Length = 4

[10,5,2,7,1,-10]          -> Length = 6

Longest length = 6

--------------------------------------------------------
EXAMPLE 2:

Input:

arr = [-5,8,-14,2,4,12]
k = -5

Output:

5

--------------------------------------------------------
CONSTRAINTS:

1 <= arr.length <= 10^5

-10^4 <= arr[i] <= 10^4

-10^9 <= k <= 10^9

--------------------------------------------------------
'''

'''
--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Start from every index.

2. Extend the subarray one element at a time.

3. Keep calculating the current sum.

4. Whenever current sum becomes equal to k:
      - Calculate the subarray length.
      - Update the maximum length.

--------------------------------------------------------
CODE:
'''

class Solution:
    def longestSubarray(self, arr, k):

        max_length = 0

        for i in range(len(arr)):

            curr_sum = 0

            for j in range(i, len(arr)):

                curr_sum += arr[j]

                if curr_sum == k:

                    length = j - i + 1

                    max_length = max(max_length, length)

        return max_length
obj=Solution()
print(obj.longestSubarray([1,2,3,4,5,1,6,4],10))
'''
--------------------------------------------------------
TIME COMPLEXITY:

O(n²)

Explanation:

- Outer loop runs n times.
- Inner loop runs up to n times.

Therefore:

O(n) × O(n) = O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

Only a few extra variables are used:

1. curr_sum
2. length
3. max_length

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

- Every possible subarray is checked.
- Many sums are recalculated repeatedly.
- Becomes slow for large arrays.

An optimal HashMap approach exists with
O(n) time complexity.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. No subarray has sum = k.

Example:

arr = [1,2,3]
k = 10

Output:

0


2. Entire array has sum = k.

Example:

arr = [1,2,3]

k = 6

Output:

3


3. Only one element equals k.

Example:

arr = [5]

k = 5

Output:

1


4. Array contains negative numbers.

Example:

arr = [-5,8,-14,2,4,12]

The brute force approach still works correctly.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"We generate every possible subarray using
two nested loops.

The outer loop selects the starting index,
while the inner loop extends the subarray
one element at a time.

We maintain a running sum and whenever it
becomes equal to k, we calculate the current
subarray length and update the maximum length.

Although this solution is simple and easy to
understand, it has O(n²) time complexity.
A HashMap-based solution can improve it to O(n)."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays.
2. Subarrays.
3. Nested Loops.
4. Running Sum.
5. Brute Force Technique.
6. Maximum Tracking.
7. Time Complexity Analysis.
8. Space Complexity Analysis.

--------------------------------------------------------
'''