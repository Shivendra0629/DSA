'''
--------------------------------------------------------
PROBLEM:

75. Sort Colors

Given an array nums containing only 0s, 1s, and 2s,
sort the array in-place so that all:

0s (Red) come first,
1s (White) come next,
2s (Blue) come last.

You must solve this problem without using Python's
built-in sort() function.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [2,0,2,1,1,0]

Output:

[0,0,1,1,2,2]

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [2,0,1]

Output:

[0,1,2]

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 300

nums[i] is either 0, 1, or 2.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
FIRST APPROACH (Selection Sort Style)

Idea:

1. Traverse the array.
2. Compare the current element with every element
   after it.
3. If a smaller element is found, swap them.
4. Continue until the entire array is sorted.

--------------------------------------------------------
CODE:

class Solution:
    def sortColors(self, nums):

        for i in range(len(nums)):
            for j in range(i, len(nums)):

                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

--------------------------------------------------------
DRY RUN:

Input:

[2,0,2,1,1,0]

Pass 1:

Compare 2 with every element.

Smallest becomes 0.

Array:

[0,2,2,1,1,0]

--------------------------------------------------------

Pass 2:

Compare second element with remaining elements.

Array:

[0,0,2,1,1,2]

--------------------------------------------------------

Pass 3:

Compare third element.

Array:

[0,0,1,2,1,2]

--------------------------------------------------------

Pass 4:

Array:

[0,0,1,1,2,2]

--------------------------------------------------------

Final Output:

[0,0,1,1,2,2]

--------------------------------------------------------
TIME COMPLEXITY:

Outer Loop  : O(n)

Inner Loop  : O(n)

Overall:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Sorting is performed in-place using swapping.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

- Uses nested loops.
- Performs unnecessary comparisons.
- Takes O(n²) time.
- Can be improved to O(n).

--------------------------------------------------------
'''

class Solution:
    def sortColors(self, nums):

        for i in range(len(nums)):
            for j in range(i, len(nums)):

                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


nums = [2,0,2,1,1,0]

obj = Solution()

obj.sortColors(nums)

print(nums)

'''
--------------------------------------------------------
OPTIMAL APPROACH (Dutch National Flag Algorithm)

Idea:

Maintain three pointers.

low  -> Next position of 0

mid  -> Current element

high -> Next position of 2

Rules:

1. nums[mid] == 0

   Swap low and mid

   low += 1

   mid += 1

2. nums[mid] == 1

   mid += 1

3. nums[mid] == 2

   Swap mid and high

   high -= 1

   Do NOT increment mid because the swapped
   element has not been processed yet.

--------------------------------------------------------
CODE:

class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1

--------------------------------------------------------
DRY RUN:

Input:

[2,0,2,1,1,0]

Initially:

low = 0

mid = 0

high = 5

--------------------------------------------------------

Step 1

nums[mid] = 2

Swap mid and high

Array:

[0,0,2,1,1,2]

low = 0

mid = 0

high = 4

--------------------------------------------------------

Step 2

nums[mid] = 0

Swap low and mid

Array:

[0,0,2,1,1,2]

low = 1

mid = 1

--------------------------------------------------------

Step 3

nums[mid] = 0

Swap low and mid

Array:

[0,0,2,1,1,2]

low = 2

mid = 2

--------------------------------------------------------

Step 4

nums[mid] = 2

Swap mid and high

Array:

[0,0,1,1,2,2]

low = 2

mid = 2

high = 3

--------------------------------------------------------

Step 5

nums[mid] = 1

mid = 3

--------------------------------------------------------

Step 6

nums[mid] = 1

mid = 4

Now,

mid > high

Loop Stops.

Final Output:

[0,0,1,1,2,2]

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:

Every element is visited at most once.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only three pointers are used.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

- Single traversal.
- No nested loops.
- Constant extra space.
- In-place sorting.
- Expected interview solution.

--------------------------------------------------------
'''

class Solution:
    def sortColors(self, nums):

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1


nums = [2,0,2,1,1,0]

obj = Solution()

obj.sortColors(nums)

print(nums)

'''
--------------------------------------------------------
EDGE CASES:

1. Already Sorted

Input:

[0,0,1,1,2,2]

Output:

[0,0,1,1,2,2]

--------------------------------------------------------

2. Reverse Order

Input:

[2,2,1,1,0,0]

Output:

[0,0,1,1,2,2]

--------------------------------------------------------

3. All Elements Same

Input:

[1,1,1]

Output:

[1,1,1]

--------------------------------------------------------

4. Single Element

Input:

[2]

Output:

[2]

--------------------------------------------------------

5. Empty Regions

Input:

[0,0,0]

Output:

[0,0,0]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"My first solution uses a Selection Sort style
approach. It compares every element with the
remaining elements and swaps whenever a smaller
element is found. This correctly sorts the array
without using Python's built-in sort() function.
However, its time complexity is O(n²).

The optimal solution is the Dutch National Flag
Algorithm. It maintains three pointers:
low, mid, and high.

The region before low contains all 0s,
the region after high contains all 2s,
and mid scans the unknown region.

Depending on whether the current element is 0,
1, or 2, I perform the required swap and move
the pointers accordingly.

This completes the sorting in one traversal with
O(n) time complexity and O(1) extra space."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Selection Sort
3. Swapping
4. Nested Loops
5. In-place Sorting
6. Time Complexity Analysis
7. Space Complexity Analysis
8. Dutch National Flag Algorithm
9. Three Pointer Technique
10. Dry Run Analysis

--------------------------------------------------------
'''