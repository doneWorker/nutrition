from typing import Optional, Any

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ApiError(BaseModel):
    code: int
    detail: str


class ApiResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[ApiError] = None

    def dict(self, *args, **kwargs):
        exclude_unset = kwargs.get("exclude_unset", False)
        kwargs["exclude_unset"] = exclude_unset or (self.message is None)
        return super().dict(*args, **kwargs)


class APIHttpException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: str,
            headers: Optional[dict] = None,
    ):
        self.status_code = status_code
        self.detail = detail
        self.headers = headers

    def to_response(self):
        return JSONResponse(
            status_code=self.status_code,
            content=ApiResponse(
                success=False,
                error=ApiError(code=self.status_code, message=self.detail),
            ).dict(),
            headers=self.headers,
        )
