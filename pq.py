class Item:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __repr__(self):
        return "Item(val: {}, pri: {})".format(self.val,
                                               self.priority)


class PriorityQueue:

    def __init__(self):
        self.storage = []

    def __str__(self):
        return "[" + ", ".join([str(item) for item in self.storage]) + "]"

    def insert(self, val, priority):
        to_insert = Item(val, priority)

        insert_index = 0
        while insert_index < len(self.storage):
            if self.storage[insert_index] < to_insert:
                break
            
            if self.storage[insert_index] == to_insert:
                raise  DuplicatePriorityException(to_insert)

            insert_index += 1

        self.storage.insert(insert_index, to_insert)

    def peek(self):
        if self.storage == []:
            raise EmptyQueueException(self.storage)
        return self.storage[-1].val
        
    def pop(self):
        if self.storage == []:
            raise EmptyQueueException(self.storage)
        return self.storage.pop().val

class EmptyQueueException(Exception):
    '''Raised when storage is empty'''

    def __init__(self, expression, message='Storage is empty'):
        self.expression = expression
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.expression} -> {self.message}'

class DuplicatePriorityException(Exception):
    '''Raised when there are duplicate priority values'''

    def __init__(self, expression, message='Duplicate priority values'):
        self.expression = expression
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.expression} -> {self.message}'

def simple_test():
    print("Running simple test...")
    pq = PriorityQueue()
    pq.insert("c", 3)
    pq.insert("a", 1)
    pq.insert("b", 2)

    assert(pq.pop() == "a")
    assert(pq.pop() == "b")
    assert(pq.pop() == "c")
    print("Simple test passed!")


if __name__ == "__main__":
    simple_test()
