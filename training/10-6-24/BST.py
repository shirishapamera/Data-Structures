#binary search tree
class node:
    def _init_(self,x):
        self.data=x
        self.left=None
        self.right=None

class tree:
    def _init_(self):
        self.root=None

    

    def create(self,root,x): 
        if(root==None):
            self.root=node(x)
        elif(x < root.data):
            self.create(root.left,x)
        else:
            self.create(root.right,x)

t1=tree()
t1.create(t1.root,5)
t1.create(t1.root,9)
t1.create(t1.root,2)
t1.create(t1.root,8)
t1.create(t1.root,1)
t1.create(t1.root,4)