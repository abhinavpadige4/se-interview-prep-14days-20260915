"""
LeetCode Problem 42: Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

Approach:
- Two pointer approach: maintain left and right pointers
- Track max height from left and right as we move pointers
- Water trapped at each position = min(left_max, right_max) - current_height
- Move the pointer with smaller max height towards center
- Time Complexity: O(n) - single pass with two pointers
- Space Complexity: O(1) - constant extra space
"""

from typing import List

def trap(height: List[int]) -> int:
    """
    Calculate how much water can be trapped after raining.
    
    Args:
        height: List of non-negative integers representing elevation map
        
    Returns:
        Total units of trapped rain water
    """
    # Edge case: less than 3 bars cannot trap water
    if len(height) < 3:
        return 0
    
    # Initialize two pointers
    left, right = 0, len(height) - 1
    
    # Track maximum height from left and right
    left_max, right_max = height[left], height[right]
    
    # Total water trapped
    water_trapped = 0
    
    # Two pointer approach
    while left < right:
        if height[left] < height[right]:
            # Process left side
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            # Process right side
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1
    
    return water_trapped

# Alternative approach using prefix/suffix arrays (for reference)
def trap_prefix_suffix(height: List[int]) -> int:
    """
    Prefix/suffix array approach - O(n) time, O(n) space
    """
    if len(height) < 3:
        return 0
    
    n = len(height)
    
    # Prefix max array
    prefix_max = [0] * n
    prefix_max[0] = height[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], height[i])
    
    # Suffix max array
    suffix_max = [0] * n
    suffix_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], height[i])
    
    # Calculate trapped water
    water_trapped = 0
    for i in range(n):
        water_trapped += min(prefix_max[i], suffix_max[i]) - height[i]
    
    return water_trapped

# Test cases
if __name__ == "__main__":
    # Test case 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Input: height = {height1}")
    print(f"Output: {trap(height1)}")
    print(f"Expected: 6")
    print()
    
    # Test case 2
    height2 = [4,2,0,3,2,5]
    print(f"Input: height = {height2}")
    print(f"Output: {trap(height2)}")
    print(f"Expected: 9")
    print()
    
    # Edge cases
    height3 = [0,0,0]
    print(f"Input: height = {height3}")
    print(f"Output: {trap(height3)}")
    print(f"Expected: 0")
    print()
    
    height4 = [5,4,3,2,1]
    print(f"Input: height = {height4}")
    print(f"Output: {trap(height4)}")
    print(f"Expected: 0")
    print()