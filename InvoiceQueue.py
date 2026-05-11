from datetime import datetime
from ChainingHashTable import ChainingHashTable
from Order import Order
from ProductItem import ProductItem

#Exception handling classes
class InvoiceQueueError(Exception):
    pass
class InvalidQueueSize(InvoiceQueueError):
    pass
class QueueValueError(InvoiceQueueError):
    pass
class QueueOverflowError(InvoiceQueueError):
    pass
class QueueMemoryError(InvoiceQueueError):
    pass
class QueueRuntimeError(InvoiceQueueError):
    pass

#Array- base queue to hold all incoming invoices
class InvoiceQueue(ChainingHashTable):
    def __init__(self, maxLength= -1):
        self.invoiceList= [0]
        self.frontIndex= 0
        self.queueLength= 0
        self.maxLength= maxLength
        self.now= datetime.now()

    #return the length of the queue
    def getQueueLength(self):
        if self.queueLength < 0:
            raise InvalidQueueSize(f"The queue length must be greater than zero")
        return self.queueLength
    
    #Return the maximum length of the invoice queue
    def getQueueMaxLength(self):
        return self.maxLength
    
    #Push a created invoice into the queue
    def enqueueInvoice(self,order_number, product_number, quantity):

        if self.maxLength >= 0 and self.queueLength== self.maxLength:
            print("QUEUE IS FULL, NO ITEM CAN BE ADDED!")
            return False #This mean the queue is full
        #reallocate the size of InvoiceQueue if array is full
        if self.queueLength== len(self.invoiceList):
            self.resizeQueue()
        #new rear index
        self.rearIndex= (self.frontIndex + self.queueLength) % len(self.invoiceList)
        #Push invoice into back of queue
        order= Order(order_number, product_number, quantity)
        self.invoiceList[self.rearIndex]= order
        #setting the time an order is created and placed in the queue
        ts= datetime.now().timestamp()
        dt= datetime.fromtimestamp(ts)
        formatted= dt.strftime("%m/%d/%Y, %H:%M:%S")
        #increase length of queue
        self.queueLength += 1
        print ("Order: ", order_number)
        print("Quantity: ", quantity)
        print("Time: ", formatted)
        print("This order has been placed in the queue")
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
        print("Order has been removed from the queue")
        #Return invoice being removed
        return frontInvoice
    
    #Resize the queue when its reaches maximum length
    def resizeQueue(self):
        if self.invoiceList is None or self.queueLength < 0:
            raise QueueValueError(f"Queue cannot be empty and length cannot be negative")
        if self.queueLength > len(self.invoiceList):
            raise QueueValueError(f"queueLength resize failed because queueLength is greater than invoiceList size")
        if self.maxLength >= 0 and len(self.invoiceList) >= self.maxLength:
            raise QueueOverflowError(f"Queue overflow, the queue is at maximum length")
        #create new invoice queueList and copy existing queue invoices 
        #compute new size
        newQueueSize= len(self.invoiceList) * 2
        if self.maxLength >= 0 and newQueueSize > self.maxLength:
            newQueueSize= self.maxLength
        if newQueueSize <= len(self.invoiceList):
            raise QueueRuntimeError(f"Resize failed new queue size must be greater than invoiceList size")
        #memory reallocation
        try:
            newInvoiceList= [0] * newQueueSize
        except Exception as e:
            raise QueueMemoryError(f"Not enough memory available for reallocation")
        #copy orders to new invoice queue
        try:
            for i in range(self.queueLength):
                invoiceIndex= (self.frontIndex + i) % len(self.invoiceList)
                newInvoiceList[i]= self.invoiceList[invoiceIndex]
        except Exception as e:
            raise QueueRuntimeError(f"Failed to copy invoices to new queue") 
        #Assign new queue list and reset frontIndex back to 0
        self.invoiceList= newInvoiceList
        self.frontIndex= 0
        #reset pointers
        self.rearIndex= self.queueLength - 1 if self.queueLength > 0 else -1