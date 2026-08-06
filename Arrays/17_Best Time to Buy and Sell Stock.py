'''
--------------------------------------------------------
PROBLEM:

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i]
represents the stock price on the ith day.

You may buy one stock and later sell it exactly once.

Return the maximum profit you can achieve.

If no profit is possible, return 0.

--------------------------------------------------------
EXAMPLE 1:

Input:

prices = [7,1,5,3,6,4]

Output:

5

Explanation:

Buy at price 1
Sell at price 6

Profit = 6 - 1 = 5

--------------------------------------------------------
EXAMPLE 2:

Input:

prices = [7,6,4,3,1]

Output:

0

Explanation:

Prices keep decreasing,
so no profitable transaction is possible.

--------------------------------------------------------
CONSTRAINTS:

1 <= prices.length <= 100000

0 <= prices[i] <= 10000

--------------------------------------------------------
'''

'''
--------------------------------------------------------
FIRST APPROACH (Brute Force)

Concept:

1. Select every day as the buying day.
2. Compare it with every future day.
3. Calculate the profit.
4. Store the maximum profit.

--------------------------------------------------------
CODE:

class Solution:

    def maxProfit(self, prices):

        max_profit = 0

        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):

                profit = prices[j] - prices[i]

                max_profit = max(max_profit, profit)

        return max_profit

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

Only a few variables are used.

--------------------------------------------------------
WHY THIS APPROACH IS NOT OPTIMAL?

- Compares every pair of days.
- Performs many unnecessary comparisons.
- Gives Time Limit Exceeded (TLE) for large inputs.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
OPTIMAL APPROACH

Concept:

Keep track of:

1. Minimum stock price seen so far.
2. Maximum profit obtained so far.

For every day:

Profit = Current Price - Minimum Price Seen

Update the maximum profit.

--------------------------------------------------------
CODE:

class Solution:

    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            min_price = min(min_price, prices[i])

            profit = prices[i] - min_price

            max_profit = max(max_profit, profit)

        return max_profit

--------------------------------------------------------
TIME COMPLEXITY:

O(n)

Reason:

Only one traversal of the array.

--------------------------------------------------------
SPACE COMPLEXITY:

O(1)

Reason:

Only two variables are maintained.

--------------------------------------------------------
WHY THIS APPROACH IS OPTIMAL?

- Single traversal.
- No nested loops.
- Constant extra space.
- Accepted by LeetCode.
- Efficient even for very large inputs.

--------------------------------------------------------
'''

'''
--------------------------------------------------------
DRY RUN

Input:

prices = [7,1,5,3,6,4]

--------------------------------------------------------

Initial:

min_price = 7

max_profit = 0

--------------------------------------------------------

Day 1

Price = 1

min_price = min(7,1) = 1

profit = 1 - 1 = 0

max_profit = 0

--------------------------------------------------------

Day 2

Price = 5

min_price = 1

profit = 5 - 1 = 4

max_profit = 4

--------------------------------------------------------

Day 3

Price = 3

min_price = 1

profit = 3 - 1 = 2

max_profit = 4

--------------------------------------------------------

Day 4

Price = 6

min_price = 1

profit = 6 - 1 = 5

max_profit = 5

--------------------------------------------------------

Day 5

Price = 4

min_price = 1

profit = 4 - 1 = 3

max_profit = 5

--------------------------------------------------------

Final Answer:

5

--------------------------------------------------------
'''

'''
--------------------------------------------------------
EDGE CASES

1. Increasing Prices

Input:

[1,2,3,4,5]

Output:

4

--------------------------------------------------------

2. Decreasing Prices

Input:

[7,6,5,4,3]

Output:

0

--------------------------------------------------------

3. Single Element

Input:

[5]

Output:

0

--------------------------------------------------------

4. Same Prices

Input:

[5,5,5,5]

Output:

0

--------------------------------------------------------
'''

'''
--------------------------------------------------------
INTERVIEW EXPLANATION

"My first solution uses a brute-force approach.
For every buying day, I compare it with every
possible selling day and calculate the profit.

Although correct, it requires O(n²) time and
causes Time Limit Exceeded for large inputs.

The optimal approach maintains the minimum stock
price seen so far and computes the profit for
selling on the current day. By updating the
maximum profit during a single traversal, the
solution achieves O(n) time complexity and
O(1) extra space."

--------------------------------------------------------
'''

class Solution:

    def maxProfit(self, prices):

        max_profit = 0

        for i in range(len(prices)):

            for j in range(i + 1, len(prices)):

                profit = prices[j] - prices[i]

                max_profit = max(max_profit, profit)

        return max_profit


obj = Solution()

print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([7,6,4,3,1]))


class Solution:

    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):

            min_price = min(min_price, prices[i])

            profit = prices[i] - min_price

            max_profit = max(max_profit, profit)

        return max_profit


obj = Solution()

print(obj.maxProfit([7,1,5,3,6,4]))
print(obj.maxProfit([7,6,4,3,1]))
print(obj.maxProfit([1,2,3,4,5]))
print(obj.maxProfit([5]))
print(obj.maxProfit([5,5,5,5]))

'''
--------------------------------------------------------
CONCEPTS USED

1. Arrays
2. Brute Force
3. Nested Loops
4. Greedy Technique
5. Minimum Value Tracking
6. One-Pass Traversal
7. Time Complexity Analysis
8. Space Complexity Analysis
9. Maximum Profit Calculation

--------------------------------------------------------
'''