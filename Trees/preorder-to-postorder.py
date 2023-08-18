#User function Template for python3
# https://practice.geeksforgeeks.org/problems/preorder-to-postorder4423/1
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def construct_tree(root,val):
    if root:
        if val>root.data:
            root.right=construct_tree(root.right,val)
        elif val<root.data:
            root.left=construct_tree(root.left,val)
        return root
    else:
        return Node(val)
def post_order(pre, size) -> Node:
    #code here
    if size==0:
        return None
    else:
        root=Node(pre[0])
        for i in range(1,len(pre)):
            root=construct_tree(root,pre[i])
    return root