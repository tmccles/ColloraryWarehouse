#Array- base queue to hold all incoming invoices
class InvoiceQueue:
    def __init__(self, maxLength= -1):
        self.invoiceList= [0]
        self.frontIndex= 0
        self.queueLength= 0
        self.maxLength= maxLength

    #return the length of the queue
    def getQueueLength(self):
        return self.queueLength
    
    #Return the maximum length of the invoice queue
    def getQueueMaxLength(self):
        return self.maxLength
    
    #Push a created invoice into the queue
    def enqueueInvoice(self, invoice):
        if self.maxLength >= 0 and self.queueLength== self.maxLength:
            print("QUEUE IS FULL, NO ITEM CAN BE ADDED!")
            return False #This mean the queue is full
        #reallocate the size of InvoiceQueue if array is full
        if self.queueLength== len(self.invoiceList):
            self.resizeQueue()
        #new rear index
        self.rearIndex= (self.frontIndex + self.queueLength) % len(self.invoiceList)
        #Push invoice into back of queue
        self.invoiceList[self.rearIndex]= invoice
        #increase length of queue
        self.queueLength += 1
        return True
    
    #Remove an invoice from the queue
    def dequeueInvoice(self):
        if self.queueLength== 0:
            print("CANNOT REMOVE ITEM THE QUEUE IS EMPTY!")
            return None
        #Pop invoice from the front of the queue
        frontInvoice= self.invoiceList[self.frontIndex]
        #Decrease the frontIndex and queueLength by 1
        self.frontIndex= (self.frontIndex + 1) % len(self.invoiceList)
        self.queueLength -= 1
        #Reset pointers once the queue is empty
        if self.queueLength== 0:
            self.frontIndex= 0
            self.rearIndex= -1
        #Return invoice being removed
        return frontInvoice
    
    #Resize the queue when its reaches maximum length
    def resizeQueue(self):
        #create new invoice queueList and copy existing queue invoices 
        newQueueSize= len(self.invoiceList) * 2
        if self.maxLength >= 0 and newQueueSize > self.maxLength:
            newQueueSize= self.maxLength
        newInvoiceList= [0] * newQueueSize
        for i in range(self.queueLength):
            invoiceIndex= (self.frontIndex + i) % len(self.invoiceList)
            newInvoiceList[i]= self.invoiceList[invoiceIndex]
        #Assign new queue list and reset frontIndex back to 0
        self.invoiceList= newInvoiceList
        self.frontIndex= 0
        #reset pointers
        self.rearIndex= self.queueLength - 1 if self.queueLength > 0 else -1