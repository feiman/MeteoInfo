"""
``numeric.lib`` is mostly a space for implementing functions that don't
belong in core or in another numeric submodule with a clear purpose
"""

from .shape_base import *
from .index_tricks import *

__all__ = []
__all__ += shape_base.__all__
__all__ += index_tricks.__all__