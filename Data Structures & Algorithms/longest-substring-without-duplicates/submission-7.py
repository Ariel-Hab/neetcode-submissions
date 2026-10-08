class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicc = {}
        longest_substring = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If we've seen the character AND it's inside our current window
            if current_char in dicc and dicc[current_char] >= left:
                # Move the left pointer to the right of the previous duplicate
                left = dicc[current_char] + 1
                
            # Update the latest index of the character
            dicc[current_char] = right
            
            # Calculate current window size and update max
            current_length = right - left + 1
            if current_length > longest_substring:
                longest_substring = current_length
                
        return longest_substring