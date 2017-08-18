static Node traverse(Node node, int searchValue) {
    if (searchValue > node.data) {
        return node.right;
    } else if(searchValue < node.data) {
        return node.left;
    } else {
        return null;
    }
}
static Node lca(Node root,int v1,int v2)
    {
        Node t1 = root;
        Node t2 = root;
        // Wouldn't probably make this null but wanna save on memory :P
        while(true) {
            Node newT1 = traverse(root, v1);
            Node newT2 = traverse(root, v2);
            if (newT1 == null || newT2 == null || newT1.data != newT2.data) {
                break;
            }
            root = newT1;
        }
        return root;
    }
