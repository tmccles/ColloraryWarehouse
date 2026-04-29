from datetime import datetime
from ProductItem import ProductItem


class Order(ProductItem):
    def __init__(self, order_number, product_number, quantity):
        self.orderNumber= order_number
        self.productNumber= product_number
        self.quantity= quantity
        now= datetime.now()
    
    #return order number
    def getOrderNumber(self):
        return self.orderNumber
    
    #return product number
    def getProductNumber(self):
        return self.productNumber
    
    #return quantity 
    def getQuantity(self):
        return self.quantity