class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, value):
        def _insert(root, value):
            if not root:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            elif value > root.value:
                root.right = _insert(root.right, value)
            return root

        self.root = _insert(self.root, value)

    # Check if tree contains a value
    def contains(self, value):
        def _contains(root, value):
            if not root:
                return False
            if value == root.value:
                return True
            elif value < root.value:
                return _contains(root.left, value)
            else:
                return _contains(root.right, value)

        return _contains(self.root, value)

    # Delete a node ( in-order successor logic )
    def delete(self, value):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(root, value):
            if not root:
                return root
            if value < root.value:
                root.left = _delete(root.left, value)
            elif value > root.value:
                root.right = _delete(root.right, value)
            else:
                # Node with one child or no child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                # Node with two children
                temp = _min_value_node(root.right)
                root.value = temp.value
                root.right = _delete(root.right, temp.value)
            return root

        self.root = _delete(self.root, value)

    # In-order Traversal (Left, Root, Right)
    def inorder(self):
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

    # Pre-order Traversal (Root, Left, Right)
    def preorder(self):
        result = []

        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    # Post-order Traversal (Left, Right, Root)
    def postorder(self):
        result = []

        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)

        _postorder(self.root)
        return result


bst = BST()
values = [10, 5, 15, 2, 7, 12, 20]
for val in values:
    bst.insert(val)

print("Inorder:", bst.inorder())     # [2, 5, 7, 10, 12, 15, 20]
print("Preorder:", bst.preorder())   # [10, 5, 2, 7, 15, 12, 20]
print("Postorder:", bst.postorder()) # [2, 7, 5, 12, 20, 15, 10]

print("Contains 7?", bst.contains(7))        # True
print("Contains 100?", bst.contains(100))    # False

bst.delete(10)  # Deleting root node
print("Inorder after deleting 10:", bst.inorder())  # [2, 5, 7, 12, 15, 20]

print("Closest to 13:", bst.find_closest(13))  # 12

print("Is valid BST?", bst.is_valid_bst())     # True
