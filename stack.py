class stackdata:
    def __init__(self,data):
        self.data = data
        self.item = []

    def add_item(self,ele):
        self.item.insert(0,ele)

    def traversal(self):
        return self.item

    def remove_item(self):
        self.item.pop()
        return self.item

def build_stack(element):
    node = stackdata(element[0])
    for i in range(len(element)):
        node.add_item(element[i])
    return node

if __name__ == "__main__":
    ele = [2,4,5,6,3,5,6,6]
    new_stack = build_stack(ele)
    print(new_stack.traversal())
    print(new_stack.remove_item())