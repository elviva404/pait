from typing import Dict

from example.param_verify.flask_example import create_app
from pait.api_doc.markdown import PaitMd
from pait.api_doc.open_api import PaitOpenApi
from pait.app import load_app
from pait.g import config
from pait.model.core import PaitCoreModel

if __name__ == "__main__":
    filename: str = "./example_doc/flask_pait"
    config.init_config(block_http_method_set={"HEAD", "OPTIONS"})
    pait_dict: Dict[str, PaitCoreModel] = load_app(create_app())
    PaitMd(pait_dict, use_html_details=True).output(filename)
    for i in ("json", "yaml"):
        PaitOpenApi(
            pait_dict,
            title="Pait Doc",
            open_api_tag_list=[
                {"name": "test", "description": "test api"},
                {"name": "user", "description": "user api"},
            ],
            type_=i,
        ).output(filename + "_openapi")
