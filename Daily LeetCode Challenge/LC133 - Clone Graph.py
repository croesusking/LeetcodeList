class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #LC133 - Clone Graph
        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]

            copy = Node(node.val)
            oldtoNew[node]=copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node) if node else None