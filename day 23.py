import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):

            h = self.height(root)
            for i in range(1, h + 1):
                self.printGivenLevel(root, i)


    def printGivenLevel(self,root, level):
            if root is None:
                return
            if level == 1:
                print "%d" % (root.data),
            elif level > 1:
                self.printGivenLevel(root.left, level - 1)
                self.printGivenLevel(root.right, level - 1)


    def height(self,node):
            if node is None:
                return 0
            else:

                lheight = self.height(node.left)
                rheight = self.height(node.right)


                if lheight > rheight:
                    return lheight + 1
                else:
                    return rheight + 1









T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
 data = int(raw_input())
 root = myTree.insert(root, data)
myTree.levelOrder(root)