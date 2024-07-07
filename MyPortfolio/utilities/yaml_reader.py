from typing import Any

import yaml


def read_yaml(file: str) -> Any:
    with open(file=file, mode="r", encoding="utf-8") as stream:
        try:
            content: Any = yaml.safe_load(stream=stream)
        except yaml.YAMLError as error:
            print(error)

    return content