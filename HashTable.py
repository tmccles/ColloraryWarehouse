#Base class for Hash table

class HashTable:
    
    #Returns a hash code for a specific key
    #abs will ensure that the hash code is non-negative
    def HashKey(self, key):
        return abs(hash(key))
    
    #Insert the key/pair into the hash table, if the key already exist the product 
    #number of copies should be incremented by one
    def insert(self, key, value):
        pass
    
    #Search the bash table for a specific key/pair
    #Return product if found
    #Return None if it is not found
    def search(self, key):
        pass

    #Remove a specific key/pair from the hash table 
    def remove(self, key):
        pass


