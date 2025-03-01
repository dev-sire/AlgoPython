# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
    i = 0

    def recoverFromPreorder(depth: int) -> TreeNode | None:
      nonlocal i
      nDashes = 0
      while i + nDashes < len(traversal) and traversal[i + nDashes] == '-':
        nDashes += 1
      if nDashes != depth:
        return None

      i += depth
      start = i
      while i < len(traversal) and traversal[i].isdigit():
        i += 1

      return TreeNode(int(traversal[start:i]),
                      recoverFromPreorder(depth + 1),
                      recoverFromPreorder(depth + 1))

    return recoverFromPreorder(0)