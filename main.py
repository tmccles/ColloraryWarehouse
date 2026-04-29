#import math
#import code
from HashTable import HashTable
from ProductItem import ProductItem
from ChainingHashTable import ChainingHashTable
from datetime import datetime
from InvoiceQueue import InvoiceQueue
from Order import Order
    
#main program
products= ChainingHashTable()
queueOrder= InvoiceQueue()
ts= datetime.now().timestamp()
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
print(" ")
print(" ")
print("Cost Analysis of Sitting Inventory")

#Place order invoices into the queue
queueOrder.enqueueInvoice(1001, 564, 2)
queueOrder.enqueueInvoice(1002, 231, 5)
queueOrder.enqueueInvoice(1003, 145, 10)
queueOrder.enqueueInvoice(1004, 135, 15)
queueOrder.enqueueInvoice(1005, 101, 20)
queueOrder.enqueueInvoice(1006, 103, 7)
queueOrder.enqueueInvoice(1007, 130, 4)
queueOrder.enqueueInvoice(1008, 140, 8)

#remove order invoices from the queue
removed= queueOrder.dequeueInvoice()
if removed:
    print(f"Remove Order: #{removed.orderNumber}| Product: #{removed.productNumber}| Qty: {removed.quantity}")
    print("Timed Removed: #", ts)
print(" ")
print(" ")

#Data Analysis Hash Table Features:
print("DATA ANALYSIS OF INVENTORY")
Beginning= 10000
Ending= 3000
Average= products.averageInventory(Beginning, Ending)
print("The cost of average inventory: $", Average)

PurchaseAmount= 5000
Goods= products.costOfGoods(Beginning, PurchaseAmount, Ending)
print("Cost of Goods Sold: $", Goods)

Days= products.daysOfInventory(Average, Goods)
print("Days of Inventory: ", Days * 365)

InventoryTurnover= Goods/Average
print("Inventory Turnover: ", InventoryTurnover, "%")
print(" ")
print(" ")

print("Inventory Storage Cost Analysis")
capitalCost= 5000
storageCost= 1500
serviceCost= 2000
riskCost= 1000
netPurchase= PurchaseAmount
totalInventoryValue= products.inventoryValue(Beginning, netPurchase,Goods)
print("Total Inventory Value: ", totalInventoryValue)

totalInventoryHoldingSum= products.holdingSum(capitalCost, storageCost, serviceCost, riskCost)
print("Total Inventory Holding Sum: ", totalInventoryHoldingSum)

InventoryHoldingCost= (totalInventoryHoldingSum/ totalInventoryValue) * 100
print("Total Hold Cost Percentage: %", InventoryHoldingCost)
print(" ")
print(" ")
print("Shipping Cost Analysis")
print(" ")
OrderRecieved= date(2026, 8, 15)
OrderPlaced= date(2026, 8, 5)
ShippingTime= OrderRecieved - OrderPlaced
print("Shipping Time: ", ShippingTime)
SupplyDelay = 4
ReorderDelay = 3
TotalDelay= products.leadTime(SupplyDelay, ReorderDelay)
print("Lead Time: ", TotalDelay)



