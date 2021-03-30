# If you had a sorted list of numbers
# How about if you need to sort a list of numbers
# When would you use, say,
# Do you know what "blocking" is.
# I have two threads running simulataneously
class LinkedNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

def array_to_linked_nodes(initial_list):
  def value_to_node(value):
    return LinkedNode(value)

  nodes = list(map(value_to_node, initial_list))

  for n in range(len(nodes) - 1):
    nodes[n].next = nodes[n + 1]

  return nodes[0]

def print_linked_list(head):
  # just for debugging
  current = head
  while current is not None:
    print(current.value)
    current = current.next

def reverse_linked_list(head):
  previous = None
  current = head

  while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

  return previous

head = array_to_linked_nodes([1, 2, 3, 4, 5])

print_linked_list(head)

# reversing
reversed_node = reverse_linked_list(head)

print()
print_linked_list(reversed_node)