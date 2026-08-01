'''
--------------------------------------------------------
PROBLEM:

1. Two Sum

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they
add up to the target.

You may assume that each input has exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [2,7,11,15]
target = 9

Output:

[0,1]

Explanation:

nums[0] + nums[1] = 2 + 7 = 9

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [3,2,4]
target = 6

Output:

[1,2]

--------------------------------------------------------
EXAMPLE 3:

Input:

nums = [3,3]
target = 6

Output:

[0,1]

--------------------------------------------------------
CONSTRAINTS:

2 <= nums.length <= 10^4

-10^9 <= nums[i] <= 10^9

-10^9 <= target <= 10^9

Exactly one valid answer exists.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
FIRST APPROACH (Brute Force)

1. Traverse the array using the first loop.
2. For every element, check all remaining elements.
3. If the sum of two elements equals the target,
   return their indices.

--------------------------------------------------------
CODE:

class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]

--------------------------------------------------------
TIME COMPLEXITY:

Outer Loop : O(n)

Inner Loop : O(n)

Overall:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

No extra data structure is used.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

Every possible pair is checked.

Many unnecessary comparisons are performed,
making it inefficient for large arrays.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH (Hash Map / Dictionary)

Concept:

1. Traverse the array once.
2. Calculate the required complement:

       target - nums[i]

3. If the complement is already present in the
   dictionary, return both indices.
4. Otherwise, store the current element and its index
   in the dictionary.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n)

Reason:

The dictionary stores array elements and their indices.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

- Only one traversal of the array.
- Faster than checking every pair.
- Meets the expected linear time complexity.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. Target formed by the first two elements.

Input:

nums = [2,7,11,15]
target = 9

Output:

[0,1]

--------------------------------------------------------

2. Duplicate elements.

Input:

nums = [3,3]
target = 6

Output:

[0,1]

--------------------------------------------------------

3. Negative numbers.

Input:

nums = [-3,4,3,90]
target = 0

Output:

[0,2]

--------------------------------------------------------

4. Target formed by the last two elements.

Input:

nums = [1,2,3,4]
target = 7

Output:

[2,3]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"The brute force approach checks every possible pair
of elements and returns the indices when their sum
equals the target. Since two nested loops are used,
the time complexity is O(n²).

The optimal solution uses a Hash Map (Dictionary) to
store previously visited elements and their indices.
For every element, we check whether its complement
(target - current element) already exists in the
dictionary. This reduces the time complexity to O(n)."

--------------------------------------------------------
'''

class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]


obj = Solution()

print(obj.twoSum([1,2,3,4], 6))
print(obj.twoSum([2,7,11,15], 9))
print(obj.twoSum([3,2,4], 6))
print(obj.twoSum([3,3], 6))

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Nested Loops
3. Brute Force
4. Pair Traversal
5. Hash Map (Optimal Approach)
6. Time Complexity Analysis
7. Space Complexity Analysis
8. Index-Based Traversal

--------------------------------------------------------
'''