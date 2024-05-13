"""finance-clue에서 발생하는 에러를 정의하는 Module"""

class FinanceClueError(Exception):
    """
    finance-clue 에러 base class
    """

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message


class HttpError(FinanceClueError):
    """
    HTTP 요청이 실패할 때 사용
    """
