import sys
class Node(object):
        def __init__(self,data):
                self.data = data
                self.children = []
                self.parent = None
                self.level = 0
                self.root_maxheight = 0
        def add_child(self,child):
                self.children.append(child)
                child.parent = self
                child.level = self.level + 1
                self.update_root_maxheight(child.level)
        def update_root_maxheight(self,height):
                if self.level == 0:
                        self.root_maxheight = height
                else:
                        self.parent.update_root_maxheight(height)
        def print_level(self,level):
                if level == self.level:
                        print self.data,
                else:
                        for child in self.children:
                                if child != None:
                                        child.print_level(level)
        def print_tree(self):
                for i in range(self.root_maxheight + 1):
                        self.print_level(i)
                        print "\n"
        def print_siblings(self):
                for children in self.parent.children:
                        print children.data
        def add_child_BST(self,child,side):
                self.children[side] = child
                child.parent = self
                child.level = self.level + 1
                self.update_root_maxheight(child.level)
def createBST(tree,node):
        left = 0
        right = 1
        if node.data.lower() >= tree.data.lower():
                if tree.children[right] == None:
                        tree.add_child_BST(node,right)
                else:
                        createBST(tree.children[right],node)
        else:
                if tree.children[left] == None:
                        tree.add_child_BST(node,left)
                else:
                        createBST(tree.children[left],node)

def inorderTraverse(root):
        left = 0
        right = 1
        if root.children[left] != None:
                inorderTraverse(root.children[left])
        print root.data
        if root.children[right] != None:
                inorderTraverse(root.children[right])
"""root = Node(0)
child1 = Node(4)
child2 = Node(6)
child3 = Node(9)
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
subchild1 = Node(8)
subchild2 = Node(10)
child2.add_child(subchild1)
child3.add_child(subchild2)
root.print_tree()
subchild2.print_siblings()
#root.print_level(2)
#print root.root_maxheight
"""
#array = sys.stdin.readline().rstrip().split()
array = [2, 5, -2, 6, -3, 8, 0, -7, -9, 4]
names = sys.stdin.readline().rstrip()
root = Node(names)
root.children.append(None)
root.children.append(None)
names = sys.stdin.readline().rstrip()
while names:
        nodeelm = Node(names)
        nodeelm.children.append(None)
        nodeelm.children.append(None)
        createBST(root,nodeelm)
        names = sys.stdin.readline().rstrip()
#root.print_tree()
print root.root_maxheight
inorderTraverse(root)
