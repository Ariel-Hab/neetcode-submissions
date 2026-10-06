class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for day in range(len(temperatures)):
            if not stack:
                result.append(0)
                stack.append(day)
            else:
                while stack:
                    prev_index = stack.pop()
                    if(temperatures[prev_index] < temperatures[day]):
                        result[prev_index] = day-prev_index
                    else: 
                        stack.append(prev_index)
                        break
                result.append(0)
                stack.append(day)
        return result