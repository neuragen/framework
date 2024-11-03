"""NeuraGens is a GenAI Framework with expressive, elegant syntax."""

__version__ = "1.0.1-alpha"

from .applications import NeuraGens
from .requests import Request
from .responses import Response

_hard_dependencies = ("parse",)
_missing_dependencies = []

for _dependency in _hard_dependencies:
    try:
        __import__(_dependency)
    except ImportError as _e:
        _missing_dependencies.append(f"{_dependency}: {_e}")

if _missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(_missing_dependencies)
    )
del _hard_dependencies, _dependency, _missing_dependencies

__all__ = ["NeuraGens", "Request", "Response"]

def show_version():
    print(f"NeuraGens version: {__version__}")
