import glob
import importlib
from pathlib import Path
from typing import NoReturn

from summer.inversion_of_control.constants import (
    ALL_FILES_PATH,
    PYTHON_EXTENSION,
    NEW_LINE_LITERAL,
    SERVICE_DECORATOR_LITERAL,
)


def get_executable_parent_path(executable_path: str) -> str:
    return str(Path(executable_path).parent.absolute())


def get_module_name_from_absolute_path(filename: str) -> str:
    return filename.split("/")[-1].split(".")[0]


def discover_services(executable_parent_path: str) -> NoReturn:
    """
    Discovers recursively all services that match with termination and execute them in order to save them to
    services dict.
    """
    for filename in glob.iglob(executable_parent_path + f"{ALL_FILES_PATH}{PYTHON_EXTENSION}", recursive=True):
        if f"{NEW_LINE_LITERAL}{SERVICE_DECORATOR_LITERAL}" in open(filename).read():
            module_name: str = get_module_name_from_absolute_path(filename)
            spec = importlib.util.spec_from_file_location(module_name, filename)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
