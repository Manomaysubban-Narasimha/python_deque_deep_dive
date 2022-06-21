'''
Author: Manomay Subban Narasimha
Goal: Implement a deque (double-ended queue) using doubly linked list to
simulate how Python has internally implemented the deque data structure that
belongs to the collections module.
'''

class deque:

    def __init__(self):
        self.dLL = DoublyLinkedList()
        

    def append(self, val):
        '''
            Adds a new element to the end of the deque
            Constant time operation.
        '''
        self.dLL.append(val)


    def pop(self):
        '''
            Removes and returns the last element from the deque
            Constant time operation.
        '''
        return self.dLL.remove_tail()


    def popleft(self):
        '''
            Removes and returns the left-most element of the deque.
            Constant time operation.
        '''
        return self.dLL.remove_head()


    def prepend(self, val):
        '''
            Adds the element with the given value to the front of the deque.
            Constant time operation.
        '''
        self.dLL.prepend(val)

    def __str__(self):
        '''
            Prints all of the elements of the deque.
            Linear time operation.
        '''
        return "deque(" + self.dLL.__str__() + ")"       
        


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

        def __init__(self):
            self.head = None
            self.tail= None
            

        def __str__(self):
            '''
                Prints the values of the nodes of this Doubly LinkedList.
                Takes linear time.
            '''
            temp = self.head
            string = "["
            while temp:
                string += str(temp.val)
                if temp.next:
                    string += ", "
                temp = temp.next

            string += "]"
            return string
        
                
        def append(self, val):
            '''
            Adds the node with the given value to the end of the Doubly LL.
            Takes constant time since there is access to the last node
            '''
            to_append = Node(val)
            if self.tail is None:
                self.tail = self.head = to_append
            else:
                self.tail.next = to_append
                to_append.prev = self.tail
                self.tail = self.tail.next
                

        def prepend(self, val):
            '''
                Adds the node with the given value to the head of the list.
                Takes constant time
            '''
            to_prepend = Node(val)
            if self.head is None:
                self.head = self.tail = to_prepend
            else:
                to_prepend.next = self.head
                self.head.prev = to_prepend
                self.head = self.head.prev


        def remove_head(self):
            '''
                Removes and returns the node at the head of the doubly LL
                Takes constant time
            '''
            temp = self.head
            # condition for empty LL
            if temp is None:
                return temp
            # for single-node LL
            if temp == self.tail:
                self.head = self.tail = None
                # return temp
            else:
                self.head = self.head.next
                temp.next = None
                self.head.prev = None
            return temp


        def remove_tail(self):
            '''
                Removes and returns the node from the tail of the doubly LL
                Takes constant time.
            '''
            if self.tail is None:
                return self.tail
            if self.head == self.tail:
                temp = self.head
                self.head = self.tail = None
                return temp
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            return temp
        

stack = deque()
queue = deque()

# Push elements in stack
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

# Pop element from stack
stack.pop()
print(stack)

# Enqueue element in queue
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)

# Dequeue element from queue
queue.popleft()
print(queue)
