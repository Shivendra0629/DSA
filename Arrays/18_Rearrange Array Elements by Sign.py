'''
--------------------------------------------------------
PROBLEM:

2149. Rearrange Array Elements by Sign

You are given an array nums of even length
containing an equal number of positive and
negative integers.

Rearrange the array such that:

1. The array starts with a positive integer.
2. Positive and negative numbers appear
   alternately.
3. The relative order of positive numbers
   remains the same.
4. The relative order of negative numbers
   remains the same.

Return the rearranged array.

--------------------------------------------------------
EXAMPLE 1:

Input:

nums = [3,1,-2,-5,2,-4]

Output:

[3,-2,1,-5,2,-4]

Explanation:

Positive numbers:

[3,1,2]

Negative numbers:

[-2,-5,-4]

Alternate them while preserving order.

--------------------------------------------------------
EXAMPLE 2:

Input:

nums = [-1,1]

Output:

[1,-1]

--------------------------------------------------------
CONSTRAINTS:

2 <= nums.length <= 2 * 10⁵

nums.length is even

Positive count == Negative count

--------------------------------------------------------
'''

'''
--------------------------------------------------------
APPROACH

Concept:

1. Store all positive numbers in one list.
2. Store all negative numbers in another list.
3. Traverse both lists together.
4. Alternately place one positive and one
   negative into the answer array.

--------------------------------------------------------
CODE:

class Solution:

    def rearrangeArray(self, nums):

        positive = []
        negative = []

        for num in nums:

            if num > 0:
                positive.append(num)

            else:
                negative.append(num)

        ans = []

        for i in range(len(positive)):

            ans.append(positive[i])
            ans.append(negative[i])

        return ans

--------------------------------------------------------
TIME COMPLEXITY:

First Traversal:

O(n)

Second Traversal:

O(n)

Overall:

O(n)

--------------------------------------------------------
SPACE COMPLEXITY:

Positive Array  -> O(n/2)

Negative Array  -> O(n/2)

Answer Array    -> O(n)

Overall:

O(n)

--------------------------------------------------------
WHY THIS APPROACH IS GOOD?

- Only one pass to separate numbers.
- One pass to build the answer.
- Preserves the order of positives.
- Preserves the order of negatives.
- Accepted by LeetCode.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
DRY RUN

Input:

nums = [-3,2,1,-5,6,-1]

--------------------------------------------------------

Initially

positive = []

negative = []

--------------------------------------------------------

num = -3

negative = [-3]

--------------------------------------------------------

num = 2

positive = [2]

--------------------------------------------------------

num = 1

positive = [2,1]

--------------------------------------------------------

num = -5

negative = [-3,-5]

--------------------------------------------------------

num = 6

positive = [2,1,6]

--------------------------------------------------------

num = -1

negative = [-3,-5,-1]

--------------------------------------------------------

Now,

positive = [2,1,6]

negative = [-3,-5,-1]

ans = []

--------------------------------------------------------

i = 0

ans.append(2)

ans = [2]

ans.append(-3)

ans = [2,-3]

--------------------------------------------------------

i = 1

ans.append(1)

ans = [2,-3,1]

ans.append(-5)

ans = [2,-3,1,-5]

--------------------------------------------------------

i = 2

ans.append(6)

ans = [2,-3,1,-5,6]

ans.append(-1)

ans = [2,-3,1,-5,6,-1]

--------------------------------------------------------

Final Answer

[2,-3,1,-5,6,-1]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES

1. Smallest Input

Input:

[-1,1]

Output:

[1,-1]

--------------------------------------------------------

2. Already Rearranged

Input:

[1,-1,2,-2]

Output:

[1,-1,2,-2]

--------------------------------------------------------

3. Mixed Order

Input:

[-3,2,1,-5,6,-1]

Output:

[2,-3,1,-5,6,-1]

--------------------------------------------------------

4. All Positives and Negatives Alternate

Input:

[4,-2,5,-7]

Output:

[4,-2,5,-7]

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION

"The idea is to first separate all positive and
negative numbers while preserving their original
order.

Then I create a new array and alternately insert
one positive and one negative number.

Since each element is visited only twice, the
time complexity is O(n). The extra space is O(n)
because separate arrays are used for positives,
negatives, and the final answer."

--------------------------------------------------------
'''

class Solution:

    def rearrangeArray(self, nums):

        positive = []
        negative = []

        for num in nums:

            if num > 0:
                positive.append(num)

            else:
                negative.append(num)

        ans = []

        for i in range(len(positive)):

            ans.append(positive[i])
            ans.append(negative[i])

        return ans


obj = Solution()

print(obj.rearrangeArray([-3,2,1,-5,6,-1]))
print(obj.rearrangeArray([3,1,-2,-5,2,-4]))
print(obj.rearrangeArray([-1,1]))


'''
--------------------------------------------------------
CONCEPTS USED

1. Arrays
2. Array Traversal
3. Two-Pointer Thinking
4. Extra Space (Auxiliary Arrays)
5. Order Preservation
6. Alternate Placement
7. Time Complexity Analysis
8. Space Complexity Analysis

--------------------------------------------------------
'''