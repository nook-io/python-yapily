"""API response object."""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field, StrictInt, StrictStr


class ApiResponse:
    """
    API response object
    """

    status_code: Annotated[StrictInt | None, Field(description='HTTP status code')] = None
    headers: Annotated[dict[StrictStr, StrictStr] | None, Field(description='HTTP headers')] = None
    data: Annotated[Any | None, Field(description='Deserialized data given the data type')] = None
    raw_data: Annotated[Any | None, Field(description='Raw data (HTTP response body)')] = None

    def __init__(self, status_code=None, headers=None, data=None, raw_data=None) -> None:
        self.status_code = status_code
        self.headers = headers
        self.data = data
        self.raw_data = raw_data
