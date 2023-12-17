"""stock-clue에서 발생하는 에러를 정의하는 Module"""

# TODO error 좀 더 명확하게 정의


class StockClueError(Exception):
    """
    stock-clue 에러 base class
    """

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message


class HttpError(StockClueError):
    """
    HTTP 요청이 실패할 때 사용
    """
