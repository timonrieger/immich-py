from typing import Union
from multidict import CIMultiDictProxy

HeadersType = Union[dict[str, str], CIMultiDictProxy[str]]
