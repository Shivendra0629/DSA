'''
--------------------------------------------------------
PROBLEM:

53. Maximum Subarray

Given an integer array nums, find the contiguous
subarray having the largest sum and return its sum.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:

6

Explanation:

The subarray

[4,-1,2,1]

has the largest sum.

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [1]

Output:

1

--------------------------------------------------------
EXAMPLE 3:

Input:

nums = [5,4,-1,7,8]

Output:

23

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 10^5

-10^4 <= nums[i] <= 10^4

--------------------------------------------------------
'''

'''
--------------------------------------------------------
APPROACH 1 (Brute Force)

Idea:

Generate every possible contiguous subarray.

For every starting index:

1. Initialize current sum as 0.
2. Extend the subarray one element at a time.
3. Update the maximum sum whenever a larger
   subarray sum is found.

--------------------------------------------------------
CODE:

class Solution:
    def Maxsub(self, nums):

        max_sum = float('-inf')

        for i in range(len(nums)):

            curr_sum = 0

            for j in range(i, len(nums)):

                curr_sum += nums[j]

                max_sum = max(max_sum, curr_sum)

        return max_sum

--------------------------------------------------------
DRY RUN:

Input:

nums = [0,1,-2,3,4]

--------------------------------------------------------

Start i = 0

Subarrays:

[0]             Sum = 0

[0,1]           Sum = 1

[0,1,-2]        Sum = -1

[0,1,-2,3]      Sum = 2

[0,1,-2,3,4]    Sum = 6

Maximum = 6

--------------------------------------------------------

Start i = 1

[1]             Sum = 1

[1,-2]          Sum = -1

[1,-2,3]        Sum = 2

[1,-2,3,4]      Sum = 6

Maximum = 6

--------------------------------------------------------

Start i = 2

[-2]            Sum = -2

[-2,3]          Sum = 1

[-2,3,4]        Sum = 5

--------------------------------------------------------

Start i = 3

[3]             Sum = 3

[3,4]           Sum = 7

Maximum = 7

--------------------------------------------------------

Start i = 4

[4]             Sum = 4

--------------------------------------------------------

Answer:

7

--------------------------------------------------------
TIME COMPLEXITY:

Outer Loop : O(n)

Inner Loop : O(n)

Overall:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

Although correct, every possible subarray is
generated.

For large arrays (n = 10^5), this results in
Time Limit Exceeded (TLE).

--------------------------------------------------------
'''

class Solution:
    def Maxsub(self, nums):

        max_sum = float('-inf')

        for i in range(len(nums)):

            curr_sum = 0

            for j in range(i, len(nums)):

                curr_sum += nums[j]

                max_sum = max(max_sum, curr_sum)

        return max_sum


obj = Solution()

print(obj.Maxsub([0,1,-2,3,4]))
print(obj.Maxsub([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.Maxsub([5,4,-1,7,8]))
print(obj.Maxsub([1]))

'''
--------------------------------------------------------
OPTIMAL APPROACH (Kadane's Algorithm)

Idea:

At every element, we have two choices:

1. Continue the previous subarray.

or

2. Start a new subarray from the current element.

Choose whichever gives the larger sum.

--------------------------------------------------------
CODE:

class Solution:
    def MaxsubArray(self, nums):

        curr_sum = nums[0]

        max_sum = nums[0]

        for i in range(1, len(nums)):

            curr_sum = max(nums[i], curr_sum + nums[i])

            max_sum = max(max_sum, curr_sum)

        return max_sum

--------------------------------------------------------
DRY RUN:

Input:

nums = [0,1,-2,3,4]

Initially:

curr_sum = 0

max_sum = 0

--------------------------------------------------------

Current Element = 1

Continue Previous:

0 + 1 = 1

Start New:

1

Maximum = 1

curr_sum = 1

max_sum = 1

--------------------------------------------------------

Current Element = -2

Continue Previous:

1 + (-2) = -1

Start New:

-2

Maximum = -1

curr_sum = -1

max_sum = 1

--------------------------------------------------------

Current Element = 3

Continue Previous:

-1 + 3 = 2

Start New:

3

Maximum = 3

curr_sum = 3

max_sum = 3

--------------------------------------------------------

Current Element = 4

Continue Previous:

3 + 4 = 7

Start New:

4

Maximum = 7

curr_sum = 7

max_sum = 7

--------------------------------------------------------

Answer:

7

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:

Only one traversal of the array.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only two variables are used.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

Instead of checking every possible subarray,
Kadane's Algorithm intelligently decides whether
to continue the previous subarray or start a new
one.

This reduces the complexity from O(n²) to O(n).

--------------------------------------------------------
'''

class Solution:
    def MaxsubArray(self, nums):

        curr_sum = nums[0]

        max_sum = nums[0]

        for i in range(1, len(nums)):

            curr_sum = max(nums[i], curr_sum + nums[i])

            max_sum = max(max_sum, curr_sum)

        return max_sum


obj = Solution()

print(obj.MaxsubArray([0,1,-2,3,4]))
print(obj.MaxsubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.MaxsubArray([5,4,-1,7,8]))
print(obj.MaxsubArray([1]))

'''
--------------------------------------------------------
EDGE CASES:

1. Single Element

Input:

[5]

Output:

5

--------------------------------------------------------

2. Single Negative Element

Input:

[-5]

Output:

-5

--------------------------------------------------------

3. All Negative Numbers

Input:

[-2,-4,-1,-8]

Output:

-1

--------------------------------------------------------

4. All Positive Numbers

Input:

[1,2,3,4]

Output:

10

--------------------------------------------------------

5. Mixed Positive and Negative

Input:

[-2,1,-3,4,-1,2,1,-5,4]

Output:

6

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"My first solution generates every possible
contiguous subarray and calculates its sum.
Although it is correct, it requires O(n²)
time and causes Time Limit Exceeded for large
inputs.

The optimal solution is Kadane's Algorithm.

At every element, I decide whether it is better
to continue the previous subarray or start a new
subarray from the current element.

This allows me to find the maximum subarray sum
in a single traversal.

Time Complexity becomes O(n) and Space Complexity
remains O(1)."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Nested Loops
3. Contiguous Subarray
4. Running Sum
5. Maximum Subarray Sum
6. Kadane's Algorithm
7. Dynamic Programming (Greedy DP)
8. Time Complexity Analysis
9. Space Complexity Analysis
10. Dry Run Analysis

--------------------------------------------------------
'''