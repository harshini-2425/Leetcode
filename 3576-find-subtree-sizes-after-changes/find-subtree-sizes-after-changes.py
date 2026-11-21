class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]

        last = [-1] * 26

        def dfs(node):
            idx = ord(s[node]) - ord('a')

            old = last[idx]

            if old != -1:
                new_parent = old
            else:
                new_parent = parent[node]

            if node != 0:
                new_children[new_parent].append(node)

            last[idx] = node

            for child in children[node]:
                dfs(child)

            last[idx] = old

        dfs(0)

        # Calculate subtree sizes in the modified tree
        ans = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                ans[node] += ans[child]

        calculate(0)

        return ans
        