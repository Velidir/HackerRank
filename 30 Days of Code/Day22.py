def getHeight(self, root):
    if root is None:
        return -1
    else:
        depthLeft = self.getHeight(root.left) + 1
        depthRight = self.getHeight(root.right) + 1
        depth = max([depthLeft, depthRight])
        return depth