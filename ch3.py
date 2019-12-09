'''
#insert 
x = ['a','b','d','e','f']
idxInsert = 2
valInsert = 'c'

y = list(range(6))
for itr in range(0, idxInsert):
    y[itr] = x[itr]
y[idxInsert] = valInsert
for itr in range(idxInsert, len(x)):
    y[itr+1] = x[itr]

print(x)
print(y)


#delete
x = ['a','b','c','d','e','f']
idxDelete = 2

y = list(range(5))
for itr in range(0, idxDelete):
    y[itr] = x[itr]
for itr in range(idxDelete+1, len(x)):
    y[itr-1] = x[itr]

x=y
print(x)
'''
#STACK
from folder import SinglyLinkedList

class Stack(object) : 
    lstInstance = SinglyLinkedList()
    def pop(self):
        return self.lstInstance.removeAt(0)
    def push(self, value):
        self.lstInstance.insertAt(value,0)

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")

print stack.pop()
print stack.pop()
print stack.pop()

#QUEUE
from folder import SinglyLinkedList

class Queue(object) :
    lstInstance = SinglyLinkedList()
    def dequeue(self) :
        return self.lstInstance.removeAt(0)
    def enqueue(self, value) :
        self.lstInstance.insertAt(value,self.lstInstance.getSize())

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print queue.dequeue()
print queue.dequeue()
print queue.dequeue()