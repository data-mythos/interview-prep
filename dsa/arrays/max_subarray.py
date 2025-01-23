"""
Max Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Step-by-Step Approach to Max Subarray Problem

    1. **Understand the Problem**:
       Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

    2. **Initialize Variables**:
       - `max_sum`: Holds the maximum sum found so far. Initialize it to the first element of the array.
       - `current_sum`: Keeps track of the current subarray sum. Also initialize it to the first element of the array.

    3. **Iterate Through the Array**:
       - Start from the second element (index 1) to the end of the array.
       - For each element, update `current_sum`:
         - Set `current_sum` to the maximum of the current element or the sum of `current_sum` and the current element.

    4. **Update the Maximum Sum**:
       - After updating `current_sum`, check if it is greater than `max_sum`. If it is, update `max_sum`.

    5. **Return the Result**:
       - After iterating through the entire array, `max_sum` will contain the largest sum of any contiguous subarray. Return this value.

Time Complexity: O(n)
Space Complexity: O(1)

"""

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    print(max_subarray([1]))                        # Output: 1
    print(max_subarray([5,4,-1,7,8]))              # Output: 23