import glob
import importlib
import ast
from pathlib import Path

from summer.inversion_of_control.constants import (
    ALL_FILES_PATH,
    PYTHON_EXTENSION,
)


def get_executable_parent_path(executable_path: str) -> str:
    return str(Path(executable_path).parent.absolute())


def get_module_name_from_absolute_path(filename: str) -> str:
    return Path(filename).stem


def has_service_decorator(filename: str) -> bool:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())
    except (SyntaxError, UnicodeDecodeError):
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == "service":
                    return True
                if (
                    isinstance(decorator, ast.Call)
                    and isinstance(decorator.func, ast.Name)
                    and decorator.func.id == "service"
                ):
                    return True
    return False


def discover_services(executable_parent_path: str) -> None:
    """
    Discovers recursively all services that match with termination and execute them in order to save them to
    services dict.
    """
    for filename in glob.iglob(
        executable_parent_path + f"{ALL_FILES_PATH}{PYTHON_EXTENSION}", recursive=True
    ):
        if has_service_decorator(filename):
            module_name: str = get_module_name_from_absolute_path(filename)
            spec = importlib.util.spec_from_file_location(module_name, filename)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
