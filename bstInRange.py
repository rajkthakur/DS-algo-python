#this function implements extracting values from BST in the given range
def bstInRange(root,k1,k2):
    if root is None or root.data<k1 or root.data >k2:
        return
    bstInRange(root.left,k1,k2)
    print str(root.data)+" ",
    bstInRange(root.right,k1,k2)
