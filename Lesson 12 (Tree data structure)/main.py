class tree:
    def __init__(self,data):
        self.data = data
        self.leftnode = None
        self.rightnode = None
#in order traversal
#left, root, right
def inordertraversal(root):
    if root.leftnode != None:
        inordertraversal(root.leftnode)
    print(root.data)
    if root.rightnode != None:
        inordertraversal(root.rightnode)
#pre order traversal, traverses root, then left, then right
def preordertraversal(root):
    print(root.data)
    if root.leftnode != None:
        preordertraversal(root.leftnode)
    if root.rightnode != None:
        preordertraversal(root.rightnode)
#post order traversal, left, right, root
def postordertraversal(root):
    if root.leftnode != None:
        postordertraversal(root.leftnode)
    if root.rightnode != None:
        postordertraversal(root.rightnode)
    print(root.data)
#creating binary tree
root = tree(10)
root.leftnode = tree(5)
root.leftnode.leftnode = tree(3)
root.rightnode = tree(12)
root.rightnode.leftnode = tree(11)
root.rightnode.rightnode = tree(13)
#executing traversal
inordertraversal(root)
preordertraversal(root)
postordertraversal(root)