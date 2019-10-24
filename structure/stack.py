from structure.list_node import DuelNode


class Stack:
    def __init__(self):
        self.m_top = None
        self.m_size = 0

    def push(self, node):
        n = DuelNode(node)
        n.prev = self.m_top
        self.m_top = n
        self.m_size += 1

    def pop(self):
        popout = self.m_top
        self.m_top = popout.prev if popout is not None else None
        self.m_size = max(0, self.m_size-1)
        return popout.val if popout is not None else None

    def clean(self):
        self.m_top = None
        self.m_size = 0

    def size(self):
        return self.m_size

    def top(self):
        return self.m_top.val if self.m_top is not None else None

    def empty(self):
        return self.m_size == 0

    def pop_to(self, stack):
        while self.m_size > 0:
            stack.push(self.pop())


class ListStack:

    def __init__(self):
        self.stack = []

    def push(self, node):
        self.stack.append(node)

    def pop(self):
        return self.stack.pop(-1) if self.size() > 0 else None

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1] if self.size() > 0 else None

    def clean(self):
        self.stack = []

    def empty(self):
        return self.size() == 0

    def pop_to(self, stack):
        while self.size() > 0:
            stack.push(self.pop())
