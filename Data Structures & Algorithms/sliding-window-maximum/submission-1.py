class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
        
        # Una lista común que guardará tuplas: (indice, valor)
        ventana = []  
        output = []
        
        for i in range(len(nums)):
            valor_actual = nums[i]
            
            # 1. Eliminar el elemento que quedó fuera de la ventana por la izquierda
            # Al usar ventana[0][0], miramos el índice del primer elemento de la lista.
            if ventana and ventana[0][0] <= i - k:
                ventana.pop(0)  # <-- Aquí eliminamos el primero (Operación Lenta)
                
            # 2. Mantener la lista ordenada eliminando los más chicos por la derecha
            # Comparamos el valor_actual con el valor del último elemento (ventana[-1][1])
            while ventana and ventana[-1][1] < valor_actual:
                ventana.pop()   # <-- Eliminar del final (Operación Rápida)
                
            # 3. Añadir el elemento actual (posición, valor) al final de la lista
            ventana.append((i, valor_actual))
            
            # 4. Si ya cubrimos el tamaño de la primera ventana, guardamos el máximo.
            # Como la lista se mantiene ordenada, el máximo siempre está al principio (ventana[0][1]).
            if i >= k - 1:
                output.append(ventana[0][1])
                
        return output
