# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        lis = []
        def find(ctr):
            if(ctr):
                lis.append(str(ctr.val))
                find(ctr.left)
                find(ctr.right)
            else:
                lis.append("n")
        find(root)
        return ",".join(lis)
    def deserialize(self, data):
        data = data.split(",")
        def find():
            if(self.k<len(data)):
                if(data[self.k]=="n"):
                    self.k+=1
                    return None
                node = TreeNode(int(data[self.k]))
                self.k+=1
                node.left = find()
                node.right = find()
                return node
        self.k = 0
        return find()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))