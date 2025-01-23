"""
Problem: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
    Input: nums = [1,2,3,1]
    Output: true
    
Approach:
    1. Use a hash set to track seen numbers
    2. Iterate through array once
    3. For each number, check if it's in set
    4. If yes -> found duplicate
    5. If no -> add to set and continue
    
Time:  O(n) - single pass through array
Space: O(n) - hash set to store numbers
"""


def contains_duplicate(nums):
    seen = set()
    print(f"\nChecking array: {nums}")

    for num in nums:
        print(f"Checking number: {num}")
        print(f"Current set: {seen}")

        if num in seen:
            print(f"Found duplicate: {num}")
            return True

        seen.add(num)
        print(f"Added {num} to set")

    print("No duplicates found")
    return False


def test_contains_duplicate():
    # Test case 1: Array with duplicates
    assert contains_duplicate([1, 2, 3, 1]) == True, "Test 1 failed"
    print("Test 1 passed!")

    # Test case 2: Array without duplicates
    assert contains_duplicate([1, 2, 3, 4]) == False, "Test 2 failed"
    print("Test 2 passed!")

    # Test case 3: Empty array
    assert contains_duplicate([]) == False, "Test 3 failed"
    print("Test 3 passed!")

    # Test case 4: Array with multiple duplicates
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3]) == True, "Test 4 failed"
    print("Test 4 passed!")


if __name__ == "__main__":
    test_contains_duplicate()
