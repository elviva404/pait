# pait Technical Documentation

**Last updated:** 2022-01-21\
_Document generation aided by **Documatic**_

<SHORT PROJECT DESCRIPTION>

* [Introduction](#introduction)
* [Code Overview](#code-overview)

## Introduction

This is a technical document detailing
        at a high-level
        what pait does, how it operates,
        and how it is built.

The outline of this document was generated
        by **Documatic**.
<!---Documatic-section-group: arch-start--->


## Project Architecture


<!---Documatic-section-group: arch-end--->

<!---Documatic-section-group: helloworld-start--->


## Code Overview

The codebase has a 4-deep folder structure, with 111 in total.
<!---Documatic-section-helloworld: setup-start--->
The codebase is compatible with Python 3.6 and above, because of f-string 3.6 in /Users/elikemOZE/Codelab/Documatic/OS_projects/pait/example/param_verify/starlette_example.py.
Install requirements with `pip install -r requirements.txt`.

Run `pip install -e .` in top-level directory to install
package in local directory.
Install from pypi with `pip install pait`.



<!---Documatic-section-helloworld: setup-end--->

<!---Documatic-section-helloworld: entrypoints-start--->


## Entrypoints

There are 0 source code entrypoints in top-level `__main__`/`__init__` files.


<!---Documatic-section-helloworld: entrypoints-end--->

<!---Documatic-section-helloworld: classes-start--->
The project has classes which are used in multiple functions:

* `pait.typing.Any` is a base class. It is used 10 times.
* `pait.typing.Callable` is a base class. It is used 5 times.
* `pait.typing.Type` is a base class. It is used 3 times.


<!---Documatic-section-helloworld: classes-end--->

<!---Documatic-section-group: concept-start--->
## Concepts
<!---Documatic-section-group: concept-end--->

<!---Documatic-section-group: helloworld-end--->

<!---Documatic-section-group: dev-start--->


## Developers
<!---Documatic-section-dev: setup-start--->
* Install developer requirements with `pip install -r requirements-dev.txt`
* This project uses `pre-commit` to enforce code style on commit. Run `pre-commit install` in a terminal to setup
* Tests are present in `tests/` (using pytest, unittest)




<!---Documatic-section-dev: setup-end--->

<!---Documatic-section-dev: ci-start--->
No CI/CD config files were detected.


<!---Documatic-section-dev: ci-end--->

<!---Documatic-section-group: dev-end--->

### **pait/**

#### example/

No files in `example/` import local package files.

### param_verify/

<!---Documatic-section-file: example/param_verify/starlette_example.py--->

#### starlette_example.py


File has 532 lines added and 284 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: example/param_verify/tornado_example.py--->

#### tornado_example.py


File has 444 lines added and 261 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: example/param_verify/model.py--->

#### model.py


File has 88 lines added and 45 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: example/param_verify/flask_example.py--->

#### flask_example.py


File has 401 lines added and 223 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: example/param_verify/sanic_example.py--->

#### sanic_example.py


File has 464 lines added and 275 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### tests/

No files in `tests/` import local package files.

### test_app/

<!---Documatic-section-file: tests/test_app/test_helper.py--->

#### test_helper.py


File has 106 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_app/test_sanic.py--->

#### test_sanic.py


File has 371 lines added and 302 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_app/test_tornado.py--->

#### test_tornado.py


File has 346 lines added and 310 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_app/test_starlette.py--->

#### test_starlette.py


File has 404 lines added and 323 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_app/test_flask.py--->

#### test_flask.py


File has 354 lines added and 244 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_app/test_app.py--->

#### test_app.py


File has 19 lines added and 4 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_model.py--->

### test_model.py


File has 85 lines added and 2 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/conftest.py--->

### conftest.py


File has 68 lines added and 40 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: tests/test_core.py--->

### test_core.py


File has 57 lines added and 59 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### pait/

No files in `pait/` import local package files.

### app/

#### flask/

##### plugin/

<!---Documatic-section-file: pait/app/flask/plugin/mock_response.py--->

###### mock_response.py


File has 53 lines added and 22 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/flask/plugin/check_json_resp.py--->

###### check_json_resp.py


File has 13 lines added and 10 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/flask/_route.py--->

##### _route.py


File has 26 lines added and 11 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/flask/_test_helper.py--->

##### _test_helper.py


File has 20 lines added and 9 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/flask/_pait.py--->

##### _pait.py


File has 42 lines added and 92 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### starlette/

##### plugin/

<!---Documatic-section-file: pait/app/starlette/plugin/auto_complete_json_resp.py--->

###### auto_complete_json_resp.py


File has 55 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/starlette/plugin/mock_response.py--->

###### mock_response.py


File has 95 lines added and 27 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/starlette/plugin/check_json_resp.py--->

###### check_json_resp.py


File has 61 lines added and 15 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/starlette/_route.py--->

##### _route.py


File has 36 lines added and 18 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/starlette/_test_helper.py--->

##### _test_helper.py


File has 20 lines added and 9 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/starlette/_pait.py--->

##### _pait.py


File has 48 lines added and 95 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### tornado/

##### plugin/

<!---Documatic-section-file: pait/app/tornado/plugin/auto_complete_json_resp.py--->

###### auto_complete_json_resp.py


File has 25 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/tornado/plugin/mock_response.py--->

###### mock_response.py


File has 63 lines added and 25 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/tornado/plugin/check_json_resp.py--->

###### check_json_resp.py


File has 52 lines added and 20 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/tornado/_route.py--->

##### _route.py


File has 30 lines added and 15 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/tornado/_test_helper.py--->

##### _test_helper.py


File has 20 lines added and 9 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/tornado/_pait.py--->

##### _pait.py


File has 36 lines added and 83 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### sanic/

##### plugin/

<!---Documatic-section-file: pait/app/sanic/plugin/auto_complete_json_resp.py--->

###### auto_complete_json_resp.py


File has 40 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/sanic/plugin/mock_response.py--->

###### mock_response.py


File has 65 lines added and 21 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/sanic/plugin/check_json_resp.py--->

###### check_json_resp.py


File has 48 lines added and 11 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/sanic/_route.py--->

##### _route.py


File has 25 lines added and 11 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/sanic/_test_helper.py--->

##### _test_helper.py


File has 20 lines added and 9 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/sanic/_pait.py--->

##### _pait.py


File has 53 lines added and 101 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


#### base/

<!---Documatic-section-file: pait/app/base/test_helper.py--->

##### test_helper.py


File has 303 lines added and 8 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/app/base/app_helper.py--->

##### app_helper.py


File has 80 lines added and 2 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


### util/

<!---Documatic-section-file: pait/util/_types.py--->

#### _types.py


File has 63 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/util/_gen_tip.py--->

#### _gen_tip.py


File has 63 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/util/_i18n.py--->

#### _i18n.py


File has 115 lines added and 1 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/util/_pydantic_util.py--->

#### _pydantic_util.py


File has 124 lines added and 9 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/util/_util.py--->

#### _util.py


File has 191 lines added and 139 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


### plugin/

<!---Documatic-section-file: pait/plugin/auto_complete_json_resp.py--->

#### auto_complete_json_resp.py


File has 51 lines added and 1 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/plugin/required.py--->

#### required.py


File has 44 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/plugin/at_most_one_of.py--->

#### at_most_one_of.py


File has 40 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/plugin/base_mock_response.py--->

#### base_mock_response.py


File has 101 lines added and 37 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/plugin/check_json_resp.py--->

#### check_json_resp.py


File has 113 lines added and 47 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/plugin/base.py--->

#### base.py


File has 109 lines added and 40 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


### model/

<!---Documatic-section-file: pait/model/config.py--->

#### config.py


File has 25 lines added and 39 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/model/core.py--->

#### core.py


File has 98 lines added and 74 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/model/response.py--->

#### response.py


File has 90 lines added and 24 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/model/links.py--->

#### links.py


File has 91 lines added and 0 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/model/tag.py--->

#### tag.py


File has 23 lines added and 1 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


### api_doc/

<!---Documatic-section-file: pait/api_doc/base_parse.py--->

#### base_parse.py


File has 54 lines added and 28 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/api_doc/open_api.py--->

#### open_api.py


File has 323 lines added and 188 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/api_doc/markdown.py--->

#### markdown.py


File has 257 lines added and 226 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/field.py--->

### field.py


File has 57 lines added and 12 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/core.py--->

### core.py


File has 453 lines added and 311 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/param_handle.py--->

### param_handle.py


File has 284 lines added and 243 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.


<!---Documatic-section-file: pait/exceptions.py--->

### exceptions.py


File has 29 lines added and 8 lines removed
                in the past 4 weeks. so1n <qaz6803609@163.com> is the inferred code owner.
