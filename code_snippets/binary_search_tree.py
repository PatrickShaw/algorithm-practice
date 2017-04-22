from binary_tree import BinaryNode


class BinarySearchNode(BinaryNode):
    def append(self, other):
        if other.value <= self.value:
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

    def search_for_node(self, value):
        if self.value == value:
            return self
        if value <= self.value:
            if self.left is not None:
                return self.left.search_for_node(value)
        else:
            if self.right is not None:
                return self.right.search_for_node(value)

    def has_value(self, value):
        return self.search_for_node(value) is not None
