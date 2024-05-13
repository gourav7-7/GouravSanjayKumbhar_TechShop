class InsufficientStockException(Exception):
    def __init__(self, message="Insufficient stock to fulfill the order."):
        self.message = message
        super().__init__(self.message)
