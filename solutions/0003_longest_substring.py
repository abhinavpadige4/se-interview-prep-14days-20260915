"""
LeetCode Problem 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Approach:
- Use sliding window technique with two pointers (left and right)
- Use a set to track characters in the current window
- Expand right pointer, add characters to set
- When duplicate found, shrink left pointer until duplicate is removed
- Track maximum window size during the process
- Time Complexity: O(n) - each character visited at most twice
- Space Complexity: O(min(m, n)) - size of character set
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    # Edge case: empty string
    if not s:
        return 0
    
    # Set to store characters in current window
    char_set = set()
    
    # Left pointer of the sliding window
    left = 0
    
    # Maximum length found
    max_length = 0
    
    # Iterate through string with right pointer
    for right in range(len(s)):
        # If character is already in set, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Alternative approach using dictionary to store character indices
def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized version using dictionary to jump left pointer directly.
    """
    if not s:
        return 0
    
    # Dictionary to store character -> last index mapping
    char_index_map = {}
    
    # Left pointer of the sliding window
    left = 0
    
    # Maximum length found
    max_length = 0
    
    # Iterate through string with right pointer
    for right in range(len(s)):
        # If character exists in current window, move left pointer
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        
        # Update character's last seen index
        char_index_map[s[right]] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {length_of_longest_substring(s1)}")
    print(f"Expected: 3")
    print()
    
    # Test case 2
    s2 = "bbbbb"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {length_of_longest_substring(s2)}")
    print(f"Expected: 1")
    print()
    
    # Test case 3
    s3 = "pwwkew"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {length_of_longest_substring(s3)}")
    print(f"Expected: 3")
    print()
    
    # Additional test cases
    s4 = ""
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {length_of_longest_substring(s4)}")
    print(f"Expected: 0")
    print()
    
    s5 = "abcdefg"
    print(f"Input: s = \"{s5}\"")
    print(f"Output: {length_of_longest_substring(s5)}")
    print(f"Expected: 7")
    print()