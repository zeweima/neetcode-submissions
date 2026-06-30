class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.succ = self.tail
        self.tail.pred = self.head
        self.key_value = {}

    def get(self, key: int) -> int:
        # print('get', key, self.key_value)
        if key in self.key_value:
            print(key, self.key_value[key].val)
            
            self.delete_node(self.key_value[key])
            self.insert_node(self.key_value[key])
            return self.key_value[key].val
        # print(-1)
        
        return -1

    def put(self, key: int, value: int) -> None:
        # 
        if key in self.key_value:
            self.key_value[key].val = value
            self.delete_node(self.key_value[key])
        else:
            self.key_value[key] = LinkNode(val=value, key=key)
        
        self.insert_node(self.key_value[key])

        if len(self.key_value)>self.capacity:
            del_node = self.tail.pred
            self.delete_node(del_node)
            del self.key_value[del_node.key]
        print(self.key_value)

    def delete_node(self,node):
        pred = node.pred
        succ = node.succ
        pred.succ = succ
        succ.pred = pred

    def insert_node(self, node):
        node.succ = self.head.succ
        node.pred = self.head
        node.succ.pred = node
        self.head.succ = node

class LinkNode:
    def __init__(self, val=None, key=None):
        self.pred = None
        self.succ = None 
        self.val = val
        self.key = key