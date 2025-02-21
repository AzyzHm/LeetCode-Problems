# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        self.recover(root, 0)

    def recover(self, node: TreeNode, val: int):
        if node:
            node.val = val
            self.values.add(val)
            self.recover(node.left, 2 * val + 1)
            self.recover(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# Construct the contaminated binary tree
root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)

# Initialize FindElements with the contaminated tree
find_elements = FindElements(root)

# Test find method
print(find_elements.find(1))  # Output: True
print(find_elements.find(3))  # Output: True
print(find_elements.find(5))  # Output: False