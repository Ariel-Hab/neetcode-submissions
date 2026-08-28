class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the delimiter '#' instantly without a manual inner loop
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Jump straight to the start of the next string
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            i = end
        return res