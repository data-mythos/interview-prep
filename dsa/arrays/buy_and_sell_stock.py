"""
Best Time to Buy and Sell Stock

Problem: Best Time to Buy and Sell Stock
Given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit by buying on one day and selling on a different day in the future.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

Approach:
1. Keep track of minimum price seen so far (buying price)
2. For each price, calculate potential profit if we sell at current price
3. Update maximum profit if current profit is larger
4. Return maximum profit found

Time: O(n) - single pass through array
Space: O(1) - only using two variables
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize minimum price to infinity
        max_profit = 0  # Initialize maximum profit to 0
        
        for price in prices:
            # Print current state for visualization
            print(f"Current price: {price}, Min price so far: {min_price}, Max profit so far: {max_profit}")
            
            # Update minimum price if current price is lower
            if price < min_price:
                min_price = price
                print(f"Found new minimum price: {min_price}")
            
            # Calculate potential profit if we sell at current price
            current_profit = price - min_price
            
            # Update maximum profit if current profit is larger
            if current_profit > max_profit:
                max_profit = current_profit
                print(f"Found new maximum profit: {max_profit}")
        
        return max_profit


# Unit Tests
def test_max_profit():
    solution = Solution()
    
    # Test case 1: Normal case with profit
    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    
    # Test case 2: Decreasing prices (no profit possible)
    assert solution.maxProfit([7,6,4,3,1]) == 0
    
    # Test case 3: Single price
    assert solution.maxProfit([1]) == 0
    
    # Test case 4: Empty array
    assert solution.maxProfit([]) == 0
    
    # Test case 5: Increasing prices
    assert solution.maxProfit([1,2,3,4,5]) == 4
    
    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    prices = [7,1,5,3,6,4]
    profit = solution.maxProfit(prices)
    print(f"\nInput prices: {prices}")
    print(f"Maximum profit: {profit}")
    
    # Run tests
    test_max_profit()
