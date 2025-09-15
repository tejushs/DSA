class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1   

class BST:
    def __init__(self):
        self.root = None

    def _update_size(self, node):
        if node:
            left_size = node.left.size if node.left else 0
            right_size = node.right.size if node.right else 0
            node.size = 1 + left_size + right_size

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        self._update_size(node)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        self._update_size(node)
        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(f"{node.key} (size={node.size})", end=" ")
            self.inorder(node.right)


if __name__ == "__main__":
    bst = BST()
    for x in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(x)

    print("Inorder with subtree sizes:")
    bst.inorder()
    print("\nRoot size:", bst.root.size)

    bst.delete(70)
    print("\nAfter deleting 70:")
    bst.inorder()
    print("\nRoot size:", bst.root.size)
