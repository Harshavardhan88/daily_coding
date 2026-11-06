# a queue built out of two stacks
# new items go into inbox, old ones come out of outbox.
# when outbox is empty we flip inbox over into it, which
# puts the oldest item on top

class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            return None
        return self.outbox.pop()

    def peek(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            return None
        return self.outbox[-1]

    def is_empty(self):
        return not self.inbox and not self.outbox


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.peek())     # 2
q.enqueue(4)
print(q.dequeue())  # 2
print(q.dequeue())  # 3
print(q.dequeue())  # 4
print(q.is_empty())  # True
print(q.dequeue())  # None
