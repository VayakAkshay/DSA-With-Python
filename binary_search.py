class binarysearchtree:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binarysearchtree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarysearchtree(data)

    def node_traversal(self):
        elements = []
        if self.left:
            elements += self.left.node_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.node_traversal()
        return elements

    def search(self,element):
        if self.data == element:
            return True
        if element < self.data:
            if self.left:
                return self.left.search(element)
            else:
                return False
        if element > self.data:
            if self.right:
                return self.right.search(element)
            else:
                return False
def build_tree(element):
    root = binarysearchtree(element[0])
    for i in range(len(element)):
        root.add_child(element[i])
    return root

if __name__ == "__main__":
    ele = [33,65,3,465,3,6,57,3,6,7]
    numbers_tree = build_tree(ele)
    print(numbers_tree.search(3356))