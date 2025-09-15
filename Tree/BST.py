from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")

    def levelorder(self):
        if self.root is None:
            return
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.key, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
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
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def count_leaves(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Is BST empty?", bst.is_empty())
    print("Node count:", bst.count_nodes())
    print("Search 40:", bst.search(40))
    print("Inorder:", end=" "); bst.inorder(); print()
    print("Preorder:", end=" "); bst.preorder(); print()
    print("Postorder:", end=" "); bst.postorder(); print()
    print("Level-order:", end=" "); bst.levelorder(); print()
    print("Height:", bst.height())
    print("Leaf nodes:", bst.count_leaves())

    bst.delete(70)
    print("After deleting 70, inorder:", end=" "); bst.inorder(); print()
