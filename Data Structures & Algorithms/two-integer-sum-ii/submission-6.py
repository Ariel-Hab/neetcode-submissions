class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #O(n) because i iterate only once the whole array
        left = 0
        right = len(numbers)-1
        while left < right:
            current_sum = numbers[left]+numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        
        
        #O(n**2)
        # for n1 in numbers:
        #     for n2 in numbers:
        #         if n1 == n2:
        #             continue
        #         elif n1+n2 == target:
        #             return [n1,n2]
