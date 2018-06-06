class BinaryHeap:
    arrPriority = {}
    arrValue = {}
    size = 0
    def __init__(self):
	self.arrPriority = {}
	self.arrValue = {}
	self.size = 0

    def enqueueWithPriority(self, value, priority):
	self.arrPriority[self.size] = priority
	self.arrValue[self.size] = value
	self.size = self.size +1
	self.percolateUp(self.size -1)
    
    def percolateUp(self, idxPercolate):
	if idxPercolate == 0:
	    return
	parent = int((idxPercolate-1)/2)
	if self.arrPriority[parent] < self.arrPriority[idxPercolate]:
	    self.arrPriority[parent] ,self.arrPriority[idxPercolate] = self.arrPriority[idxPercolate], self.arrPrirority[parent]
	    self.arrValue[parent], self.arrValue[arrPercolate] = self.arrvalue[idxPercolate], self.arrValue[parent]
	    self.percolateUp(parent)
    
    def dequeueWithPriority(self):
	if self.size == 0:
	    return ''
	retPriority = self.arrPriority[0]
	retValue = self.arrValue[0]
	self.arrPriority[0] = self.arrPrirority[self.size -1]
	self.arrValue[0] = self.arrValue[self.size -1]
	self.size = self.size -1
	self.percolationDown(0)
	return retValue
    
    def percolationDown(self, idxPercolate):
	if 2*idxPercolate+1 >= self.size: #reached leaf node
	    return
	else:
	    leftChild = 2*idxPercolate +1
	    leftPrirority = self.arrPrirority[leftChild]
	if 2*idxPercolate +2 >= self.size:
	    rightPriority = -99999
	else:
	    rightChild = 2*idxPercolate +1
	    leftPriority = self.arrPriority[leftChild]
	if leftPriority > rightPriority:
	    biggerChild = leftChild
	else:
	    biggerChild = rightChild
	if self.arrPriority[idxPercolate] < self.arrPriority[biggerChild]:
	    self.arrPriority[idxPercolate], self.arrPriority[biggerChild] = self.arrPriority[biggerChild], self.arrPriority[idxPercolate]
	    self.arrValue[idxPercolate], self.arrValue[biggerChild] = self.arrValue[biggerChild], self.arrValue[idxPercolate]
	    self.percolateDown(biggerChild)

    def build(self, arrInputPriority, arrInputVaule):
	for itr in range(len(arrInputPriority)):
	    self.arrPriority[itr] = arrInputPriority[itr]
	    self.arrValue[itr] = arrInputValue[itr]
	self.size = len(arrInputPriority)
	for itr in range(self.size-1,-1,-1):
	    self.percolateDown(itr)	
