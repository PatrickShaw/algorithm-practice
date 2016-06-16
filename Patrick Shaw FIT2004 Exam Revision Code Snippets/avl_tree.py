from binary_search_tree import BinarySearchNode
from binary_tree import BinaryNode


class AVLNode(BinarySearchNode):
    def __init__(self, value, left=None, right=None, parent=None, height=0):
        super().__init__(value, left, right)
        self.__parent = parent
        self.__height = height

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def height(self):
        return self.__height

    def __update_height(self):
        original_height = self.__height
        if self.right is None and self.left is None:
            self.__height = 0
        elif self.right is None:
            self.__height = self.left.height + 1
        else:
            self.__height = self.right.height + 1
        if original_height != self.__height:
            if self.parent is not None:
                self.parent.__update_height()

    def __increment_height(self, increment=1):
        self.__height += increment
        if self.parent is not None:
            self.parent.__update_height()

    def __decrement_height(self, decrement=1):
        self.__height -= decrement
        if self.parent is not None:
            self.parent.__update_height()

    @BinaryNode.left.setter
    def left(self, left):
        if self.left is not None:
            self.left.parent = None
        if left is not None:
            left.parent = self
        BinaryNode.left.fset(self, left)
        self.__update_height()

    @BinaryNode.right.setter
    def right(self, right):
        if self.right is not None:
            self.right.parent = None
        if right is not None:
            right.parent = self
        BinaryNode.right.fset(self, right)
        self.__update_height()

    def __rotate_right(self):
        original_parent = self.parent
        original_right_child = self.right
        self.right = original_right_child.left
        self.right.parent = self
        original_right_child.left = self
        self.parent = original_right_child
        original_right_child.parent = original_parent

    def __rotate_left(self):
        self.__left = self.__parent
        self.__parent = self.__left.__parent
        self.right = self.right

        original_parent = self.parent
        original_left_child = self.parent.left
        self.left = original_left_child.right
        self.left.parent = self
        original_left_child.left = self
        self.parent = original_left_child
        original_left_child.parent = original_parent

    @property
    def subtree_height_difference(self):
        height_difference = (0 if self.left is None else self.left.height) - (0 if self.right is None else self.right.height)
        return height_difference

    def rebalance(self):
        # TODO
        pass

    def append(self, other):
        if other.value <= self.value:
            if self.left is None:
                self.left = other
                self.rebalance()
            else:
                self.left.append(other)
        else:
            if self.right is None:
                self.right = other
                self.rebalance()
            else:
                self.right.append(other)

    def __add__(self, other):
        self.append(other)


if __name__ == "__main__":
    root = AVLNode("f")
    d = AVLNode("d")
    b = AVLNode("b")
    a = AVLNode("a")
    c = AVLNode("c")
    e = AVLNode("e")
    j = AVLNode("j")
    g = AVLNode("g")
    h = AVLNode("h")
    i = AVLNode("i")
    k = AVLNode("k")
    root.append(d)
    root.append(j)
    root.append(b)
    root.append(e)
    root.append(a)
    root.append(c)
    root.append(h)
    root.append(k)
    root.append(g)
    root.append(i)
    print("".join(root.prefix_traversal))
    print("".join(root.infix_traversal))
    print("".join(root.postfix_traversal))
    print(root.height)
    print(h.height)
    print(root.is_binary_search_tree)
    print(root.has_value("k"))
    print(root.has_value("z"))