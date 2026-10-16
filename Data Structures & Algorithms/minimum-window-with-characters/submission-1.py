from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        window_counts = Counter()

        required = len(target_counts)
        formed = 0

        # Stores (window_length, left_index, right_index)
        min_len = float("inf")
        ans_indices = (0, 0)

        left = 0
        for right, char in enumerate(s):
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Contract window from the left as long as it remains valid
            while left <= right and formed == required:
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    ans_indices = (left, right)

                remove_char = s[left]
                window_counts[remove_char] -= 1
                if remove_char in target_counts and window_counts[remove_char] < target_counts[remove_char]:
                    formed -= 1

                left += 1

        return "" if min_len == float("inf") else s[ans_indices[0] : ans_indices[1] + 1]