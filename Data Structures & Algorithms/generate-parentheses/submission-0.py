class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parenthesis = ""
        def dfs(abiertos:int, cerrados:int):
            nonlocal parenthesis
            #decision: por cada nodo, puedo cerrar ahora si hay pendiete o abrir uno nuevo si tengo resto
            if abiertos == n and cerrados == n:
                res.append(parenthesis)
                return
            if len(parenthesis) > n*2:
                return

            if abiertos <= n:
                parenthesis += "("
                dfs(abiertos+1,cerrados)
                parenthesis = parenthesis[:-1]

            if cerrados < abiertos:
                parenthesis += ")"
                dfs(abiertos,cerrados+1)
                parenthesis = parenthesis[:-1]
        dfs(0,0)
        return res



