'''
--------------------------------------------------------
PROBLEM:

Given an array arr[] of size n, find the second largest DISTINCT
element in the array.

If no such element exists, return None (or -1 as specified by the
coding platform).

--------------------------------------------------------
BRUTE FORCE APPROACH:

1. Sort the array in ascending order.
2. Traverse the sorted array from the end.
3. Find the first element that is not equal to the largest element.
4. Return that element as the second largest.

Time Complexity:
- O(n log n)

Space Complexity:
- Depends on the sorting algorithm used.

Why is it not optimal?
- Sorting the entire array is unnecessary when we only need
  the second largest element.

--------------------------------------------------------
OPTIMAL APPROACH:

1. Initialize the largest element with the first element of the array.
2. Initialize the second largest element as None.
3. Traverse the array exactly once.
4. If the current element is greater than the largest element:
      - Update second largest as the previous largest.
      - Update largest as the current element.
5. Else, if the second largest element is not found yet:
      - Assign the current element if it is distinct from the largest.
6. Else, if the current element is:
      - Smaller than the largest element.
      - Greater than the current second largest element.
      Then update the second largest element.
7. Return the largest and second largest elements.

This is the optimal approach because we traverse the array only once.

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

- Only two extra variables are used:
      1. largest
      2. slargest
- The amount of extra memory does not depend on the size
  of the array.

Hence, the space complexity is O(1).

--------------------------------------------------------
EDGE CASES:

1. Array contains only one element.
2. Array contains all negative numbers.
3. Array contains duplicate values.
4. All elements are the same.
5. Array is already sorted.
6. Array size is large.
7. Second largest element does not exist.

--------------------------------------------------------
OPTIMAL?

YES

Reason:

- Every element must be checked at least once.
- Therefore, O(n) is the best possible time complexity
  for this problem.

--------------------------------------------------------
INTERVIEW EXPLANATION:

"We maintain two variables: one for the largest element and
another for the second largest distinct element. While traversing
the array only once, we update these variables whenever a larger
or better candidate for the second largest element is found.
Since we perform constant-time operations per iteration, the time
complexity is O(n) and the auxiliary space complexity is O(1).
This is the optimal solution because every element must be
inspected at least once."

--------------------------------------------------------
'''


class Solution:
    def secondlargest(self,arr):
        largest=arr[0]
        slargest=None

        # Traverse the array once.
        for i in range(1,len(arr)):

            # New largest element found.
            if arr[i]>largest:
                slargest = largest
                largest=arr[i]

            # Second largest element not found yet.
            elif slargest is None:
                if arr[i] != largest:
                    slargest = arr[i]

            # Better candidate for second largest element.
            elif arr[i] < largest and arr[i] > slargest:
                slargest = arr[i]

        
        return largest,slargest
obj=Solution()
print(obj.secondlargest([30,60,90,10,50]))
print(obj.secondlargest([1,66,90,100,18]))
print(obj.secondlargest([7,9,-6,10,40]))
print(obj.secondlargest([8,3,-4,-5]))
print(obj.secondlargest([8, 3, 7]))

'''
--------------------------------------------------------
CONCEPTS USED:

1. Array Traversal.
2. Conditional Statements (if-elif).
3. Comparison Operators.
4. Time Complexity Analysis.
5. Space Complexity Analysis.
6. Handling Edge Cases.
7. Maintaining Multiple Variables During Traversal.

--------------------------------------------------------
'''