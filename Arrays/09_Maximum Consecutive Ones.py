'''
--------------------------------------------------------
PROBLEM:

485. Max Consecutive Ones

Given a binary array nums, return the maximum
number of consecutive 1's in the array.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [1,1,0,1,1,1]

Output:

3

Explanation:

The first two 1's are consecutive.

The last three 1's are also consecutive.

The maximum consecutive 1's are 3.

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [1,0,1,1,0,1]

Output:

2

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 10^5

nums[i] is either 0 or 1.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
BRUTE FORCE APPROACH:

For every index:

1. Start counting consecutive 1's.
2. Continue until a 0 is found.
3. Store the maximum count obtained.

--------------------------------------------------------
TIME COMPLEXITY:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

The same elements are checked multiple times,
making it inefficient for large arrays.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH:

1. Traverse the array once.

2. If the current element is 1:
      - Increase the current count.
      - Update the maximum count.

3. If the current element is 0:
      - Reset the current count to 0.

4. Return the maximum count.

--------------------------------------------------------
CODE:
'''
class Solution:
    def maxCon(self, nums):
        n = len(nums)

        count = 0
        max_1 = 0

        for i in range(n):

            if nums[i] == 1:
                count += 1
                max_1 = max(max_1, count)

            else:
                count = 0

        return max_1

obj = Solution()

print(obj.maxCon([1,1,0,1,1,1,1,0,1,1,1]))

'''
--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Explanation:

The array is traversed only once.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

Only two extra variables are used:

1. count
2. max_1

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL:

- Only one traversal is required.
- No extra data structure is used.
- Satisfies the best possible time complexity.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. All elements are 1.

Example:

[1,1,1,1]

Output:

4


2. All elements are 0.

Example:

[0,0,0]

Output:

0


3. Only one element.

Example:

[1]

Output:

1


4. Consecutive 1's at the beginning.

Example:

[1,1,0,0]

Output:

2


5. Consecutive 1's at the end.

Example:

[0,0,1,1,1]

Output:

3

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"We traverse the array once while maintaining
two variables.

The first variable keeps track of the current
streak of consecutive 1's.

The second variable stores the maximum streak
found so far.

Whenever a 0 is encountered, the current streak
is reset to 0 because the sequence of consecutive
1's is broken.

This gives an O(n) time and O(1) space solution."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays.
2. Linear Traversal.
3. Counting Technique.
4. Maximum Tracking.
5. Conditional Statements.
6. Time Complexity Analysis.
7. Space Complexity Analysis.
8. Edge Case Handling.

--------------------------------------------------------
'''