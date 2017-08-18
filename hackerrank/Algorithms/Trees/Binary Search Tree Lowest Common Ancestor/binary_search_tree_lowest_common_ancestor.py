def traverse(node, search_value):
    if node.data < search_value:
        return node.right
    elif node.data > search_value:
        return node.left
    else:
        return None
    
def lca(root , v1 , v2):
    t1 = traverse(root, v1)
    t2 = traverse(root, v2)
    while t1 is not None and t2 is not None and t1.data == t2.data:
        root = t1
        t1 = traverse(root, v1)
        t2 = traverse(root, v2)
    return root