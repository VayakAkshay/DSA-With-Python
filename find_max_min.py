from xml.dom.minidom import Element


class dataoftree:
    def __init__(self,data):
        self.data = data
        self.min = None
        self.max = None
        self.left = None
        self.right = None
        self.element = []
    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = dataoftree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = dataoftree(data)
    def traversal(self):
        # element = []
        if self.left:
            self.element += self.left.traversal()
        self.element.append(self.data)
        if self.right:
            self.element += self.right.traversal()
        return self.element
    def find_max(self):
        number = 0
        for i in range(len(self.element)):
            if number < self.element[i]:
                number = self.element[i]
            else:
                number = number
        return number
    def find_min(self):
        number = self.element[0]
        for i in range(len(self.element)):
            if self.element[i] < number:
                number = self.element[i]
            else:
                number = number
        return number
def build_tree(element):
    root = dataoftree(element[0])
    for i in range(len(element)):
        root.add_child(element[i])
    return root

if __name__ == "__main__":
    ele = [3,54,64,5245,76,86,786,54,5]
    number_tree = build_tree(ele)
    print(number_tree.traversal())
    print(number_tree.find_max())
    print(number_tree.find_min())