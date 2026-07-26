'''
--------------------------------------------------------
PROBLEM:

1752. Check if Array Is Sorted and Rotated

Given an array nums, return True if the array was originally
sorted in non-decreasing order and then rotated some number
of positions (including zero). Otherwise, return False.

Note:
- There may be duplicate elements in the array.
- The array is considered circular while checking rotation.

--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Create a copy of the given array.
2. Sort the array in non-decreasing order.
3. Compare the sorted array with the original array.
4. If they are not equal, rotate the sorted array one position
   at a time and compare it with the original array.
5. If any rotation matches the original array, return True.
6. Otherwise, return False.

Time Complexity:
- O(n²) or more (sorting + multiple rotations + comparisons)

Space Complexity:
- O(n)

Why is it not optimal?
- Sorting the array is unnecessary.
- Performing rotations repeatedly is expensive.
- The problem can be solved using a simple observation in a
  single traversal.

--------------------------------------------------------
OPTIMAL APPROACH:

1. Traverse the array only once.
2. Count the number of times an element is greater than its
   next element.
3. Treat the array as circular by comparing the last element
   with the first element using modulo (%).
4. If the count of such violations is greater than one,
   return False.
5. Otherwise, return True.

Observation:
- A sorted array can have at most one break point.
- A sorted and rotated array can also have at most one break point.
- More than one break point means the array is invalid.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Explanation:

- We traverse the entire array exactly once.
- Each comparison takes constant time.

Therefore, the overall time complexity is O(n).

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

- Only two extra variables are used:
      1. count
      2. n

- No additional data structures are created.

Hence, the space complexity is O(1).

--------------------------------------------------------
EDGE CASES:

1. Array is already sorted.
   Example: [1, 2, 3]

2. Array is sorted and rotated.
   Example: [3, 4, 5, 1, 2]

3. Array contains duplicate elements.
   Example: [1, 1, 1]

4. Array is not sorted and rotated.
   Example: [2, 1, 3, 4]

5. Array contains only one element.
   Example: [5]

--------------------------------------------------------
OPTIMAL?

YES

Reason:

- We traverse the array only once.
- No sorting or actual rotation is performed.
- Every element is inspected at most once.
- O(n) is the best possible time complexity for this problem.

--------------------------------------------------------
INTERVIEW EXPLANATION:

"We treat the array as circular and count the number of
places where the sorted order breaks. A valid sorted and
rotated array can have at most one such break point.
If the count exceeds one, the array cannot be sorted and
rotated. This approach achieves O(n) time complexity and
O(1) auxiliary space complexity."

--------------------------------------------------------
'''

class Solution:
    def check(self, nums) -> bool:

        count = 0
        n = len(nums)

        for i in range(n):

            # Circular comparison
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        if count<=1:
            return True
        else:
            return False
        


obj = Solution()

print(obj.check([3, 4, 5, 1, 2]))  
print(obj.check([2, 1, 4, 3, 4]))      
print(obj.check([1, 2, 3]))         
print(obj.check([1, 1, 1]))         
print(obj.check([4, 5, 1, 2, 3]))   

'''
--------------------------------------------------------
CONCEPTS USED:

1. Array Traversal.
2. Circular Traversal.
3. Modulo Operator (%).
4. Conditional Statements.
5. Time Complexity Analysis.
6. Space Complexity Analysis.
7. Observation-Based Problem Solving.

--------------------------------------------------------
'''