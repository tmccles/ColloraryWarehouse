import copy
import math
from HashTable import HashTable
#This class is the node containing the product data
#This is designed for the chaining technique

class ProductItem:
    def _init_(self, ProductKey, ProductName, ProductCategory, ProductQuantity):
        self.Key= ProductKey
        self.Name= ProductName
        self.Category= ProductCategory
        self.Quantity= ProductQuantity
        self.next= None