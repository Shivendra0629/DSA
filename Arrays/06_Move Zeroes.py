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
class Solution:

    def MoveZeroes(self, nums):

        n = len(nums)

        for i in range(n):

            for j in range(n-1):

                if nums[j] == 0:

                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums
--------------------------------------------------------
TIME COMPLEXITY:

Outer loop:

Runs n times.

O(n)

Inner loop:

Runs (n - 1) times for every iteration of the outer loop.

O(n - 1)

Total Time Complexity:

O(n) × O(n - 1)

= O(n² - n)

In Big-O notation, we ignore lower-order terms.

Therefore,

Time Complexity:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

No extra array or data structure is created.

Only swapping is performed using the existing array.

--------------------------------------------------------
WHY IS THIS NOT AN OPTIMAL APPROACH?

1. The array is traversed multiple times.

2. Even after a zero reaches the end,
   the algorithm continues checking and swapping.

3. Many unnecessary comparisons and swaps are performed.

4. The same elements may be visited repeatedly.

Hence, the algorithm takes O(n²) time,
which is inefficient for large input sizes.

A Two Pointer approach solves the same problem
in O(n) time and O(1) extra space.

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