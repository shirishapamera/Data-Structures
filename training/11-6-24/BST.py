class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
    def sum(self,root):
        if root:
            return self.sum(root.left)+self.sum(root.right)+root.data
        else:
            return 0
    def evensum(self,root):
        if root==None:
            return 0
        if (root.data)%2==0:
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if root==None:
            return 0
        if (root.data)%2!=0:
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def evenodd_diff(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return self.evenodd_diff(root.left)+self.evenodd_diff(root.right) +root.data
        else:
            return self.evenodd_diff(root.left)+self.evenodd_diff(root.right)-root.data
        
        
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def balance_tree(self,root):
        return abs((self.height(root.left))-self.height(root.right))<=1
    
    def leaf_nodes(self,root):
        if root==None:
            return 0
        elif root.right==None and root.left==None:
            return 1
        return self.leaf_nodes(root.left)+self.leaf_nodes(root.right)
    
    def leaf_node_sum(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return root.data
        return self.leaf_node_sum(root.left)+self.leaf_node_sum(root.right)
    
    def search(self,root,x):
        if root==None:
            return 0
        if root.data==x:
            return 1
        elif x<root.data:
            return self.search(root.left,x)
        elif x>root.data:
            return self.search(root.right,x)
        
    def depth(self,root,x):
        if self.search(root,x):
            if root.data==x:
                return 0
            elif x<root.data:
                return 1+self.depth(root.left,x)
            else:
                return 1+self.depth(root.right,x)
        else:
            return -1
        '''
        if root.data==x:
                return c
            elif x<root.data:
                return 1+self.depth(root.left,x,c+1)
            else:
                return 1+self.depth(root.right,x,c+1)
        
        '''
    def left_view(self,root,c,l):
        if root==None:
            return
        if c not in l: 
           print(root.data)
           l.append(c)
        self.left_view(root.left,c+1,l)
        self.left_view(root.right,c+1,l)
    def right_view(self,root,c,l):
        if root==None:
            return
        if c not in l: 
           print(root.data)
           l.append(c)
        self.right_view(root.right,c+1,l)
        self.right_view(root.left,c+1,l)
    def top_view(self,root):
        if root==None:
            return
        q=[(root,0)]
        d={}
        while q:
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            if q[0][1] not in d:
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
    def bottom_view(self,root):
        if root==None:
            return
        q=[(root,0)]
        d={}
        while q:
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")

            

    
t1=Tree()
t1.root=Node(10)
t1.create(t1.root, 5)
t1.create(t1.root, 15)
t1.create(t1.root, 2)
t1.create(t1.root, 7)
t1.create(t1.root, 11)
t1.create(t1.root, 20)
t1.create(t1.root, 4)
t1.create(t1.root, 3)
t1.create(t1.root, 12)
t1.create(t1.root, 13)
t1.create(t1.root, 14)
#t1.create(t1.root, 1)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print("alll")
print("sum of all nodes in tree",t1.sum(t1.root))
print("left subtree sum",t1.sum(t1.root.left))
print("left subtree - right subtree",t1.sum(t1.root.left)-t1.sum(t1.root.right))
print("even sum",t1.evensum(t1.root))
print("odd sum",t1.oddsum(t1.root))
print("even odd sum difference",abs(t1.evenodd_diff(t1.root)))
print("height of tree",(t1.height(t1.root)))
x=t1.balance_tree(t1.root)
if x:
    print("balanced")
else:
    print("not balanced")
print("no of leaf node",t1.leaf_nodes(t1.root))
print("leaf node sum",t1.leaf_node_sum(t1.root))
print(t1.search(t1.root,62))
print("depth of tree:",t1.depth(t1.root,70))
print("left view")
t1.left_view(t1.root,0,[])
print("right view")
t1.right_view(t1.root,0,[])
print("top view")
t1.top_view(t1.root)
print()
print("bottom view")
t1.bottom_view(t1.root)



