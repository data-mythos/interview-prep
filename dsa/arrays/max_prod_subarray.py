"""
Max Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Step-by-Step Approach to Max Product Subarray Problem

    1. **Understand the Problem**:
       Given an integer array `nums`, find the contiguous subarray that has the largest product and return that product.

    2. **Initialize Variables**:
       - `max_product`: Holds the maximum product found so far. Initialize it to the first element of the array.
       - `min_product`: Holds the minimum product found so far (to handle negative numbers). Initialize it to the first element of the array.
       - `result`: Holds the final maximum product. Initialize it to the first element of the array.

    3. **Iterate Through the Array**:
       - Start from the second element (index 1) to the end of the array.
       - For each element, if it is negative, swap `max_product` and `min_product`.
       - Update `max_product` to be the maximum of the current element or the product of `max_product` and the current element.
       - Update `min_product` to be the minimum of the current element or the product of `min_product` and the current element.
       - Update `result` to be the maximum of `result` and `max_product`.

    4. **Return the Result**:
       - After iterating through the entire array, `result` will contain the largest product of any contiguous subarray. Return this value.
"""


def max_product_subarray(nums):
    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result


# Example usage
if __name__ == "__main__":
    print(max_product_subarray([2, 3, -2, 4]))  # Output: 6
    print(max_product_subarray([-2, 0, -1]))  # Output: 0
