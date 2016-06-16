from binary_tree import BinaryNode


class BinarySearchNode(BinaryNode):
    def append(self, other):
        if self.value <= other.value:
            if self.left is None:
                self.left = other
            else:
                self.left.append(other)
        else:
            if self.right is None:
                self.right = other
            else:
                self.right.append(other)

    def __add__(self, other):
        self.append(other)
