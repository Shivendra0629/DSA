'''
--------------------------------------------------------
PROBLEM:

26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element
appears only once.

Return the number of unique elements present in the array.

The first k elements of the array should contain all unique
elements in sorted order. The remaining elements can be ignored.

--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Create a new array or set to store unique elements.
2. Traverse the given array and store only distinct elements.
3. Copy the unique elements back into the original array.
4. Return the count of unique elements.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Why is it not optimal?
- The problem specifically asks for an in-place solution.
- Using an additional data structure violates the space constraint.

--------------------------------------------------------
OPTIMAL APPROACH:

1. Initialize a pointer 'i' at index 0.
2. Traverse the array using another pointer 'k' starting from index 1.
3. Whenever a new unique element is found:
      - Increment i by 1.
      - Store the unique element at nums[i].
4. Continue traversing the array.
5. Return i + 1, which represents the total number of unique elements.

This approach modifies the original array in-place without using
any extra space.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Explanation:

- The array is traversed exactly once.
- Each element is compared at most one time.

Hence, the time complexity is O(n).

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

- Only two extra variables are used:
      1. i
      2. k

- No additional data structures are created.

Hence, the space complexity is O(1).

--------------------------------------------------------
EDGE CASES:

1. Array contains only one element.
2. Array contains all duplicate elements.
3. Array contains no duplicates.
4. Array contains negative numbers.
5. Array size is large.
6. Array is already unique.

--------------------------------------------------------
OPTIMAL?

YES

Reason:

- The array is traversed only once.
- No extra memory is used.
- The solution satisfies the in-place modification requirement.
- O(n) is the best possible time complexity for this problem.

--------------------------------------------------------
INTERVIEW EXPLANATION:

"We use the two-pointer technique to solve this problem.
One pointer keeps track of the position where the next unique
element should be placed, while the other pointer traverses
the entire array. Whenever a new unique element is found, it is
placed at the next available position. Since the array is sorted,
all duplicates are adjacent, allowing us to solve the problem
efficiently in O(n) time and O(1) extra space."

--------------------------------------------------------
'''


class Solution:
    def duplicate(self,nums):
            i=0
            for k in range(1,len(nums)):
                  if nums[i]!=nums[k]:
                        i+=1
                        nums[i]=nums[k]
                        
            return nums
        
obj=Solution()
print(obj.duplicate([0,1,1,2,2,3,3,4,5]))
print(obj.duplicate([1,1,2,2,2,3,3]))
print(obj.duplicate([1,1,1,1]))
print(obj.duplicate([1,2,3,4,5]))

'''
--------------------------------------------------------
CONCEPTS USED:

1. Two Pointer Technique.
2. Array Traversal.
3. In-place Modification.
4. Time Complexity Analysis.
5. Space Complexity Analysis.
6. Conditional Statements.

--------------------------------------------------------
'''