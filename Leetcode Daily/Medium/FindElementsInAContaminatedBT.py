# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
  def __init__(self, root: TreeNode | None):
    self.vals = set()
    self.dfs(root, 0)

  def find(self, target: int) -> bool:
    return target in self.vals

  def dfs(self, root: TreeNode | None, val: int) -> None:
    if not root:
      return

    root.val = val
    self.vals.add(val)
    self.dfs(root.left, val * 2 + 1)
    self.dfs(root.right, val * 2 + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)