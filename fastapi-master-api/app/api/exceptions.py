from app.service.authorization import NotAuthorizedError
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette import status


def _format(body: dict) -> dict:
    if body.get("entity"):
        body["entity"] = body["entity"].upper()
    return body


class HTTP404Exception(HTTPException):
    def __init__(self, message="Item not found"):
        self.message = message
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=self.message)


class HTTP409Exception(HTTPException):
    def __init__(self, message="Item already exists"):
        self.message = message
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=self.message)


def not_authorized_handler(error: NotAuthorizedError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=_format({"type": error.type}),
    )
