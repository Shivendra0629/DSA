'''
--------------------------------------------------------
PROBLEM:

136. Single Number

Given a non-empty integer array nums, every element
appears exactly twice except for one element.

Return the element that appears only once.

You must solve it with linear time complexity and
constant extra space.

--------------------------------------------------------
EXAMPLE 1:

Input:
nums = [2,2,1]

Output:
1

--------------------------------------------------------
EXAMPLE 2:

Input:
nums = [4,1,2,1,2]

Output:
4

--------------------------------------------------------
EXAMPLE 3:

Input:
nums = [1]

Output:
1

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 3 * 10^4

-3 * 10^4 <= nums[i] <= 3 * 10^4

Every element appears exactly twice except one.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
FIRST APPROACH (Sorting)

1. Sort the array.
2. Compare elements in pairs.
3. If a pair is different, return that element.
4. If all pairs match, return the last element.

--------------------------------------------------------
CODE:

class Solution:
    def SingleNum(self, arr):

        arr.sort()

        for i in range(0, len(arr)-1, 2):
            if arr[i] != arr[i+1]:
                return arr[i]

        return arr[-1]

--------------------------------------------------------
TIME COMPLEXITY:

Sorting : O(n log n)

Traversing : O(n)

Overall:

O(n log n)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

Sorting itself takes O(n log n), whereas the problem
expects O(n) time complexity.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH (XOR)

Concept:

1. x ^ x = 0
2. x ^ 0 = x

Every duplicate element cancels itself using XOR.

Only the element appearing once remains.

--------------------------------------------------------
CODE:

class Solution:
    def SingleNum(self, arr):

        ans = 0

        for num in arr:
            ans ^= num

        return ans

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:

The array is traversed only once.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only one extra variable (ans) is used.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

- No sorting required.
- One traversal only.
- Constant extra space.
- Satisfies the problem constraints.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. Single element.

Input:

[5]

Output:

5

--------------------------------------------------------

2. Unique element at the beginning.

Input:

[4,1,1,2,2]

Output:

4

--------------------------------------------------------

3. Unique element at the end.

Input:

[1,1,2,2,3]

Output:

3

--------------------------------------------------------

4. Negative numbers.

Input:

[-1,-1,-5]

Output:

-5

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"The sorting approach works correctly but requires
O(n log n) time due to sorting.

The optimal approach uses XOR. Since XOR of two equal
numbers is 0 and XOR of any number with 0 is the
number itself, all duplicate elements cancel each
other, leaving only the unique element.

Thus, the solution runs in O(n) time and O(1) space."

--------------------------------------------------------
'''

class Solution:
    def SingleNum(self, arr):

        ans = 0

        for num in arr:
            ans ^= num

        return ans


obj = Solution()

print(obj.SingleNum([1,2,1,2,3]))
print(obj.SingleNum([4,1,2,1,2]))
print(obj.SingleNum([2,2,1,3]))
print(obj.SingleNum([5]))
print(obj.SingleNum([-1,-1,-5]))

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Sorting
3. XOR (Bit Manipulation)
4. Time Complexity Analysis
5. Space Complexity Analysis
6. Bitwise Operators
7. Array Traversal

--------------------------------------------------------
'''