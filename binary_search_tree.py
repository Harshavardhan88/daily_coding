# binary search tree - left child is smaller, right child is bigger

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, value):
    if root is None:
        return None
    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        # node with only one child or no child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # node with two children: replace with smallest in right side
        smallest = find_min(root.right)
        root.value = smallest.value
        root.right = delete(root.right, smallest.value)
    return root


def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


tree = None
for num in [10, 5, 15, 3, 7, 12, 18]:
    tree = insert(tree, num)

print(inorder(tree, []))
print(search(tree, 7) is not None)
print(search(tree, 99) is not None)

tree = delete(tree, 5)
print(inorder(tree, []))
tree = delete(tree, 10)
print(inorder(tree, []))
