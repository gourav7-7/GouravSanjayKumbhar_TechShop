class Inventory:
    def __init__(self, InventoryID, Product, QuantityInStock):
        self._InventoryID = InventoryID
        self._Product = Product
        self._QuantityInStock = QuantityInStock

    # Getter and setter methods for each attribute

    def setInventoryID(self, InventoryID):
        self._InventoryID = InventoryID

    def setProduct(self,Product):
        self._Product = Product

    def setQuantityInStock(self, QuantityInStock):
        self._QuantityInStock = QuantityInStock



    def getInventoryID(self):
        return self._InventoryID
    
    def getProduct(self,Product):
        return self._Product

    def getQuantityInStock(self, QuantityInStock):
        return self._QuantityInStock

    


   