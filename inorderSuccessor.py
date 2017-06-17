# cook your code here
#node class
class Node:
    def __init__(self,key):
        self.data = key
        self.left=None
        self.right=None
#function to get the inorder successor       
def inorderSucc(root,target):
    #if there are child to the right of target node then take the node that has minimum value
    if target.right is not None:
        return getMin(target.right)
    #else the parent of the target that is left to its parent
    ans = None
    while root is not None:
        if target.data < root.data:
            ans = root
            root = root.left
        else:
            root=root.right
            
    return ans
 #helper function to get minimum valued node   
def getMin(root):
    if root.left is None:
        return root
    root = root.left
    
#helper function to construct tree 
def insert(root,data):
    if  root is None:
        return Node(data)
    if data < root.data :
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right,data)
      
    return root
#helper function to print tree in inorder traversal 
def inorderPrint(root):
    if root is None:
        return
    inorderPrint(root.left)
    print str(root.data)+" ",
    inorderPrint(root.right)
root=None
root = insert(root,10)
insert(root, 5)
insert(root, 15)
insert(root, 56)
insert(root, 13)
insert(root, 8)

inorderPrint(root)
print
print inorderSucc(root,root.left.right).data

        
    
    
