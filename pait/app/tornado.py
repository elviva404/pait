import logging
import json
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Type

from tornado.httputil import RequestStartLine
from tornado.web import Application

from pait.app.base import BaseAppHelper
from pait.core import pait as _pait
from pait.g import pait_data
from pait.model import PaitResponseModel, PaitStatus


class AppHelper(BaseAppHelper):
    RequestType = RequestStartLine
    FormType = dict
    FileType = dict
    HeaderType = dict

    def __init__(self, class_: Any, args: Tuple[Any, ...], kwargs: Mapping[str, Any]):
        super().__init__(class_, args, kwargs)
        self.request = self.cbv_class.request
        self._path_kwargs = self.cbv_class.path_kwargs

    def body(self) -> dict:
        return json.loads(self.request.body.decode())

    def cookie(self) -> dict:
        return self.request.cookies

    def file(self) -> dict:
        return self.request.files

    def form(self) -> dict:
        return self.request.body_arguments

    def header(self) -> dict:
        return self.request.headers

    def path(self) -> dict:
        return self._path_kwargs

    def query(self) -> dict:
        return {key: value[0].decode() for key, value in self.request.query_arguments.items()}


def load_app(app: Application) -> None:
    """Read data from the route that has been registered to `pait`"""
    for rule in app.wildcard_router.rules:
        path: str = rule.matcher.regex.pattern
        base_name: str = rule.target.__name__
        for method in ["get", "post", "head", "options", "delete", "put", "trace", "patch"]:
            try:
                handler: Callable = getattr(rule.target, method, None)
            except TypeError:
                continue
            route_name: str = f"{base_name}.{method}"
            pait_id: Optional[str] = getattr(handler, "_pait_id", None)
            if not pait_id:
                continue
            pait_data.add_route_info(pait_id, path, {method}, route_name)


def pait(
    author: Optional[Tuple[str]] = None,
    desc: Optional[str] = None,
    status: Optional[PaitStatus] = None,
    group: str = "root",
    tag: Optional[Tuple[str, ...]] = None,
    response_model_list: List[Type[PaitResponseModel]] = None,
) -> Callable:
    """Help starlette provide parameter checks and type conversions for each routing function/cbv class"""
    return _pait(
        AppHelper,
        author=author,
        desc=desc,
        status=status,
        group=group,
        tag=tag,
        response_model_list=response_model_list,
    )
