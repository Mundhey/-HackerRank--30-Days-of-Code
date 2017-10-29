class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def removeDuplicates(self,head):
        self.root=head
        self.pointerA=head
        self.pointerB=head.next

        while self.pointerA.next != None:

         if(self.pointerA.data==self.pointerB.data):
            self.pointerA.next=self.pointerB.next
            self.pointerB=self.pointerA.next
         else:
            self.pointerA=self.pointerA.next
            self.pointerB=self.pointerA.next

        return self.root












mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);