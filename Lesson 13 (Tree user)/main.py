class tree:
    def __init__(self,data):
        self.data = data
        self.leftnode = None
        self.rightnode = None
#function to insert new values
def insert(root,val1):
    if root == None:
        return tree(val1)
    if root.data > val1:
        root.leftnode = insert(root.leftnode,val1)
    else:
        root.rightnode = insert(root.rightnode, val1)
    return root
#function for searching
def search(root,key):
    if root.data == key:
        return root
    elif root.data > key and root.leftnode != None:
        return search(root.leftnode,key)
    elif root.data < key and root.rightnode != None:
        return search(root.rightnode,key)
    else:
        return -1
def inordertraversal(root):
    if root.leftnode != None:
        inordertraversal(root.leftnode)
    print(root.data)
    if root.rightnode != None:
        inordertraversal(root.rightnode)
#function for minimum value
def minimum(root):
    if root == None:
        return None
    while root.leftnode is not None:
        root = root.leftnode
    return root.data

#ask the user how many elements they want
elementcount = int(input("How many elements would you like?"))
root = None
for i in range(elementcount):
    element = int(input("What would you like to add?"))
    root = insert(root,element)

inordertraversal(root)

#Ask user what they are searching for
usersearch = int(input("What are you searching for?"))
node = search(root,usersearch)
if node == -1:
    print("Value does not exist! Try again")
else:
    print("Element exists", node.data)
print("Minimum is ", minimum(root))