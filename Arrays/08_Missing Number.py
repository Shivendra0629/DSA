'''
--------------------------------------------------------
PROBLEM:

268. Missing Number

Given an array nums containing n distinct numbers
in the range [0, n], return the only number in the
range that is missing from the array.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [3,0,1]

Output:

2

Explanation:

n = 3

Numbers in the range:

[0,1,2,3]

The missing number is 2.

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [0,1]

Output:

2

--------------------------------------------------------
EXAMPLE 3:

Input:

nums = [9,6,4,2,3,5,7,0,1]

Output:

8

--------------------------------------------------------
CONSTRAINTS:

n == nums.length

1 <= n <= 10^4

0 <= nums[i] <= n

All numbers are unique.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Create another array containing all numbers
   from 0 to n.

2. Traverse the new array.

3. If any element is not present in nums,
   return that element.

--------------------------------------------------------
CODE:

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        b = []

        for i in range(n + 1):
            b.append(i)

        for j in range(n + 1):
            if b[j] not in nums:
                return b[j]

--------------------------------------------------------
TIME COMPLEXITY:

O(n²)

Explanation:

- Creating array b takes O(n).

- Traversing array b takes O(n).

- 'not in nums' performs Linear Search,
  which takes O(n).

Therefore:

O(n) × O(n)

= O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n)

Explanation:

An extra array b is created to store
numbers from 0 to n.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

- Uses an extra array.

- Every 'not in' operation performs a
  Linear Search.

- This increases the overall time complexity
  to O(n²).

--------------------------------------------------------
'''

'''
--------------------------------------------------------
BETTER APPROACH:

1. Sort the array.

2. Traverse the array.

3. Compare every index with its value.

4. If nums[i] != i, then i is the
   missing number.

5. If every index matches, return len(nums).

--------------------------------------------------------
CODE:
'''
class Solution:
    def missingNumber(self, nums):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
obj=Solution()
print(obj.missingNumber([1,0,2,0,2,3]))
'''
--------------------------------------------------------
TIME COMPLEXITY:

O(n log n)

Explanation:

- Sorting takes O(n log n).

- Traversing the array takes O(n).

Overall:

O(n log n)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

No extra array is created.

(Considering only explicit extra space.)

--------------------------------------------------------
WHY THIS APPROACH IS BETTER:

- No extra array is required.

- Simpler than the brute force approach.

- Faster than O(n²).

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. Missing number is 0.

Example:

[1]

Output:

0


2. Missing number is n.

Example:

[0,1]

Output:

2


3. Missing number is in the middle.

Example:

[3,0,1]

Output:

2


4. Array contains only one element.

Example:

[0]

Output:

1


5. Large input size.

Sorting still works correctly.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"The brute force approach creates another array
containing all numbers from 0 to n and checks
which number is missing using Linear Search.

A better approach is to sort the array and compare
every element with its index. The first mismatch
indicates the missing number. If all indices match,
then the missing number is n."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays.
2. Linear Search.
3. Sorting.
4. Brute Force.
5. Time Complexity Analysis.
6. Space Complexity Analysis.
7. Edge Case Handling.

--------------------------------------------------------
'''