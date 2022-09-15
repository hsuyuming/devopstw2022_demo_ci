"""
demo code
"""
# read version from installed package
from importlib.metadata import version

__version__ = version("fastapi_demo")

print(__version__)
