'''
--------------------------------------------------------
PROBLEM:

560. Subarray Sum Equals K

Given an integer array nums and an integer k,
return the total number of continuous subarrays
whose sum equals k.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [1,1,1]
k = 2

Output:

2

Explanation:

Subarrays:
[1,1] (Index 0-1)
[1,1] (Index 1-2)

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [1,2,3]
k = 3

Output:

2

Explanation:

Subarrays:
[1,2]
[3]

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 2 * 10^4

-1000 <= nums[i] <= 1000

--------------------------------------------------------
'''

'''
--------------------------------------------------------
FIRST APPROACH (Brute Force)

Concept:

1. Pick every starting index.
2. Keep extending the subarray.
3. Maintain the running sum.
4. If running sum == k, increase count.

--------------------------------------------------------
CODE:

class Solution:

    def Subarray(self, nums, k):

        count = 0

        for i in range(len(nums)):

            sum_arr = 0

            for j in range(i, len(nums)):

                sum_arr += nums[j]

                if sum_arr == k:
                    count += 1

        return count

--------------------------------------------------------
TIME COMPLEXITY:

Outer Loop : O(n)

Inner Loop : O(n)

Overall:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only variables are used.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

- Every possible subarray is checked.
- Too slow for large inputs.
- Gives Time Limit Exceeded (TLE) on LeetCode.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH (Prefix Sum + HashMap)

Concept:

Maintain:

1. prefix_sum → Sum from index 0 to current index.
2. HashMap (Dictionary) → Stores frequency of every prefix sum.

Key Observation:

If

Current Prefix Sum = P

and

Previous Prefix Sum = P - k

then

Current Sum - Previous Sum = k

which means there exists a subarray whose sum is k.

--------------------------------------------------------
CODE:

class Solution:

    def subarraySum(self, nums, k):

        prefix_sum = 0
        count = 0

        prefix = {0:1}

        for num in nums:

            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]

            if prefix_sum in prefix:
                prefix[prefix_sum] += 1
            else:
                prefix[prefix_sum] = 1

        return count

--------------------------------------------------------
DRY RUN

Input:

nums = [1,1,1]
k = 2

Initially

prefix_sum = 0

count = 0

prefix = {0:1}

--------------------------------------------------------

Iteration 1

num = 1

prefix_sum = 1

Need:

1 - 2 = -1

Not present.

Store:

prefix = {0:1,1:1}

count = 0

--------------------------------------------------------

Iteration 2

num = 1

prefix_sum = 2

Need:

2 - 2 = 0

0 exists.

count += prefix[0]

count = 1

Store:

prefix = {0:1,1:1,2:1}

--------------------------------------------------------

Iteration 3

num = 1

prefix_sum = 3

Need:

3 - 2 = 1

1 exists.

count += prefix[1]

count = 2

Store:

prefix = {0:1,1:1,2:1,3:1}

--------------------------------------------------------

Answer:

count = 2

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:

Single traversal of the array.

--------------------------------------------------------
SPACE COMPLEXITY:

O(n)

Reason:

HashMap stores prefix sums.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

- Only one traversal.
- No nested loops.
- Efficient for very large arrays.
- Accepted by LeetCode.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES

1.

nums = [1]
k = 1

Output:

1

--------------------------------------------------------

2.

nums = [0,0,0]

k = 0

Output:

6

--------------------------------------------------------

3.

nums = [-1,-1,1]

k = 0

Output:

1

--------------------------------------------------------

4.

nums = [3]

k = 5

Output:

0

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION

"My first solution checks every possible subarray
using nested loops and keeps a running sum.
Whenever the sum becomes equal to k,
I increment the answer.

Its time complexity is O(n²), which leads to
Time Limit Exceeded for large inputs.

The optimal solution uses Prefix Sum with a HashMap.
While traversing the array once, I store the frequency
of every prefix sum. If (current_prefix_sum - k)
already exists in the HashMap, it means a previous
prefix can be removed to obtain a subarray whose sum
is exactly k.

This reduces the complexity to O(n)."

--------------------------------------------------------
'''

# ---------------- BRUTE FORCE ----------------

class Solution:

    def Subarray(self, nums, k):

        count = 0

        for i in range(len(nums)):

            sum_arr = 0

            for j in range(i, len(nums)):

                sum_arr += nums[j]

                if sum_arr == k:
                    count += 1

        return count


obj = Solution()

print(obj.Subarray([1,1,1],2))
print(obj.Subarray([1,2,3],3))


# ---------------- OPTIMAL ----------------

class Solution:

    def subarraySum(self, nums, k):

        prefix_sum = 0
        count = 0

        prefix = {0:1}

        for num in nums:

            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]

            if prefix_sum in prefix:
                prefix[prefix_sum] += 1
            else:
                prefix[prefix_sum] = 1

        return count


obj = Solution()

print(obj.subarraySum([1,1,1],2))
print(obj.subarraySum([1,2,3],3))

'''
--------------------------------------------------------
CONCEPTS USED

1. Arrays
2. Nested Loops
3. Running Sum
4. Prefix Sum
5. HashMap (Dictionary)
6. Frequency Counting
7. Time Complexity Analysis
8. Space Complexity Analysis
9. Sliding Prefix Technique

--------------------------------------------------------
'''