class Orders:
    def __init__(self, OrderID, customerID, OrderDate):
        self._OrderID = OrderID
        self._customerID = customerID
        self._OrderDate = OrderDate
        self._total_amount = 0  

    # Getter and setter methods for each attribute
    

    def set_order_id(self, OrderID):
        self._OrderID = OrderID

    def setOrderDate(self, OrderDate):
        self._OrderDate = OrderDate

    def setCustomerID(self, CustomerID):
        self._CustomerID= CustomerID

    def setTotalAmount(self,TotAmount):
        self._total_amount = TotAmount

    

    def getOrderID(self):
        return self._OrderID

    def getCustomer(self):
        return self._customer
    
    def getOrderDate(self):
        return self._OrderID
    
    def getTotalAmount(self):
        return self._total_amount


    