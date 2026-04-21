import copy
import math
from HashTable import HashTable
from ProductItem import ProductItem
#This hash table uses the chaining technique
#The initial capacity will be set to 1,000

class ChainingHashTable(HashTable):
    def _init_(self):
        self.initialCapacity= 1000
        self.table= [None] *self.initialCapacity
        item= ProductItem()

    def _len_(self):
        return len(self.table)
    
    #Insert a new product into the hash table
    #Check for duplicate, if found increase product quantity by one
    #Return True if product is appended or quantity updated
    def insert (self, key, name, category, quantity):
        #Calculates the hash key for the bucket index
        bucket_index= self.HashKey(key) % len(self.table)

        #traverse the linked list if the product already exist, do not append the
        #product simply increment the quantity
        item= self.table[bucket_index] 
        previous= None
        while item !=None:
            if key== item.Key:
                item.Quantity= item.Quantity +1
            return True
            previous= item
            item= item.next
            
        #if it is not a duplicate key append new key to linked list
        if self.table[bucket_index]==None:
            self.table[bucket_index]= item(key, name,category,quantity)
        else:
            previous.next= item(key,name,category,quantity)
        return True
    
    #Remove an item from the hash table
    #Traverse the linked list to find key/product pair
    def remove(self, key):
        #get bucket index to start traversing the linked list
        bucket_index= self.HashKey(key) % len(self.table)
        item= self.table[bucket_index]
        previous= None
        while item != None:
            if key== item.Key:
                if previous== None:
                    self.table[bucket_index]= item.next
                else:
                    previous.next= item.next
                return True
            previous= item
            item= item.next
        return False #key was not located in linked list

    #Find a specific key and print product information
    def search(self, key):
        #calculate hash key to start search
        bucket_index= self.HashKey(key) % len(self.table)
        item= self.table[bucket_index]
        while item != None:
            if key== item.Key:
                print("Product: ", item.Name)
                print("Category: ", item.Category)
                print("Quantity: ", item.Quantity)
                return item.Key
            item= item.next
        return None #product not found
    
    #Update product quantity amount, when a product is remove from inventory
    def updateQuantity(self, key, quantityRemove):
        #calculate hash key
        bucket_index= self.HashKey(key)% len(self.table)
        item= self.table[bucket_index]
        while item != None:
            if key== item.Key and item.Quantity != 0:
                #ERROR HANDLING: Removing more products than what is available
                if item.Key < quantityRemove:
                    print("ERROR: TRYING TO REMOVE TOO MANY ITEMS")
                    print("CURRENTLY AVAILABLE: ", item.Quantity)
                else:
                    item.Quantity= item.Quantity- quantityRemove
            #Show new product quantity after update perform
            print("Product Quantity: ", item.Quantity)
         

