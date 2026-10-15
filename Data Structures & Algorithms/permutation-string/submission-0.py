from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        target_counts = Counter(s1)
        window_counts = Counter()

        for right in range(n2):
            # Expand the window by adding the current character
            window_counts[s2[right]] += 1

            # Shrink the window if it exceeds len(s1)
            if right >= n1:
                left_char = s2[right - n1]
                if window_counts[left_char] == 1:
                    del window_counts[left_char]
                else:
                    window_counts[left_char] -= 1

            # Check for match when window size equals len(s1)
            if window_counts == target_counts:
                return True

        return False