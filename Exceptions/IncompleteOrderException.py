class IncompleteOrderException(Exception):
    def __init__(self, message="Order detail lacks a product reference."):
        self.message = message
        super().__init__(self.message)
