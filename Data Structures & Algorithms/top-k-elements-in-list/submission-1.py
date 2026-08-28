from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Cuenta las frecuencias y extrae directamente los k más comunes
        return [item[0] for item in Counter(nums).most_common(k)]