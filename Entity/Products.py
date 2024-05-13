class Products:
    def __init__(self, ProductID, ProductName, Description, Price):
        self._ProductID = ProductID
        self._ProductName = ProductName
        self._Description = Description
        self._Price = Price

    # Getter and setter methods for each attribute
    def getProductID(self):
        return self._ProductID

    def setProductID(self, ProductID):
        self._ProductID = ProductID

    def getProductName(self):
        return self._ProductName

    def setProductName(self, ProductName):
        self._ProductName = ProductName

    def getDescription(self):
        return self._Description

    def setDescription(self, Description):
        self._Description = Description

    def getPrice(self):
        return self._Price

    def setPrice(self, Price):
        self._Price = Price

    
   