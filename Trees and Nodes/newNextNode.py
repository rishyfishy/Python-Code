def findNewNextNode(node):
    #base case: if node is root, return left child
    if not (node.parent):
        return node.left

    #simplest case: if node is a left child, return the parent's right child
    elif node.parent.right!=node:   
        return node.parent.right

    #if node is a right child, return the left child of the parent's "next node"
    #recursion may occur, and will occur to the root if node is (2^integer-1)th node
    else:
        return findNewNextNode(node.Parent).left
