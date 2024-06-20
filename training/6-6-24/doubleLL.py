#double linked list
class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next

    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<-")
            t=t.prev
        print()

    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if (t.data)==x or (t1.data)==x:
                return 1
            t=t.next
            t1=t1.prev
        if t.data==x:
            return "element found"
        else:
            return "element not found"
    def length(self):
        c=0
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if t==t1:
            return "odd"
        else:
            return "even"
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if(t.data==t1.data):
                return 0
            t=t.next
            t1=t1.prev
        return 1
    def change(self):
        t=self.head
        t1=self.tail
        while(t!=t1.next):                      
            t=t.next
            t1=t1.prev
        u=self.head
        while(t!=None):
            u.data,t.data=t.data,u.data
            u=u.next
            t=t.next
        l1.display()
    def links_change(self):
        t=self.head 
        while(t!=None):
            t1=t.next
            if(t==self.head):
                t.next,t1.next=t1.next,t
                t.prev,t1.prev=t1,None 
                t.next.prev=t
                self.head=t1
            else:
                t.next,t1.next=t1.next,t
                t1.prev,t.prev=t.prev,t1
                if(t.next!=None):
                    t.next.prev=t
                t1.prev.next=t1    
            t=t.next
    def evenoddsumdiff(self,t,es,os):
            if t==None:
                return abs(es-os)
            if t.data%2==0:
                es=es+t.data
            else:
                os=os+t.data
            t=t.next
            return self.evenoddsumdiff(t,es,os)

    def prime(self,t,c):
        if t==None:
            return c
        def pn(s,n):
            if(s>(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pn(s+1,n)
        if(pn(2,t.data)):
            c=c+1
        return self.prime(t.next,c)
            
            
        
        

    

        
    

    
l1=dll()
#l1.addfront(20)
l1.addback(1)
l1.addback(2)
l1.addback(3)
l1.addback(7)
l1.addback(5)
l1.addback(13)
l1.display()
l1.rev_display()
print(l1.search(50))
print(l1.search(80))
print(l1.length())
print(l1.palindrome())
l1.display()
#l1.change()
l1.links_change()
l1.display()
#l1.balance_string()
print("even and odd sum difference",l1.evenoddsumdiff(l1.head,0,0))
print(l1.prime(l1.head,0))





    