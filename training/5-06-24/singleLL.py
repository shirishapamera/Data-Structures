#single linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()

    def addback(self,data):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(data)

    def addfront(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node

    def addeven(self,t,s):
        if t==None:
            return s
        if t.data%2==0:
            s=s+t.data
        return self.addeven(t.next,s)
        
    def search(self,s):
        t=self.head
        c=0
        while(t!=None):
            if (t.data)==s:
                return "element found"
            t=t.next
        return "element not found"
    
    def middle(self):
        t=self.head
        u=self.head
        while(t!=None and t.next!=None):
            u=u.next
            t=t.next.next
        print("middele element:",u.data)

    def length(self):
        t=self.head
        u=self.head
        c=0
        while(t!=None and t.next!=None):
            u=u.next
            t=t.next.next
            c=c+1
        if t==None:
            print("even length")
        else:
            print("odd length")

    def substr(self):
        t=self.head
        ma=1
        max1=0
        while(t.next!=None):
            if t.data ==((t.next.data)-1):
                ma=ma+1
            else:
                if max1<=ma:
                 max1=ma
                 ma=1
            t=t.next
        if(max1<ma):
           max1=ma
        print(max1)

    def pairs(self):
        t=self.head
        t1=t.next
        while(t.next!=None):
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
            t1=t.next
    def bubblesort(self):
        t=self.head
        p=None
        c=0
        while(t.next!=None):
            t1=self.head
            f=0
            while(t1.next!=p):
                if t1.data>(t1.next.data):
                    f=1
                    t1.data,t1.next.data=t1.next.data,t1.data
                c+=1
                t1=t1.next
            if f==0:
                break
            p=t1
            t=t.next
        return c
        

l1=sll()
l1.head=node(5)
l1.addback(1)
l1.addback(22)
l1.addback(4)
l1.addback(15)
l1.addback(60)
l1.addback(8)
l1.addfront(10)
l1.display()
print(l1.search(30))
print(l1.search(80))
print(l1.addeven(l1.head,0))
l1.middle()
l1.length()
l1.substr()
l1.pairs()
l1.display()
print("no of iterations",l1.bubblesort())
l1.display()
'''
l2=sll()
l2.head=node(100)
l2.addback(200)
l2.addback(300)
l2.addback(400)
l2.addback(500)
l2.addfront(50)
l2.display()
print()
l2.addeven()'''

