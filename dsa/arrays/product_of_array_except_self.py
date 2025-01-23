"""
Product of Array Except Self

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Approach:
1. Use two passes through the array to avoid division:
   - First pass (Left to Right): Calculate prefix products
   - Second pass (Right to Left): Calculate suffix products while combining with prefix

Detailed Example with nums = [1,2,3,4]:

1. Initial Setup:
   nums = [1, 2, 3, 4]
   result = [1, 1, 1, 1]  # Initialize with all 1s

2. First Pass (Left to Right):
   Calculate products of all numbers to the LEFT of each position
   Position 0: nothing to the left
   result = [1, _, _, _]
   
   Position 1: multiply by nums[0]=1
   result = [1, 1, _, _]
   
   Position 2: multiply by nums[0]*nums[1]=1*2
   result = [1, 1, 2, _]
   
   Position 3: multiply by nums[0]*nums[1]*nums[2]=1*2*3
   result = [1, 1, 2, 6]

3. Second Pass (Right to Left):
   Multiply each position by product of all numbers to the RIGHT
   Position 3: nothing to the right
   result = [1, 1, 2, 6]
   
   Position 2: multiply by nums[3]=4
   result = [1, 1, 8, 6]
   
   Position 1: multiply by nums[3]*nums[2]=4*3
   result = [1, 12, 8, 6]
   
   Position 0: multiply by nums[3]*nums[2]*nums[1]=4*3*2
   result = [24, 12, 8, 6]

Visual Example:
Array:     [1,    2,    3,    4]
Left:      [1,    1,    2,    6]   (products of numbers to the left)
Right:     [24,   12,   4,    1]   (products of numbers to the right)
Result:    [24,   12,   8,    6]   (left * right at each position)

Why This Works:
- For each position, we need the product of all numbers except itself
- Instead of using division (which could be problematic with zeros), we:
  1. First get product of all numbers to the left
  2. Then multiply by product of all numbers to the right
- This way, each position naturally skips its own number in the calculation

Time Complexity: O(n) - two passes through the array
Space Complexity: O(1) - excluding output array
"""
import logging
from typing import List

logger = logging.getLogger(__name__)


class ProductExceptSelf:
    def solve(self, nums: List[int]) -> List[int]:
        """
        Calculate product of all elements except self without using division.
        
        Args:
            nums: List of integers
            
        Returns:
            List where each element is product of all numbers except self
            
        Example:
            >>> ProductExceptSelf().solve([1,2,3,4])
            [24,12,8,6]
        """
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            logger.debug(f"Prefix pass - index {i}: prefix={prefix}, result={result}")
        
        # Calculate suffix products and combine
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            logger.debug(f"Suffix pass - index {i}: suffix={suffix}, result={result}")
        
        return result

    def test(self):
        """Test ProductExceptSelf solution"""
        # Test 1: Basic positive numbers
        assert self.solve([1, 2, 3, 4]) == [24, 12, 8, 6]
        logger.info("Test 1 PASSED")

        # Test 2: Array with zero
        assert self.solve([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
        logger.info("Test 2 PASSED")

        # Test 3: Two elements
        assert self.solve([1, 2]) == [2, 1]
        logger.info("Test 3 PASSED")

        # Test 4: All ones
        assert self.solve([1, 1, 1]) == [1, 1, 1]
        logger.info("Test 4 PASSED")

        # Test 5: Empty array
        assert self.solve([]) == []
        logger.info("Test 5 PASSED")

        # Test 6: Single element
        assert self.solve([5]) == [1]
        logger.info("Test 6 PASSED")

        # Test 7: Negative numbers
        assert self.solve([-1, -2, -3]) == [6, 3, 2]
        logger.info("Test 7 PASSED")

        logger.info("All tests PASSED!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ProductExceptSelf().test()