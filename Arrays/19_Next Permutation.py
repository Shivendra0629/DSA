
'''
--------------------------------------------------------
PROBLEM:

31. Next Permutation

Given an array of integers nums, find the next
lexicographically greater permutation of nums.

If no greater permutation is possible, rearrange the
array into the lowest possible order, which means
ascending order.

The modification must be done in-place and use only
constant extra memory.

--------------------------------------------------------
EXAMPLES:

Example 1:

Input:
nums = [1,2,3]

Output:
[1,3,2]

--------------------------------------------------------

Example 2:

Input:
nums = [3,2,1]

Output:
[1,2,3]

--------------------------------------------------------

Example 3:

Input:
nums = [1,1,5]

Output:
[1,5,1]

--------------------------------------------------------
APPROACH 1:

The idea is to find the next greater permutation
using three steps.

Step 1:

Find the pivot.

Starting from the right side, find the first
position where:

nums[i] < nums[i + 1]

This position is the pivot.

Step 2:

Find the first element from the right that is
greater than the pivot.

Swap the pivot with that element.

Step 3:

Reverse the part of the array after the pivot.

The suffix is originally in decreasing order.
Reversing it makes it the smallest possible
arrangement.

If no pivot exists, the entire array is in
descending order.

That means the current permutation is the largest
possible permutation.

Therefore, reverse the entire array.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

The array is traversed a constant number of times.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Only a few variables are used.

The modification is done in-place.

--------------------------------------------------------
WHY IS THIS OPTIMAL?

- No extra array is required.
- No permutations need to be generated.
- The array is modified in-place.
- Only constant extra memory is used.
- Time complexity is O(n).
- Space complexity is O(1).

--------------------------------------------------------
APPROACH 2:

The second approach uses the same algorithm.

The only difference is how the pivot is found.

Approach 1 uses a while loop.

Approach 2 uses a for loop and stores the starting
position of the suffix in the variable pivot.

If no pivot is found, the array is in descending
order, so reversing the entire array gives the
smallest permutation.

--------------------------------------------------------
INTERVIEW EXPLANATION:

First, I find the pivot by scanning the array from
right to left.

The pivot is the first element that is smaller than
the element immediately after it.

Then I find the smallest element from the right side
that is greater than the pivot and swap them.

After the swap, I reverse the suffix because the
suffix is in decreasing order and reversing it gives
the smallest possible arrangement.

If there is no pivot, the array is already the largest
permutation, so I reverse the complete array.

The time complexity is O(n) and the space complexity
is O(1).

--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Permutations
3. Lexicographical Order
4. Greedy Technique
5. Pivot
6. Two Pointers
7. Swapping
8. Reversing
9. In-place Modification
10. Time Complexity
11. Space Complexity
12. Constant Extra Space

--------------------------------------------------------
'''

class Solution:
    def nextPermutation(self, nums):

        n = len(nums)

        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:

            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

        return nums


obj = Solution()

print(obj.nextPermutation([1, 3, 2, 6, 5]))
print(obj.nextPermutation([1, 2, 3]))
print(obj.nextPermutation([3, 2, 1]))
print(obj.nextPermutation([1, 1, 5]))


class Solution:
    def nextPermutation(self, nums):

        n = len(nums)

        pivot = 0

        for i in range(n - 1, 0, -1):

            if nums[i - 1] < nums[i]:
                pivot = i
                break

        if pivot == 0:
            nums.reverse()
            return nums

        swap = n - 1

        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]

        nums[pivot:] = reversed(nums[pivot:])

        return nums


obj = Solution()

print(obj.nextPermutation([1, 3, 2, 6, 5]))
print(obj.nextPermutation([1, 2, 3]))
print(obj.nextPermutation([3, 2, 1]))
print(obj.nextPermutation([1, 1, 5]))

