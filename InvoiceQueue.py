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
        if self.queueLength== self.maxLength:
            return False #This mean the queue is full
        #reallocate the size of InvoiceQueue
        if self.queueLength== len(self.invoiceList):
            self.resize()
            #Push invoice into back of queue
            invoiceIndex= (self.frontIndex- self.queueLength) % len(self.invoiceList)
            self.invoiceList[invoiceIndex]= invoice
            self.queueLength += 1
            return True
    
    #Remove an invoice from the queue
    def dequeueInvoice(self):
        #Pop invoice from the front of the queue
        frontInvoice= self.invoiceList[self.frontIndex]
        #Decrease the frontIndex and queueLength by 1
        self.frontIndex= (self.frontIndex + 1) % len(self.invoiceList)
        #Return invoice being removed
        return frontIndex