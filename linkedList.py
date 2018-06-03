class Node:
    nodeNext = ''
    objValue = ''
    binHead = False
    binTail = False
    def __init__(self, objValue="",nodeNext='',binHead=False,binTail=False):
        self.nodeNext = nodeNext
        self.objValue = objValue
	self.binHead = binHead
	self.binTail = binTail
    def getValue(self):
 	return self.objValue
    def setValue(self, objValue):
	self.objValue = objValue
    def getNext(self):
	return self.nodeNext
    def setNext(self, nodeNext):
  	self.nodeNext = nodeNext
    def isHead(self):
	return self.binHead
    def isTail(self):
	return self.binTail

class SinglyLinkedList:
    nodeHead = ''
    nodeTail = ''
    size = 0
    def __init__(self):
 	self.nodeTail = Node(binTail=True)
	self.nodeHead = Node(binHead=True, nodeNext = self.nodeTail)
    
    def get(self, idxRetrieve):
	nodeReturn = self.nodeHead
 	for itr in range(idxRetrieve +1):
	    nodeReturn = nodeReturn.getNext()
	return nodeReturn

    def insertAt(self, objInsert, IdxInsert):
	nodeNew = Node(objValue=objInsert)
	nodePrev = self.get(IdxInsert -1)
	nodeNext = nodePrev.getNext()
	nodePrev.setNext(nodeNew)
	nodeNew.setNext(nodeNext)
	self.size = self.size +1

    def removeAt(self, idxRemove):
	nodePrev = self.get(idxRemove -1)
	nodeNext = self.get(idxRemove +1)
	nodePrev.setNext(nodeNext)
	self.size -=1

    def printStatus(self):
	nodeCurrent = self.nodeHead
	while nodeCurrent.getNext().isTail() == False:
	    nodeCurrent = nodeCurrent.getNext()
	    print nodeCurrent.getValue(),
	print

    def getSize(self):
	return self.size
