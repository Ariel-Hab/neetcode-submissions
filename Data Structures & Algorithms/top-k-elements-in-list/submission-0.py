class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            if n in hashmap:
                hashmap[n] = hashmap[n]+1
            else:
                hashmap[n] = 1

        ordered_list = sorted(hashmap.keys(), key=lambda x: hashmap[x],reverse=True)
        return ordered_list[:k]