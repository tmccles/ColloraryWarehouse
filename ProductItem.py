import copy
import math
from HashTable import HashTable
#This class is the node containing the product data
#This is designed for the chaining technique

class ProductItem:
    def __init__(self, ProductKey, ProductName, ProductCategory, ProductQuantity,ItemCost):
        self.Key= ProductKey
        self.Name= ProductName
        self.Category= ProductCategory
        self.Quantity= ProductQuantity
        self.Cost= ItemCost
        self.next= None