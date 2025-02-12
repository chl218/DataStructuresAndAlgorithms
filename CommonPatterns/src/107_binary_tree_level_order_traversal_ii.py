class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()
                if node is not None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res[::-1]