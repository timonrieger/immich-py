from typing import Literal, Optional, Union

from pydantic import BaseModel

MaybeBaseModel = Optional[Union[BaseModel, list[BaseModel], str]]
FormatMode = Literal["pretty", "json", "table"]
PrintType = Literal["info", "warning", "error", "debug", "success", "json", "text"]


class ClientConfig(BaseModel):
    """
    A configuration for a client to connect to an Immich server.
    """

    base_url: Optional[str]
    api_key: Optional[str]
    access_token: Optional[str]
