class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.buildTrie(words)

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.check(i, j, board, res)
        return res

    def check(self, m, n, board, res):

        def dfs(i,j,curr,path):
            if (i<0 or j<0 or 
                i>=len(board) or 
                j>=len(board[0]) or 
                board[i][j] not in curr.child or
                (i,j) in visited
            ):
                return
            visited.add((i,j))
            path.append(board[i][j])
            curr = curr.child[board[i][j]]
            if curr.is_leaf:
                curr.is_leaf=False
                res.append(''.join(path))
            deltas = [(0,1), (0,-1), (1,0), (-1,0)]
            for di, dj in deltas:
                n_i, n_j = i+di, j+dj
                dfs(n_i,n_j,curr,path)
            visited.remove((i,j))
            path.pop()
        visited = set()
        dfs(m,n,self.TrisHead,[])


    def buildTrie(self, words):
        self.TrisHead = TrieNode()
        for word in words:
            curr = self.TrisHead
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode(val=c)
                curr = curr.child[c]
            curr.is_leaf = True


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.child = {}
        self.is_leaf = False