'''
--------------------------------------------------------
PROBLEM:

189. Rotate Array

Given an integer array nums, rotate the array to the right
by k steps, where k is non-negative.

The rotation should be done in-place.

--------------------------------------------------------
EXAMPLE 1:

Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]

Explanation:

Rotate 1 step:
[7,1,2,3,4,5,6]

Rotate 2 steps:
[6,7,1,2,3,4,5]

Rotate 3 steps:
[5,6,7,1,2,3,4]

--------------------------------------------------------
EXAMPLE 2:

Input:
nums = [-1,-100,3,99]
k = 2

Output:
[3,99,-1,-100]

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 10^5

-2^31 <= nums[i] <= 2^31 - 1

0 <= k <= 10^5

--------------------------------------------------------
'''
'''
--------------------------------------------------------
FIRST APPROACH:

Rotate the array one position to the right, k times.

For every single rotation:

1. Store the last element.
2. Shift every element one position to the right.
3. Put the stored last element at index 0.

Example:

nums = [1,2,3,4,5]
k = 1

Store last:

last = 5

Shift right:

[1,1,2,3,4]

Put last at index 0:

[5,1,2,3,4]

--------------------------------------------------------
CODE:

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        for _ in range(k):

            last = nums[n - 1]

            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = last

        return nums

--------------------------------------------------------
TIME COMPLEXITY:

O(n * k)

Explanation:

- One rotation takes O(n) time.
- We perform the rotation k times.

Therefore:

O(n) * O(k) = O(n * k)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Only one extra variable is used:

last

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL:

For large values of n and k, the same elements are moved repeatedly.

This causes too many operations and can result in:

Time Limit Exceeded.

--------------------------------------------------------
'''
'''
--------------------------------------------------------
OPTIMAL APPROACH USED HERE:

1. Calculate:

      k = k % n

   This handles cases where k is greater than the
   length of the array.

2. Take the last k elements:

      nums[-k:]

3. Take the remaining elements:

      nums[:-k]

4. Concatenate them:

      nums[-k:] + nums[:-k]

5. Assign the result back to the original list using:

      nums[:] = ...

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Explanation:

The array elements are copied into the new arrangement.

Therefore, the total work is proportional to the
number of elements in the array.

--------------------------------------------------------
SPACE COMPLEXITY:

O(n)

Explanation:

Python slicing creates new lists.

Therefore, additional memory is used.

--------------------------------------------------------
IMPORTANT:

This solution is simple and efficient in time complexity,
but it uses O(n) extra space because of slicing.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
LEFT AND RIGHT ROTATION USING SLICING:

RIGHT ROTATION:

In a right rotation, the last k elements move to the front.

Example:

nums = [1,2,3,4,5,6,7]
k = 2

Last k elements:

nums[-k:] = [6,7]

Remaining elements:

nums[:-k] = [1,2,3,4,5]

Result:

[6,7] + [1,2,3,4,5]

Final:

[6,7,1,2,3,4,5]

CODE:

nums[:] = nums[-k:] + nums[:-k]


--------------------------------------------------------
LEFT ROTATION:

In a left rotation, the first k elements move to the end.

Example:

nums = [1,2,3,4,5,6,7]
k = 2

Elements after the first k elements:

nums[k:] = [3,4,5,6,7]

First k elements:

nums[:k] = [1,2]

Result:

[3,4,5,6,7] + [1,2]

Final:

[3,4,5,6,7,1,2]

CODE:

nums[:] = nums[k:] + nums[:k]


--------------------------------------------------------
MEMORY TRICK:

RIGHT ROTATION:

Last k elements go to the front.

nums[-k:] + nums[:-k]


LEFT ROTATION:

First k elements go to the back.

nums[k:] + nums[:k]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES:

1. k = 0

No rotation is required.

Example:

[1,2,3]

Result:

[1,2,3]


2. k = n

The array returns to its original form.

Example:

[1,2,3]

k = 3

Result:

[1,2,3]


3. k > n

Use:

k = k % n

Example:

n = 5
k = 7

7 % 5 = 2

So rotating 7 times is equivalent to rotating 2 times.


4. Array contains one element.

Example:

[5]

Any rotation produces:

[5]


5. Negative numbers.

Example:

[-1,-100,3,99]

The rotation logic works normally.


6. Very large array.

The slicing solution runs in O(n) time.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"We first reduce k using k % n because rotating an array
by its length brings the array back to its original state.

For a right rotation, the last k elements are moved to the
front, while the remaining elements are placed after them.

We use slicing to create these two parts and then assign the
combined result back to nums using nums[:] so that the original
array is modified in-place.

The time complexity is O(n), while the space complexity is O(n)
because Python slicing creates additional lists."

--------------------------------------------------------
'''

class Solution:
    def rotate(self, nums,k) -> None:
        n = len(nums)
        k = k % n

        nums[:] = nums[-k:] + nums[:-k]

        return nums
obj=Solution() 

print(obj.rotate([1,2,3,4,5,6,7],3)) 
print(obj.rotate([3,5,12,6,7,3,5],2)) 
print(obj.rotate([-99,64,22,3,5],4))
print(obj.rotate([8,66,42,1,2,3,6,7,],1))

'''
--------------------------------------------------------
CONCEPTS USED:

1. Array Manipulation.
2. Array Rotation.
3. Python List Slicing.
4. Negative Indexing.
5. Modulo Operator (%).
6. In-place Modification using nums[:].
7. Time Complexity Analysis.
8. Space Complexity Analysis.
9. Left Rotation.
10. Right Rotation.
11. Edge Case Handling.
12. Array Partitioning.
13. Concatenation.

--------------------------------------------------------
'''