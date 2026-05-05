class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def push(self, x: int) -> None:
        new_node = Node(x)
        first_node = self.head.next
        self.head.next = new_node
        first_node.prev = new_node
        new_node.prev = self.head
        new_node.next = first_node

    def pop(self) -> int:
        popped = self.head.next
        self.head.next = popped.next
        return popped.value

    def top(self) -> int:
        return self.head.next.value

    def empty(self) -> bool:
        return self.head.next == self.tail


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()