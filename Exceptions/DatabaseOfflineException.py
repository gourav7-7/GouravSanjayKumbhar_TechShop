class DatabaseOfflineException(Exception):
    def __init__(self, message="Database is offline."):
        self.message = message
        super().__init__(self.message)
