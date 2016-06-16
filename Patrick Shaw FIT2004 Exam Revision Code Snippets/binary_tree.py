class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def prefix_traversal(self):
        traversed_nodes = [self.value]
        if self.left is not None:
            traversed_nodes.extend(self.left.prefix_traversal)
        if self.right is not None:
            traversed_nodes.extend(self.right.prefix_traversal)
        return traversed_nodes

    @property
    def infix_traversal(self):
        traversed_nodes = []
        if self.left is not None:
            traversed_nodes.extend(self.left.infix_traversal)
        traversed_nodes.append(self.value)
        if self.right is not None:
            traversed_nodes.extend(self.right.infix_traversal)
        return traversed_nodes

    @property
    def postfix_traversal(self):
        traversed_nodes = []
        if self.left is not None:
            traversed_nodes.extend(self.left.postfix_traversal)
        if self.right is not None:
            traversed_nodes.extend(self.right.postfix_traversal)
        traversed_nodes.append(self.value)
        return traversed_nodes



if __name__ == "__main__":
    root = BinaryNode("f")
    d = BinaryNode("d")
    b = BinaryNode("b")
    a = BinaryNode("a")
    c = BinaryNode("c")
    e = BinaryNode("e")
    j = BinaryNode("j")
    g = BinaryNode("g")
    h = BinaryNode("h")
    i = BinaryNode("i")
    k = BinaryNode("k")
    root.left = d
    root.right = j
    d.left = b
    d.right = e
    b.left = a
    b.right = c
    j.left = h
    j.right = k
    h.left = g
    h.right = i
    print("".join(root.prefix_traversal))
    print("".join(root.infix_traversal))
    print("".join(root.postfix_traversal))

