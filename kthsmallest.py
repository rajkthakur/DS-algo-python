# function to search the kth smallest value in a BST(Binary Search Tree)
#pass the root of the tree and the kth value
tar = 0
def kthSmallest(root, k):
    global tar
    if root is None:
        return
    kthSmallest(root.left,k)
    tar=tar+1
    if tar==k:
        print root.data
    kthSmallest(root.right,k)
