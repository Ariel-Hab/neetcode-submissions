class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. Inicializamos la lista con ceros. Ya no necesitamos hacer appends.
        result = [0] * len(temperatures)
        stack = []
        
        for day in range(len(temperatures)):
            # 2. Comparamos directamente con el último elemento de la pila (stack[-1])
            while stack and temperatures[stack[-1]] < temperatures[day]:
                prev_index = stack.pop()
                result[prev_index] = day - prev_index
            
            # El índice actual siempre se agrega a la pila al final
            stack.append(day)
            
        return result