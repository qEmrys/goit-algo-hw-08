class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        result = []
        if node is not None:
            result.extend(self._inorder_recursive(node.left))
            result.append(node.key)
            result.extend(self._inorder_recursive(node.right))
        return result

    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def sum_all(self):
        return self._sum_all_recursive(self.root)
    
    def _sum_all_recursive(self, node):
        if node is None:
            return 0
        return node.key + self._sum_all_recursive(node.left) + self._sum_all_recursive(node.right)
