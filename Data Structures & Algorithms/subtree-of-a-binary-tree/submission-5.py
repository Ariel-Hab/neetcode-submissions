class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Caso base: un subRoot vacío siempre es subárbol de cualquier árbol
        if not subRoot:
            return True
        
        # Si el árbol principal está vacío pero subRoot no, no puede ser subárbol
        if not root:
            return False

        # 1. Si son exactamente idénticos desde el nodo actual
        if self.isSameTree(root, subRoot):
            return True

        # 2. Si no, busca recursivamente en los hijos izquierdo y derecho
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)