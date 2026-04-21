#import math
#import code
from HashTable import HashTable
from ProductItem import ProductItem
from ChainingHashTable import ChainingHashTable
    
#main program
products= ChainingHashTable()
#populates the hash table
products.insert("101", "Iphone 15", "Apple", 100)
products.insert("102", "Samsung Galaxy 24", "Samsung", 120)
products.insert("103", "Macbook Pro", "Apple", 45)
products.insert("123", "HP Laptop", "HP", 87)
products.insert("130", "Apple iWatch Series 7", "Apple", 34)
products.insert("135", "LG Tablet", "Android", 76)
products.insert("140", "Netbook", "Android", 123)
products.insert("145", "Stylus Pen", "Samsung", 32)
products.insert("110", "Apple Pen", "Apple", 65)
products.insert("114", "Samsung Watch", "Samsung", 78)
products.insert("231", "Eastsport", "Backpack", 75)
products.insert("345", "Addidas", "Backpack", 45)
products.insert("564", "Nike Sport", "Backpack", 43)
print("Table has been successfully populated")


#test that an item has been successfully remove from the table
removal= products.remove(110)
if removal== True:
    print("Item was successfully remove from table")
elif removal== False:
    print("Item was not remove from table")

#test the search function of the hash table
products.search(564)

products.updateQuantity(110)

