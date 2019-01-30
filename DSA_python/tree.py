class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
    
    def bfs(self):
        row = [self.root]
        while row:
            print(" ".join(map(lambda x: str(x.value), row)))
            row = [kid for item in row for kid in (item.left, item.right) if kid]
    
    def preorder(self,root):
        if root != None:
            print(root.value,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print(root.value,end=" ")
            self.inorder(root.right)
    def postorder(self,root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value,end=" ")

    def maxdepth(self, root):
        if not root:
            return 0
        return max(self.maxdepth(root.left),self.maxdepth(root.right))+1
    
    def is_same(self, a, b):
        if a == None and b == None:
            return True
        elif a and b:
            return a.value == b.value and self.is_same(a.left,b.left) and self.is_same(a.right,b.right)
        else:
            return False
        

if __name__ == "__main__":

    root = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    tree = Tree(root)
    
    print("BFS traversal: ")
    tree.bfs()

    print("Preorder traversal:")
    tree.preorder(root)
    print("\n")

    print("Inorder traversal:")
    tree.inorder(root)
    print("\n")

    print("Postorder traversal:")
    tree.postorder(root)
    print("\n")

    print("Max Depth of the tree is %d" % tree.maxdepth(root))

    root2 = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    print("The tree are same" if tree.is_same(root,root2) else "Thre tree are different")

    

