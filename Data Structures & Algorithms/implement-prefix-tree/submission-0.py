class PrefixTree:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:  
        curr = self.head
        for c in word:
            if c not in curr.child:
                NewNode = TreeNode(c)
                curr.child[c] = NewNode
            curr = curr.child[c]
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.is_leaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True

class TreeNode:
    def __init__(self, c=None):
        self.child = dict()
        self.char = c
        self.is_leaf = False