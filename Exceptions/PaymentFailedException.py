class PaymentFailedException(Exception):
    def __init__(self, message="Payment for the order failed."):
        self.message = message
        super().__init__(self.message)
