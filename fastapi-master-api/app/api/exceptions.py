from fastapi import HTTPException
from starlette import status


class HTTP403Exception(HTTPException):
    def __init__(self, message="You are not allowed to access this operation."):
        self.message = message
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=self.message)


class HTTP404Exception(HTTPException):
    def __init__(self, message="Item not found"):
        self.message = message
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=self.message)
