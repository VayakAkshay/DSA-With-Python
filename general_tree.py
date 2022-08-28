class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def addchild(self,child):
        child.parent = self
        self.children.append(child)
    def printdata(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printdata()

def build_product():
    root = Treenode("Electric")
    leptop = Treenode("Leptop")
    leptop.addchild(Treenode("Dell"))
    leptop.addchild(Treenode("Thinkpad"))
    root.addchild(leptop)
    return root
if __name__ == "__main__":
    root = build_product()
    root.printdata()
    pass