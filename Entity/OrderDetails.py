class OrderDetails:
    def __init__(self, OrderDetailID, Order, Product, Quantity):
        self._OrderDetailID = OrderDetailID
        self._Order = Order
        self._Product = Product
        self._Quantity = Quantity

    
    def setOrderDetailID(self, OrderDetailID):
        self._OrderDetailID = OrderDetailID

    def setOrder(self, Order):
        self._Order = Order

    def setProduct(self, Product):
        self._Product = Product

    def setQuantity(self, Quantity):
        self._Quantity = Quantity

    def setOrderDetailID(self, OrderDetailID):
        self._OrderDetailID = OrderDetailID



    def getOrderDetailID(self):
        return self._OrderDetailID
    
    def setOrder(self, Order):
        return self._Order

    def setProduct(self, Product):
        return self._Product

    def setQuantity(self, Quantity):
        return self._Quantity 

    def setOrderDetailID(self, OrderDetailID):
        return self._OrderDetailID 
    

    
