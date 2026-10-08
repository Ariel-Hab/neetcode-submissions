class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest_substring = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # 1. Agregamos el carácter actual al conteo de la ventana
            current_char = s[right]
            count[current_char] = count.get(current_char, 0) + 1
            
            # 2. Actualizamos la frecuencia máxima vista en la ventana
            max_freq = max(max_freq, count[current_char])
            
            # 3. Verificamos si la ventana es inválida
            # Tamaño actual de la ventana = (right - left + 1)
            if (right - left + 1) - max_freq > k:
                # La ventana es inválida, restamos el carácter de la izquierda y la encogemos
                count[s[left]] -= 1
                left += 1
                
            # 4. Actualizamos el tamaño máximo (en este punto la ventana siempre es válida)
            longest_substring = max(longest_substring, right - left + 1)
            
        return longest_substring