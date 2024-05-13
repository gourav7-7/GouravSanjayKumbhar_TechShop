class FileIOException(Exception):
    def __init__(self, message="Error occurred during file I/O."):
        self.message = message
        super().__init__(self.message)
