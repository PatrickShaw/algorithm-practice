class MaxHeapArray:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.__array = []
        self.__array.append(None)
        for value in array:
            self.append(value)

    def __getitem__(self, index):
        return self.__array[index]

    def __add__(self, other):
        self.append(other)

    def pop_top(self):
        self.__array[1], self.__array[-1] = self.__array[-1], self.__array[1]
        popped_value = self.__array[-1]
        del self.__array[-1]
        # Rebalanced the tree
        if len(self) > 0:
            self.__rebalance_node_top_down(1)
        return popped_value

    def __len__(self):
        return len(self.__array) - 1

    def __rebalance_node_top_down(self, index_to_rebalance):
        traversed_value = self.__array[index_to_rebalance]
        right_index = self.right_child_index(index_to_rebalance)
        left_index = self.left_child_index(index_to_rebalance)
        if right_index is not None:
            right_value = self.__array[right_index]
            left_value = self.__array[left_index]
            if left_value > traversed_value or right_value > traversed_value:
                if left_value > right_value:
                    self.__array[index_to_rebalance], self.__array[left_index] = self.__array[left_index], self.__array[
                        index_to_rebalance]
                    self.__rebalance_node_top_down(left_index)
                else:
                    self.__array[index_to_rebalance], self.__array[right_index] = self.__array[right_index], \
                                                                                  self.__array[index_to_rebalance]
                    self.__rebalance_node_top_down(right_index)
        elif left_index is not None:
            left_value = self.__array[left_index]
            if left_value > traversed_value:
                self.__array[index_to_rebalance], self.__array[left_index] = self.__array[left_index], self.__array[
                    index_to_rebalance]
                self.__rebalance_node_top_down(left_index)

    def append(self, value):
        self.__array.append(value)
        self.__rebalance_node_bottom_up(len(self.__array) - 1)

    def __rebalance_node_bottom_up(self, index_to_rebalance):
        parent_index = MaxHeapArray.parent_index(index_to_rebalance)
        if parent_index is None:
            return
        if self.__array[parent_index] < self.__array[index_to_rebalance]:
            self.__array[parent_index], self.__array[index_to_rebalance] = self.__array[index_to_rebalance], \
                                                                           self.__array[parent_index]
            self.__rebalance_node_bottom_up(parent_index)

    def is_max_heap(self, node_index=1):
        left_index = self.left_child_index(node_index)
        right_index = self.right_child_index(node_index)
        if left_index is not None:
            if self.__array[left_index] > self.__array[node_index]:
                return False
            elif not self.is_max_heap(left_index):
                return False
        if right_index is not None:
            if self.__array[right_index] > self.__array[node_index]:
                return False
            elif not self.is_max_heap(right_index):
                return False
        return True

    @staticmethod
    def parent_index(index):
        if index <= 1:
            return None
        return index // 2

    def right_child_index(self, index):
        child_index = index * 2 + 1
        return child_index if child_index < len(self.__array) else None

    def left_child_index(self, index):
        child_index = index * 2
        return child_index if child_index < len(self.__array) else None

    @staticmethod
    def is_right_child(index):
        return index % 2 == 1

    def __str__(self):
        return str(self.__array)

    def height(self):
        height = 0
        size = len(self.__array)
        while size > 0:
            height += 1
            size >>= 1
        return height


if __name__ == "__main__":
    max_heap = MaxHeapArray([12, 13123, 1, 2, 12, 2, 2, 3, 1, 12, 2, 23, 1, 2, 222, 22, 22, 21, 1, 1])
    print(max_heap)
    print(max_heap.is_max_heap())
