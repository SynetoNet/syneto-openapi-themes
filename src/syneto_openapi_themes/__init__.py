"""
Syneto OpenAPI Themes

Syneto-branded themes and utilities for OpenAPI documentation tools,
built on top of OpenAPIPages.
"""

__version__ = "0.1.0"
__author__ = "Syneto"
__email__ = "dev@syneto.net"

from .brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from .rapidoc import SynetoRapiDoc
from .swagger import SynetoSwaggerUI
from .redoc import SynetoReDoc
from .elements import SynetoElements
from .scalar import SynetoScalar

# FastAPI integration (optional import)
try:
    from .fastapi_integration import (
        add_syneto_rapidoc,
        add_syneto_swagger,
        add_syneto_redoc,
        add_syneto_elements,
        add_syneto_scalar,
        add_all_syneto_docs,
        SynetoDocsManager,
    )
    _fastapi_available = True
except ImportError:
    _fastapi_available = False

__all__ = [
    "SynetoBrandConfig",
    "SynetoColors", 
    "SynetoTheme",
    "SynetoRapiDoc",
    "SynetoSwaggerUI",
    "SynetoReDoc",
    "SynetoElements",
    "SynetoScalar",
]

# Add FastAPI integration to exports if available
if _fastapi_available:
    __all__.extend([
        "add_syneto_rapidoc",
        "add_syneto_swagger", 
        "add_syneto_redoc",
        "add_syneto_elements",
        "add_syneto_scalar",
        "add_all_syneto_docs",
        "SynetoDocsManager",
    ]) 