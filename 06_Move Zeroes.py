'''
--------------------------------------------------------
PROBLEM:

283. Move Zeroes

Given an integer array nums, move all 0's to the end
while maintaining the relative order of non-zero elements.

The operation must be performed in-place.

--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Traverse the array multiple times.
2. Whenever a zero is found, swap it with the next element.
3. Repeat until all zeroes reach the end.

Time Complexity:
O(n²)

Space Complexity:
O(1)

Reason:
Many unnecessary swaps are performed.

--------------------------------------------------------
OPTIMAL APPROACH:

Use Two Pointers.

i -> Traverses the array.

j -> Stores the index where the next non-zero element
should be placed.

Whenever nums[i] is non-zero:

Swap nums[i] and nums[j]

Increment j.

--------------------------------------------------------
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
object=Solution()
print(object.moveZeroes([1,0,2,0,2,3]))
print(object.moveZeroes([0,0,2,30,0]))
print(object.moveZeroes([0,1,0,3,12]))
print(object.moveZeroes([1,5,0,6,5,0]))


'''
--------------------------------------------------------
ANOTHER APPROACH (Using Extra Array)

non_zero = []
zero_count = 0

for num in nums:
    if num == 0:
        zero_count += 1
    else:
        non_zero.append(num)

nums[:] = non_zero + [0] * zero_count

Time Complexity:
O(n)

Space Complexity:
O(n)

Reason:
Uses an extra array.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:
The array is traversed only once.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:
Only two pointers (i and j) are used.

--------------------------------------------------------
EDGE CASES:

1. Single element.
2. All zeroes.
3. No zeroes.
4. Zeroes already at the end.
5. Negative numbers.

--------------------------------------------------------
INTERVIEW EXPLANATION:

"We use the Two Pointer Technique.
Pointer i traverses the array while pointer j keeps
track of where the next non-zero element should be placed.
Whenever a non-zero element is found, we swap it with
nums[j]. This keeps the relative order intact while
moving all zeroes to the end."

--------------------------------------------------------
CONCEPTS USED:

1. Two Pointer Technique
2. Array Traversal
3. In-place Modification
4. Swapping
5. Time & Space Complexity Analysis

--------------------------------------------------------
'''