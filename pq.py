import unittest

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
        return "The first item entered in this list is " + str(self.peek()) + ". There are " + str(len(self.storage)) + " items in this list."

    def insert(self, val, priority):
        to_insert = Item(val, priority)

        insert_index = 0
        while insert_index < len(self.storage):
            if self.storage[insert_index] == to_insert or self.storage[insert_index] < to_insert:
                break
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

#Handling duplicate priority now
# class DuplicatePriorityException(Exception):
#     '''Raised when there are duplicate priority values'''

#     def __init__(self, expression, message='Duplicate priority values'):
#         self.expression = expression
#         self.message = message
#         super().__init__(self.message)
    
#     def __str__(self):
#         return f'{self.expression} -> {self.message}'

class Test(unittest.TestCase):
    def testSimple(self):
        pq = PriorityQueue()
        pq.insert("c", 3)
        pq.insert("a", 1)
        pq.insert("b", 2)
        pq.insert("c", 1)
        pq.insert("3", 2)
        pq.insert("GEORGE", 1)

        assert(pq.pop() == "a")
        assert(pq.pop() == "c")
        assert(pq.pop() == "GEORGE")
        assert(pq.pop() == "b")
        assert(pq.pop() == "3")
        assert(pq.pop() == "c")
        print("Simple test passed!")

    def testEmpty(self):
        with self.assertRaises(EmptyQueueException):
            pq = PriorityQueue()
            pq.pop()
        print("Empty queue test passed!")
    
    def testFloatsAndNegatives(self):
        pq = PriorityQueue()
        pq.insert("c", 1)
        pq.insert("e", 1.01)
        pq.insert("first", -1)

        assert(pq.pop() == "first")
        assert(pq.pop() == "c")
        assert(pq.pop() == "e")
        print("Float test passed!")


if __name__ == "__main__":
    unittest.main()
