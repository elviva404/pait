from typing import List, Tuple, Type

from pait.model import PaitResponseModel, PaitStatus


class Config(object):
    def __init__(self) -> None:
        self.author: Tuple[str, ...] = ("",)
        self.status: PaitStatus = PaitStatus.undefined
        self.default_response_model_list: List[Type[PaitResponseModel]] = []
