from structure.list_node import DuelNode


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, node):
        n = DuelNode(node)
        n.prev = self.top
        self.top = n
        self.size += 1

    def pop(self):
        popout = self.top
        self.top = popout.prev if popout is not None else None
        self.size = max(0, self.size-1)
        return popout.val

    def clean(self):
        self.top = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def pop_to(self, stack):
        while self.size > 0:
            stack.push(self.pop())

