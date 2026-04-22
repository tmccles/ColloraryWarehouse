#import math
#import code
from HashTable import HashTable
from ProductItem import ProductItem
from ChainingHashTable import ChainingHashTable
    
#main program
products= ChainingHashTable()
#populates the hash table
products.insert(101, "Iphone 15", "Apple", 100,1000)
products.insert(102, "Samsung Galaxy 24", "Samsung", 120, 1000)
products.insert(103, "Macbook Pro", "Apple", 45, 2000)
products.insert(123, "HP Laptop", "HP", 87, 200)
products.insert(130, "Apple iWatch Series 7", "Apple", 34, 300)
products.insert(135, "LG Tablet", "Android", 76, 200)
products.insert(140, "Netbook", "Android", 123, 150)
products.insert(145, "Stylus Pen", "Samsung", 32, 100)
products.insert(110, "Apple Pen", "Apple", 65, 125)
products.insert(114, "Samsung Watch", "Samsung", 78, 250)
products.insert(231, "Eastsport", "Backpack", 75, 65)
products.insert(345, "Addidas", "Backpack", 45, 85)
products.insert(564, "Nike Sport", "Backpack", 43, 110)
print("Table has been successfully populated")


#test that an item has been successfully remove from the table
removal= products.remove(110)
if removal== True:
    print("Item was successfully remove from table")
else:
    print("Item was not remove from table")

#test the search function of the hash table
products.search(564)
#test inventory levels of a product
products.decreaseQuantity(345, 10)
products.restock(135,100)
print("  ")
totalNumber= products.totalNumberProduct()
print("The total number of products in inventory: ", totalNumber)

