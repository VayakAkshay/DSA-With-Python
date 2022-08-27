from email.errors import NonPrintableDefect


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    def addbeginvalue(self,data):
        node = Node(data,self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list in empty")
            return
        itr = self.head
        # print("itr = ",itr)
        listr = ''
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)
    def addendvalue(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def getlength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def removedata(self,index):
        if index<0 or index>=self.getlength():
            print("Invalid input")
        
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index>=self.getlength():
            print("Invalid input")
        if index==0:
            self.addbeginvalue(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

if __name__ == "__main__":
    l1 = linkedlist()
    l1.addbeginvalue(5)
    l1.addbeginvalue(21)
    l1.addendvalue(54)
    l1.addendvalue(13)
    l1.print()
    l1.removedata(2)
    l1.print()
    l1.insert_at(2,65)
    l1.print()