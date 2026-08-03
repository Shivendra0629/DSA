'''
--------------------------------------------------------
PROBLEM:

169. Majority Element

Given an integer array nums of size n, return the
majority element.

The majority element is the element that appears
more than ⌊n/2⌋ times.

It is guaranteed that the majority element always
exists.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [3,2,3]

Output:

3

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [2,2,1,1,1,2,2]

Output:

2

--------------------------------------------------------
CONSTRAINTS:

1 <= nums.length <= 5 * 10^4

-10^9 <= nums[i] <= 10^9

The majority element always exists.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
APPROACH 1 (Brute Force)

Idea:

For every element in the array,

1. Count how many times it appears.
2. If its frequency becomes greater than n//2,
   return that element.

--------------------------------------------------------
CODE:

class Solution:
    def majorityElement(self, nums):

        n = len(nums)

        for i in range(n):

            count = 0

            for j in range(n):

                if nums[i] == nums[j]:
                    count += 1

            if count > n // 2:
                return nums[i]

--------------------------------------------------------
DRY RUN:

Input:

nums = [2,2,1,1,1,2,2]

n = 7

Majority Frequency > 3

--------------------------------------------------------

Check element 2

Count = 4

4 > 3

Return 2

--------------------------------------------------------
TIME COMPLEXITY:

Outer Loop : O(n)

Inner Loop : O(n)

Overall:

O(n²)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

--------------------------------------------------------
DRAWBACK:

Nested loops make this solution slow for
large inputs.

LeetCode gives Time Limit Exceeded (TLE).

--------------------------------------------------------
'''

class Solution:
    def majorityElement(self, nums):

        n = len(nums)

        for i in range(n):

            count = 0

            for j in range(n):

                if nums[i] == nums[j]:
                    count += 1

            if count > n // 2:
                return nums[i]


obj = Solution()

print(obj.majorityElement([2,2,1,1,1,2,2]))

'''
--------------------------------------------------------
APPROACH 2 (HashMap / Dictionary)

Idea:

Store the frequency of every element inside a
dictionary.

Key   -> Element

Value -> Frequency

After storing frequencies,

Traverse the dictionary and return the element
whose frequency is greater than n//2.

--------------------------------------------------------
CODE:

class Solution:
    def majorityElement(self, nums):

        freq = {}

        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key in freq:

            if freq[key] > len(nums)//2:
                return key

--------------------------------------------------------
DRY RUN:

Input:

nums = [2,2,1,1,1,2,2]

Initially:

freq = {}

--------------------------------------------------------

Read 2

freq = {2:1}

Read 2

freq = {2:2}

Read 1

freq = {2:2,1:1}

Read 1

freq = {2:2,1:2}

Read 1

freq = {2:2,1:3}

Read 2

freq = {2:3,1:3}

Read 2

freq = {2:4,1:3}

--------------------------------------------------------

Traverse Dictionary

key = 2

freq[2] = 4

4 > 3

Return 2

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

--------------------------------------------------------
SPACE COMPLEXITY:

O(n)

Reason:

Dictionary stores frequencies.

--------------------------------------------------------
'''

class Solution:
    def majorityElement(self, nums):

        freq = {}

        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key in freq:

            if freq[key] > len(nums)//2:
                return key


obj = Solution()

print(obj.majorityElement([2,2,1,1,1,2,2]))

'''
--------------------------------------------------------
APPROACH 3 (Moore's Voting Algorithm)

Idea:

Maintain only two variables.

candidate

count

Whenever count becomes zero,

choose the current element as the new candidate.

If the current element equals the candidate,

increase count.

Otherwise,

decrease count.

Different elements cancel each other's votes.

Since the majority element appears more than
n/2 times,

it can never be completely cancelled.

--------------------------------------------------------
CODE:

class Solution:
    def majorityElement(self, nums):

        candidate = None

        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

--------------------------------------------------------
DRY RUN:

Input:

nums = [2,2,1,1,1,2,2]

Initially

candidate = None

count = 0

--------------------------------------------------------

Read 2

candidate = 2

count = 1

--------------------------------------------------------

Read 2

count = 2

--------------------------------------------------------

Read 1

count = 1

--------------------------------------------------------

Read 1

count = 0

--------------------------------------------------------

Read 1

candidate = 1

count = 1

--------------------------------------------------------

Read 2

count = 0

--------------------------------------------------------

Read 2

candidate = 2

count = 1

--------------------------------------------------------

Loop Ends

Return candidate

Answer = 2

--------------------------------------------------------
WHY DOES THIS WORK?

Think of different elements cancelling each
other's votes.

Example:

2 1 -> Cancel

2 1 -> Cancel

2 1 -> Cancel

Since the majority element appears more than
half the time,

it always survives the cancellation process.

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only two variables are used.

--------------------------------------------------------
'''

class Solution:
    def majorityElement(self, nums):

        candidate = None

        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


obj = Solution()

print(obj.majorityElement([2,2,1,1,1,2,2]))

'''
--------------------------------------------------------
EDGE CASES:

1. Single Element

Input:

[5]

Output:

5

--------------------------------------------------------

2. All Elements Same

Input:

[2,2,2,2]

Output:

2

--------------------------------------------------------

3. Majority Element at Beginning

Input:

[1,1,1,2,3]

Output:

1

--------------------------------------------------------

4. Majority Element at End

Input:

[3,2,1,2,2,2,2]

Output:

2

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION:

"I first solved the problem using the brute-force
approach by counting the frequency of every
element using nested loops. This works correctly
but takes O(n²) time.

Next, I improved it using a HashMap (Dictionary),
where I stored the frequency of every element.
This reduced the time complexity to O(n) but
required O(n) extra space.

Finally, I used Moore's Voting Algorithm, which
maintains only a candidate and a count. Different
elements cancel each other's votes, and because
the majority element appears more than n/2 times,
it always survives the cancellation process.

This gives O(n) time complexity with O(1) extra
space, making it the optimal solution."

--------------------------------------------------------
'''

'''
--------------------------------------------------------
CONCEPTS USED:

1. Arrays
2. Nested Loops
3. Frequency Counting
4. HashMap / Dictionary
5. Moore's Voting Algorithm
6. Time Complexity Analysis
7. Space Complexity Analysis
8. Majority Element
9. Dry Run Analysis

--------------------------------------------------------
'''