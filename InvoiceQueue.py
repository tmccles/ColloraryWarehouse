#Array- base queue to hold all incoming invoices
class InvoiceQueue:
    def __init__(self, max_length= -1):
        self.invoiceList= [0]
        self.frontIndex= 0
        self.queueLength= 0
        self.max_length= max_length

    #return the length of the queue
    