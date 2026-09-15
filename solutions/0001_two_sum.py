"""
LeetCode Problem 1: Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach:
- Use a hash map to store numbers we've seen so far along with their indices
- For each number, check if (target - current_number) exists in the hash map
- If yes, we found our pair; if no, add current number to hash map and continue
- Time Complexity: O(n) - single pass through the array
- Space Complexity: O(n) - hash map storage
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in array that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that add up to target
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement we need
        complement = target - num
        
        # Check if complement exists in our map
        if complement in num_map:
            # Found the pair: return [index of complement, current index]
            return [num_map[complement], i]
        
        # Store current number with its index
        num_map[num] = i
    
    # According to problem constraints, we should always find a solution
    # This line should never be reached, but included for completeness
    return []

# Alternative brute force approach (for reference)
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - O(n^2) time, O(1) space
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    print(f"Expected: [0, 1]")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    print(f"Expected: [1, 2]")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    print(f"Expected: [0, 1]")
    print()