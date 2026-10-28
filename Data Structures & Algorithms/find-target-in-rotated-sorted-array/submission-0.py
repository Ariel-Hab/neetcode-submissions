class Solution:
    def binSearch(self, nums: List[int], target: int) -> int:
        lower = 0
        higher = len(nums) -1 
        while lower <= higher:
            index = (lower + higher)//2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                lower = index + 1
            else:
                higher = index - 1
            
        return -1
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:  #Uso < ya que quiero cortar cuando son iguales
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def search(self, nums: List[int], target: int) -> int:
        minPos = self.findMin(nums)
        print(minPos)
        indice = self.binSearch(nums[minPos:(len(nums))], target) 
        print(indice)
        indice += minPos
        print(indice)
        if (nums[indice] == target):
            return indice
        elif minPos != 0:
            indice = self.binSearch(nums[0:(minPos)], target)
            print(indice)
            if (nums[indice] == target):
                return indice   
        return -1
        