'''
--------------------------------------------------------
PROBLEM:

Given an array arr[] of size n, find the largest element.

--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Sort the array in ascending order.
2. Return the last element of the sorted array.

Time Complexity:
- O(n log n)

Space Complexity:
- Depends on the sorting algorithm used.

Why is it not optimal?
- Sorting the entire array is unnecessary when we only need
  the largest element.

--------------------------------------------------------
OPTIMAL APPROACH:

1. Initialize the largest element with the first element of the array.
2. Traverse the entire array once.
3. If the current element is greater than the stored largest value,
   update the largest value.
4. Return the largest element.

This is the optimal approach because we only traverse the array once.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Explanation:

- We traverse the array exactly one time.
- The loop runs (n - 1) times since the first element is already
  considered while initialization.
- Each iteration performs constant-time operations
  (comparison and assignment).

Therefore, the total time complexity is O(n).

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Explanation:

- Only one extra variable (largest) is used.
- The amount of extra memory does not depend on the size of the array.

Hence, the space complexity is O(1).

--------------------------------------------------------
EDGE CASES:

1. Array contains only one element.
2. Array contains all negative numbers.
3. Array contains duplicate values.
4. Array is already sorted.
5. Array size is large.

--------------------------------------------------------
OPTIMAL?

YES

Reason:

- Every element must be checked at least once.
- Therefore, O(n) is the best possible time complexity for this problem.

--------------------------------------------------------
INTERVIEW EXPLANATION:

"We traverse the array only once while maintaining the largest
element seen so far. Since every iteration performs constant-time
operations, the time complexity is O(n). We use only one extra
variable, giving us O(1) auxiliary space. This is the optimal
solution because every element must be inspected at least once."

--------------------------------------------------------

'''

class Solution:
    def largest (self,arr)->int:
        largest=arr[0]     # O(1)
        # Traverse the array once
        for i in range(1,len(arr)):       # O(n)
            if arr[i] > largest:   # O(1)
                largest=arr[i]     # O(1)
        
        return largest
obj= Solution()
print(obj.largest([60,30,50,70,140]))
print(obj.largest([-5, -3,-10, ]))
print(obj.largest([70,102,30,-11,-50,]))
print(obj.largest([55,49,36,28,87,66,108]))


'''      
--------------------------------------------------------
CONCEPTS USED:

1. Array Traversal
2. Comparison Operators
3. Time Complexity Analysis
4. Space Complexity Analysis

--------------------------------------------------------

'''
     
