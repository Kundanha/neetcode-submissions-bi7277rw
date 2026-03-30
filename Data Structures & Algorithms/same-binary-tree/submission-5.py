# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodep = q1.popleft()
                nodeq = q2.popleft()
                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False
                q1.append(nodep.left)
                q1.append(nodep.right)
                q2.append(nodeq.left)
                q2.append(nodeq.right)
        return True

        