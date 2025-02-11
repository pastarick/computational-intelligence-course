class Node:
    def __init__(self, data, id=-1, children_ids=[], parent_id=-1):
        # GameMove, value, simulations
        self.data = data
        self.id = id
        self.children_ids = children_ids[:]
        self.parent_id = parent_id
    
    def is_leaf(self):
        return len(self.children_ids) == 0
    
    def is_root(self):
        return self.id == 0
    
    def copy(self):
        return Node(self.data, self.id, self.children_ids[:], self.parent_id)


class Tree:
    def __init__(self, root):
        root.id = 0
        self.nodes = [root]

    def insert(self, node, parent):
        node.id = len(self.nodes)
        node.parent_id = parent.id
        self.nodes.append(node)
        self.nodes[node.parent_id].children_ids.append(node.id)
    
    def get_root(self):
        return self.nodes[0]
    
    def get_children(self, node):
        if not node:
            return []
        arr = []
        for i in range(len(node.children_ids)):
            arr.append(self.nodes[node.children_ids[i]])
        return arr
    
    def get_siblings(self, node):
        return self.get_children(self.get_parent(node))
    
    def get_parent(self, node):
        return self.nodes[node.parent_id]
    
