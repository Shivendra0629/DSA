'''
--------------------------------------------------------
PROBLEM:

Union of Two Sorted Arrays

Given two sorted integer arrays nums1 and nums2,
return the union of both arrays.

The union should:

- Contain only unique elements.
- Include all elements present in either array.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums1 = [1,2,3,4]
nums2 = [2,3,4,5]

Output:

[1,2,3,4,5]

--------------------------------------------------------
EXAMPLE 2:

Input:

nums1 = [1,1,2]
nums2 = [2,3,3]

Output:

[1,2,3]

--------------------------------------------------------
CONSTRAINTS:

1 <= nums1.length, nums2.length <= 10^5

Arrays are sorted in non-decreasing order.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
APPROACH 1: USING SET

Idea:

1. Merge both arrays.
2. Convert the merged array into a set.
3. Return the set.

--------------------------------------------------------
CODE:

class Solution:
    def Union(self, nums1, nums2):
        arr = set(nums1 + nums2)
        return arr

obj = Solution()
print(obj.Union([1,2,3,4], [2,3,4,5]))

--------------------------------------------------------
TIME COMPLEXITY:

O(n + m)

Explanation:

- Merging both arrays takes O(n + m).
- Creating a set also takes O(n + m).

Overall:

O(n + m)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n + m)

Explanation:

The set stores all unique elements.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

- Uses extra memory.
- Set does not guarantee sorted order.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
APPROACH 2: USING LIST

Idea:

1. Create an empty list.
2. Traverse nums1 and add unique elements.
3. Traverse nums2 and add elements that are
   not already present.
4. Return the final list.

--------------------------------------------------------
CODE:
'''

class Solution:
    def Union(self, nums1, nums2):
        nums3 = []

        for i in range(len(nums1)):
            if nums1[i] not in nums3:
                nums3.append(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] not in nums3:
                nums3.append(nums2[j])

        return nums3

obj = Solution()
print(obj.Union([1,2,3,4], [2,3,4,5]))

'''
--------------------------------------------------------
TIME COMPLEXITY:

O((n + m)²)

Explanation:

- The outer loops together run O(n + m) times.
- Every 'not in' operation performs
  Linear Search.

Therefore:

O((n + m)²)

If both arrays are of similar size:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n + m)

Explanation:

The result list stores all unique elements.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

- 'not in' performs Linear Search.
- Membership checking becomes slow
  for large arrays.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH:

Use the Two Pointer Technique.

Since both arrays are already sorted:

1. Initialize two pointers.

2. Compare elements from both arrays.

3. Add the smaller element to the answer.

4. If both elements are equal,
   add only one of them.

5. Move the corresponding pointer(s).

--------------------------------------------------------
TIME COMPLEXITY:

O(n + m)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n + m)

(For storing the union.)

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. One array is empty.

Example:

nums1 = []
nums2 = [1,2,3]

Output:

[1,2,3]


2. Both arrays are empty.

Output:

[]


3. Both arrays contain the same elements.

Example:

nums1 = [1,2,3]
nums2 = [1,2,3]

Output:

[1,2,3]


4. Arrays contain duplicates.

Example:

nums1 = [1,1,2]
nums2 = [2,2,3]

Output:

[1,2,3]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"The simplest solution is to merge both arrays
and remove duplicates using a set. Another approach
is to store only unique elements in a new list,
but checking membership in a list requires Linear
Search, making it slower.

Since both arrays are sorted, the optimal solution
uses the Two Pointer Technique, which traverses
both arrays only once and achieves O(n + m) time."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays.
2. Union of Arrays.
3. Set.
4. List.
5. Linear Search.
6. Two Pointer Technique.
7. Time Complexity Analysis.
8. Space Complexity Analysis.
9. Duplicate Removal.

--------------------------------------------------------
'''