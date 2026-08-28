class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for phrase in strs:
            phrase_ordered = tuple(sorted(phrase))
            if phrase_ordered not in hashmap:
                hashmap[phrase_ordered]=[]
            hashmap[phrase_ordered].append(phrase)
        result = list(hashmap.values())
        return(result)  