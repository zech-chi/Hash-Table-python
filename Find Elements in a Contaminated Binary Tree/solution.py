# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.items = set()
        self.items.add(0)
        root.val = 0
        queue = deque()
        queue.append(root)
        while queue:
            cur_node = queue.popleft()
            if cur_node.left:
                self.items.add(2 * cur_node.val + 1)
                cur_node.left.val = 2 * cur_node.val + 1
                queue.append(cur_node.left)
            if cur_node.right:
                self.items.add(2 * cur_node.val + 2)
                cur_node.right.val = 2 * cur_node.val + 2
                queue.append(cur_node.right)
        
    def find(self, target: int) -> bool:
        if target in self.items:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
