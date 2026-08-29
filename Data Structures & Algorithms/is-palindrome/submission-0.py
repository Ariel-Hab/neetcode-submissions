class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at the start and end of the string
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move the left pointer if it's not looking at a letter/number
            if not s[left].isalnum():
                left += 1
                continue
            
            # Move the right pointer if it's not looking at a letter/number
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Compare the characters (lowercased)
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True