from linkedList import SinglyLinkedList

class PriorityNode:
    priority = -1
    value = ''
    def __init__(self, value, priority):
	self.priority = priority
	self.value = value
    def getValue(self):
	return self.value
    def getPriority(self):
	return self.priority

class PriorityQueue:
    list = ''

    def __init__(self):
	self.list = SignglyLinkedList()

    def enqueueWithPriority(self, value, priority):
	idxInsert = 0
	for itr in range(self.list.getSize()):
	    node = self.list.get(itr)
	    if node.getValue() == '': # true when it is tail
		idxInsert = itr
		break
	    if node.getValue().getPrioirity() < priority:
		idxInsert = itr
		break
	    else:
		idxInsert = itr +1
    	self.list.insertAt(PriorityNode(value.priority), idxInsert)

    def dequeueWithPriority(self):
	return self.list.removeAt(0).getValue()	
