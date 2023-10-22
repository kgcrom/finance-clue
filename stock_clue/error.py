class StockClueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)
        self.message = message


class HttpError(StockClueError):
    pass
