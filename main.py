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
print("Product 101 has been added")
products.insert(102, "Samsung Galaxy 24", "Samsung", 120, 1000)
print("Product 102 has been added")
products.insert(103, "Macbook Pro", "Apple", 45, 2000)
print ("Product 103 has been added")
products.insert(123, "HP Laptop", "HP", 87, 200)
print("Product 123 has been added")
products.insert(130, "Apple iWatch Series 7", "Apple", 34, 300)
print("Product 130 has been added")
products.insert(135, "LG Tablet", "Android", 76, 200)
print("Product 135 has been added")
products.insert(140, "Netbook", "Android", 123, 150)
print("Product 140 has been added")
products.insert(145, "Stylus Pen", "Samsung", 32, 100)
print("Product 145 has been added")
products.insert(110, "Apple Pen", "Apple", 65, 125)
print("Product 110 has been added")
products.insert(114, "Samsung Watch", "Samsung", 78, 250)
print("Product 114 has been added")
products.insert(231, "Eastsport", "Backpack", 75, 65)
print("Product 231 has been added")
products.insert(345, "Addidas", "Backpack", 45, 85)
print("Product 345 has been added")
products.insert(564, "Nike Sport", "Backpack", 43, 110)
print("Product 564 has been added")
print("Table has been successfully populated")
print(" ")


#test that an item has been successfully remove from the table
print("Demostrates if product 110 has been successfully removed")
removal= products.remove(110)
if removal== True:
    print("Item was successfully remove from table")
else:
    print("Item was not remove from table")
print(" ")
#test the search function of the hash table
print("Demostrate the search function works")
products.search(564)
print(" ")
#test inventory levels of a product
print("Demostrate the decreaseQuantity works correctly")
products.decreaseQuantity(345, 10)
print(" ")
print("Demostrate restocks works correctly")
products.restock(135,100)
print("  ")
totalNumber= products.totalNumberProduct()
print("The total number of products in inventory: ", totalNumber)
print(" ")
print(" ")

#Place order invoices into the queue
try:
    quantity= 2
    productKey= 564
    queueOrder.enqueueInvoice(1001, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 5
    productKey= 231
    queueOrder.enqueueInvoice(1002, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 10
    productKey= 145
    queueOrder.enqueueInvoice(1003, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 15
    productKey= 135
    queueOrder.enqueueInvoice(1004, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 20
    productKey= 101
    queueOrder.enqueueInvoice(1005, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 7
    productKey= 103
    queueOrder.enqueueInvoice(1006, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 4
    productKey= 130
    queueOrder.enqueueInvoice(1007, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)

    quantity= 8
    productKey= 140
    queueOrder.enqueueInvoice(1008, productKey, quantity)
    products.decreaseQuantity(productKey, quantity)
except KeyNotFoundError as e:
    print("Error: ", e)
except HashTableError as e:
    print("Error: ", e)
#remove order invoices from the queue
removed= queueOrder.dequeueInvoice()
if removed:
    dt= datetime.fromtimestamp(ts)
    formatted= dt.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Remove Order: #{removed.orderNumber}| Product: #{removed.productNumber}| Qty: {removed.quantity}")
    print("Timed Removed: ", formatted)
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
OrderRecieved= datetime(2026, 8, 15)
OrderPlaced= datetime(2026, 8, 5)
ShippingTime= OrderRecieved - OrderPlaced
print("Shipping Time: ", ShippingTime)
SupplyDelay = 4
ReorderDelay = 3
TotalDelay= products.leadTime(SupplyDelay, ReorderDelay)
print("Lead Time: ", TotalDelay)

#Error handling testing is performed
print(" ")
print("Error handling testing")
products.insert(-584, "Addidas", "Backpack", 43, 110)




