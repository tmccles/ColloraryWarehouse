import copy
import math
from HashTable import HashTable
from ProductItem import ProductItem

#This hash table uses the chaining technique
#The initial capacity will be set to 1,000

class ChainingHashTable(HashTable):
    def __init__(self):
        self.initialCapacity= 1000
        self.table= [None] *self.initialCapacity
        

    def _len_(self):
        return len(self.table)
    
    #Insert a new product into the hash table
    #Check for duplicate, if found increase product quantity by one
    #Return True if product is appended or quantity updated
    def insert (self, key, name, category, quantity, cost):
        #Calculates the hash key for the bucket index
        bucket_index= self.HashKey(key) % len(self.table)

        #traverse the linked list if the product already exist, do not append the
        #product simply increment the quantity
        item= self.table[bucket_index] 
        previous= None
        while item !=None:
            if key== item.Key:
                item.Quantity += quantity
                return True
            previous= item
            item= item.next
            
        #if it is not a duplicate key append new key to linked list
        if self.table[bucket_index]==None:
            self.table[bucket_index]= ProductItem(key, name, category, quantity, cost)
        else:
            previous.next= ProductItem(key,name,category,quantity, cost)
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
                
                item.next= None #garbage collection
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
                print("Cost: ", item.Cost)
                return item
            item= item.next
        return None #product not found
    #Search and return the name of the product 
    def searchByName(self, key):
        #calculate hash key to start search
        bucket_index= self.HashKey(key) % len(self.table)
        item= self.table[bucket_index]
        while item != None:
            if key== item.Key:
                print("Product: ", item.Name)
                print("Category: ", item.Category)
                print("Cost: ", item.Cost)
                return item
            item= item.next
        return None
    #Update product quantity amount, when a product is remove from inventory
    def decreaseQuantity(self, key, quantityRemove):
        #calculate hash key
        bucket_index= self.HashKey(key)% len(self.table)
        item= self.table[bucket_index]
        while item != None:
            if key== item.Key and item.Quantity != 0:
                #ERROR HANDLING: Removing more products than what is available
                if item.Quantity < quantityRemove:
                    print(" ")
                    print("ERROR: TRYING TO REMOVE TOO MANY ITEMS")
                    print("CURRENTLY AVAILABLE: ", item.Quantity)
                    return False
                
                item.Quantity-= quantityRemove
                #Show new product quantity after update perform
                print(" ")
                print("Product: ", item.Name)
                print("Product Quantity: ", item.Quantity)
                return True
            item= item.next
        print(" ")    
        print("ERROR: PRODUCT NOT FOUND")
        return False
    
     #Increase product quantity amount, when a product is being restock
    def restock(self, key, quantityIncrease):
        #calculate hash key
        bucket_index= self.HashKey(key)% len(self.table)
        item= self.table[bucket_index]
        while item != None:
            if key== item.Key:     
                print(" ")
                print("CURRENTLY AVAILABLE: ", item.Quantity)
                
                item.Quantity+= quantityIncrease
                #Show new product quantity after update perform
                print(" ")
                print("Updated stock amount")
                print("Product: ", item.Name)
                print("Product Quantity: ", item.Quantity)
                return True
            item= item.next
        print(" ")    
        print("ERROR: PRODUCT NOT FOUND")
        return False
    
    #Returns the total amount of products in hashtable
    def totalNumberProduct(self):
        count= 0
        for bucket in self.table:
            item= bucket
            #Tranverse thru buckets in the linked list
            while item != None:
                count += 1
                item= item.next
        return count 
    
    #Data Analysis Functions
    #These functions will help the company to analyze the cost of sitting inventory
    #calculates the average inventory to analyze inventory's stock trends and carrying
    #costs
    def averageInventory(self, beginningInventory, endingInventory):
        average= (beginningInventory + endingInventory)/2
        return average
    
    #calculates the cost of goods sold
    def costOfGoods(self, beginningInventory, purchaseAmount, endingInventory):
        COGS= beginningInventory + purchaseAmount - endingInventory
        return COGS
    
    #calculates days inventory is sitting in the warehouse
    def daysOfInventory(self, average, cogs):
        days= average/cogs
        return days
    
    #calculates total inventory value
    def inventoryValue(self, Begin, NetPurchase, cogs):
        ending= Begin + NetPurchase - cogs
        return ending
    
    #calculates total inventory holding sum
    def holdingSum(self, capitalCost, storageCost, serviceCost, riskCost):
        total= capitalCost + storageCost + serviceCost + riskCost
        return total
    
    #calculates the total shipping cost
    def shippingCost(self, baseRate, packingMaterial, labor, handlingFees):
        totalShipping= baseRate + packingMaterial + labor + handlingFees
        return totalShipping
    
    #calculates the lead time for products
    def leadTime(self, supplyDelay, reorderDelay):
        totalLeadTime= supplyDelay + reorderDelay
        return totalLeadTime