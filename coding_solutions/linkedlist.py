class Linkly:
    def __init__(self):
        self.top=None

    def forward_Insert(self,data):
        node=Node(data)
        if self.top:
            node.next=self.top
            self.top=node
        else:
            self.top=node
    def delete(self,key):
        cu=self.top
        found=0
        if cu.data==key:
            self.top=cu.next
            cu.next=None
        else:
            while cu.next!=None:
                if key==cu.next.data:
                    found=1
                    break
                cu=cu.next
            if found:        
                cu.next=cu.next.next
            else:
                print("Element not found")
        
    def display(self):
        current=self.top
        print("The current list is ")
        while current:
            print(current.data,end="===>")
            current=current.next
        print()
class Node():        
  def __init__(self,data):
        self.data=data
        self.next=None      

n=Linkly()
while(1):
    data1=input("enter the data to be inserted in list: ")
    print()
    n.forward_Insert(data1)
    n.display()
    data2=input("Do you want to delete if yes press 1 :")
    print()
    if data2=="1":
        data3=input("Enter the element to be deleted :")
        n.delete(data3)
        n.display()
    
