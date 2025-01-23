"""
Two Sum

Problem:
Given an array of integers nums and a target integer, return indices of two numbers in nums that add up to target.
- Each input has exactly one solution
- Same element cannot be used twice
- Return the answer in any order

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Approach:
1. Use hash map to store visited numbers and their indices
2. For each number, check if (target - current_number) exists in hash map
3. If found, return current index and stored index
4. If not found, store current number and index

Time: O(n) - single pass through array
Space: O(n) - storing up to n elements in hash map
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val -> index

        for i, num in enumerate(nums):
            complement = target - num
            print(f"Current number: {num}, Looking for complement: {complement}")

            if complement in seen:
                print(f"Found pair: {num} + {complement} = {target}")
                return [seen[complement], i]

            # Store current number and its index
            seen[num] = i
            print(f"Updated hash map: {seen}")

        return []  # no solution found


# Unit Tests
def test_two_sum():
    solution = Solution()

    # Test case 1: Basic case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # Test case 2: Numbers in different order
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]

    # Test case 3: Same numbers
    assert solution.twoSum([3, 3], 6) == [0, 1]

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"\nInput array: {nums}")
    print(f"Target: {target}")
    print(f"Result indices: {result}")

    # Run tests
    test_two_sum()
