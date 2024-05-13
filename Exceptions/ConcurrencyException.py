class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency issue detected."):
        self.message = message
        super().__init__(self.message)
