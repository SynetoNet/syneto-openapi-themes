"""
Syneto OpenAPI Themes

Syneto-branded themes and utilities for OpenAPI documentation tools,
built on top of OpenAPIPages.
"""

__version__ = "0.1.0"
__author__ = "Syneto"
__email__ = "dev@syneto.net"

from .brand import (
    SYNETO_LOGO_SVG,
    SynetoBrandConfig,
    SynetoColors,
    SynetoTheme,
    get_brand_config_with_custom_logo,
    get_brand_config_with_svg_logo,
    get_default_brand_config,
    get_light_brand_config,
    svg_to_data_uri,
)
from .elements import SynetoElements
from .rapidoc import SynetoRapiDoc
from .redoc import SynetoReDoc
from .scalar import SynetoScalar
from .swagger import SynetoSwaggerUI

# FastAPI integration (optional import)
try:
    from .fastapi_integration import (
        SynetoDocsManager,
        add_all_syneto_docs,
        add_syneto_elements,
        add_syneto_rapidoc,
        add_syneto_redoc,
        add_syneto_scalar,
        add_syneto_swagger,
    )

    _fastapi_available = True
except ImportError:
    # Define dummy variables to avoid F401 errors
    SynetoDocsManager = None  # type: ignore
    add_all_syneto_docs = None  # type: ignore
    add_syneto_elements = None  # type: ignore
    add_syneto_rapidoc = None  # type: ignore
    add_syneto_redoc = None  # type: ignore
    add_syneto_scalar = None  # type: ignore
    add_syneto_swagger = None  # type: ignore
    _fastapi_available = False

__all__ = [
    "SynetoBrandConfig",
    "SynetoColors",
    "SynetoTheme",
    "SYNETO_LOGO_SVG",
    "get_default_brand_config",
    "get_light_brand_config",
    "get_brand_config_with_custom_logo",
    "get_brand_config_with_svg_logo",
    "svg_to_data_uri",
    "SynetoRapiDoc",
    "SynetoSwaggerUI",
    "SynetoReDoc",
    "SynetoElements",
    "SynetoScalar",
]

# Add FastAPI integration to exports if available
if _fastapi_available:
    __all__.extend(
        [
            "add_syneto_rapidoc",
            "add_syneto_swagger",
            "add_syneto_redoc",
            "add_syneto_elements",
            "add_syneto_scalar",
            "add_all_syneto_docs",
            "SynetoDocsManager",
        ]
    )
