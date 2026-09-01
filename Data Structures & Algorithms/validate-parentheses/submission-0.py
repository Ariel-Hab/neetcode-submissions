class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # A dictionary mapping closing brackets to their matching open brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop the top element if stack isn't empty, otherwise use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched. If not, it's invalid.
        return len(stack)==0