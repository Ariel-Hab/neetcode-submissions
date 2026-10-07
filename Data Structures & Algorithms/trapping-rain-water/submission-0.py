from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        # 1. Colocamos un puntero en cada extremo
        left = 0
        right = len(height) - 1
        
        # 2. Llevamos el registro de las paredes más altas vistas desde cada lado
        max_left = height[left]
        max_right = height[right]
        
        water = 0
        
        while left < right:
            # El lado con la pared más baja es el que manda, porque por ahí se desbordaría el agua.
            
            if max_left < max_right:
                # Nos movemos desde la izquierda
                left += 1
                
                # Actualizamos la pared máxima de la izquierda (por si encontramos una más alta)
                max_left = max(max_left, height[left])
                
                # Sumamos el agua. Si max_left es igual a height[left] (es decir, acabamos 
                # de subir un escalón), la resta da 0 y no sumamos agua, lo cual es correcto.
                water += max_left - height[left]
                
            else:
                # Nos movemos desde la derecha
                right -= 1
                
                # Actualizamos la pared máxima de la derecha
                max_right = max(max_right, height[right])
                
                # Sumamos el agua basándonos en la pared derecha
                water += max_right - height[right]
                
        return water