class Node:
    def __init__(self, data= None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        llist=[]
        count = 0
        while itr:
            llist.append(itr.data)
            count+= 1
            itr=itr.next
        print("Required Linked List is-->",llist)
        return
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        print("Length is", count)
        return
    def insert_at_begining(self,data):
        node = Node(data , self.head)
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, None)
    def insert_at(self, index, data):
        if index<0 or index==self.get_length:
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index<0 or index==self.get_length:
            raise Exception('Invalid Index number')
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                 itr.next = itr.next.next
                 break
            itr=itr.next
            count+=1
                
    def insert_values(self , data_list):
        self.head = None
        for val in data_list:
            self.insert_at_end(val)
        return
    def insert_after_index(self ,index,data):
        if index<0 or index==self.get_length:
            raise Exception("Invalid Index")
        if index==0:
            node=Node(data,self.head.next)
            self.head.next=node
        itr=self.head
        count=0
        while itr.next:
            if count==index:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    def insert_after_value(self ,data_after,data_insert):
        itr=self.head
        count=0
        while itr:
            if data_after==itr.data:
                node = Node(data_insert, itr.next)
                itr.next = node
                return
                break
            count+=1
            itr=itr.next
    def remove_by_value(self,data):
        itr=self.head
        count=0
        while itr:
            if data==itr.data:
                self.remove_at(count)
                return
                break
            count+=1
            itr=itr.next
        else:
            raise Exception("Value not found")

if __name__=="__main__":
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    ll.insert_at_end(24)
    ll.remove_by_value("figs")