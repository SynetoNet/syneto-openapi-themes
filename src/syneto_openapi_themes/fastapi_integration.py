"""
FastAPI integration utilities for Syneto OpenAPI themes.
"""

from typing import Any, Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .brand import SynetoBrandConfig, get_default_brand_config
from .elements import SynetoElements
from .rapidoc import SynetoRapiDoc
from .redoc import SynetoReDoc
from .scalar import SynetoScalar
from .swagger import SynetoSwaggerUI


def add_syneto_rapidoc(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/docs",
    title: Optional[str] = None,
    brand_config: Optional[SynetoBrandConfig] = None,
    header_slot_content: Optional[str] = None,
    **kwargs: Any,
) -> None:
    """
    Add Syneto-branded RapiDoc documentation to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        docs_url: URL where the documentation will be served
        title: Title for the documentation page
        brand_config: Syneto brand configuration
        header_slot_content: HTML content for the custom header slot (overrides brand logo/header)
        **kwargs: Additional RapiDoc configuration options
    """
    if title is None:
        title = f"{app.title} - API Documentation"

    rapidoc = SynetoRapiDoc(
        openapi_url=openapi_url,
        title=title,
        brand_config=brand_config,
        header_slot_content=header_slot_content,
        **kwargs,
    )

    @app.get(docs_url, response_class=HTMLResponse, include_in_schema=False)
    def get_rapidoc_documentation() -> str:
        return rapidoc.render()


def add_syneto_swagger(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/swagger",
    title: Optional[str] = None,
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs: Any,
) -> None:
    """
    Add Syneto-branded SwaggerUI documentation to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        docs_url: URL where the documentation will be served
        title: Title for the documentation page
        brand_config: Syneto brand configuration
        **kwargs: Additional SwaggerUI configuration options
    """
    if title is None:
        title = f"{app.title} - API Documentation"

    swagger = SynetoSwaggerUI(openapi_url=openapi_url, title=title, brand_config=brand_config, **kwargs)

    @app.get(docs_url, response_class=HTMLResponse, include_in_schema=False)
    def get_swagger_documentation() -> str:
        return swagger.render()


def add_syneto_redoc(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/redoc",
    title: Optional[str] = None,
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs: Any,
) -> None:
    """
    Add Syneto-branded ReDoc documentation to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        docs_url: URL where the documentation will be served
        title: Title for the documentation page
        brand_config: Syneto brand configuration
        **kwargs: Additional ReDoc configuration options
    """
    if title is None:
        title = f"{app.title} - API Documentation"

    redoc = SynetoReDoc(openapi_url=openapi_url, title=title, brand_config=brand_config, **kwargs)

    @app.get(docs_url, response_class=HTMLResponse, include_in_schema=False)
    def get_redoc_documentation() -> str:
        return redoc.render()


def add_syneto_elements(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/elements",
    title: Optional[str] = None,
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs: Any,
) -> None:
    """
    Add Syneto-branded Elements documentation to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        docs_url: URL where the documentation will be served
        title: Title for the documentation page
        brand_config: Syneto brand configuration
        **kwargs: Additional Elements configuration options
    """
    if title is None:
        title = f"{app.title} - API Documentation"

    elements = SynetoElements(openapi_url=openapi_url, title=title, brand_config=brand_config, **kwargs)

    @app.get(docs_url, response_class=HTMLResponse, include_in_schema=False)
    def get_elements_documentation() -> str:
        return elements.render()


def add_syneto_scalar(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    docs_url: str = "/scalar",
    title: Optional[str] = None,
    brand_config: Optional[SynetoBrandConfig] = None,
    **kwargs: Any,
) -> None:
    """
    Add Syneto-branded Scalar documentation to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        docs_url: URL where the documentation will be served
        title: Title for the documentation page
        brand_config: Syneto brand configuration
        **kwargs: Additional Scalar configuration options
    """
    if title is None:
        title = f"{app.title} - API Documentation"

    scalar = SynetoScalar(openapi_url=openapi_url, title=title, brand_config=brand_config, **kwargs)

    @app.get(docs_url, response_class=HTMLResponse, include_in_schema=False)
    def get_scalar_documentation() -> str:
        return scalar.render()


def add_all_syneto_docs(
    app: FastAPI,
    *,
    openapi_url: str = "/openapi.json",
    brand_config: Optional[SynetoBrandConfig] = None,
    rapidoc_url: str = "/docs",
    swagger_url: str = "/swagger",
    redoc_url: str = "/redoc",
    elements_url: str = "/elements",
    scalar_url: str = "/scalar",
    **kwargs: Any,
) -> None:
    """
    Add all Syneto-branded documentation tools to a FastAPI app.

    Args:
        app: FastAPI application instance
        openapi_url: URL to the OpenAPI JSON schema
        brand_config: Syneto brand configuration
        rapidoc_url: URL for RapiDoc documentation
        swagger_url: URL for SwaggerUI documentation
        redoc_url: URL for ReDoc documentation
        elements_url: URL for Elements documentation
        scalar_url: URL for Scalar documentation
        **kwargs: Additional configuration options
    """
    add_syneto_rapidoc(app, openapi_url=openapi_url, docs_url=rapidoc_url, brand_config=brand_config, **kwargs)
    add_syneto_swagger(app, openapi_url=openapi_url, docs_url=swagger_url, brand_config=brand_config, **kwargs)
    add_syneto_redoc(app, openapi_url=openapi_url, docs_url=redoc_url, brand_config=brand_config, **kwargs)
    add_syneto_elements(app, openapi_url=openapi_url, docs_url=elements_url, brand_config=brand_config, **kwargs)
    add_syneto_scalar(app, openapi_url=openapi_url, docs_url=scalar_url, brand_config=brand_config, **kwargs)


class SynetoDocsManager:
    """
    Manager class for Syneto documentation tools.

    Provides a convenient way to manage multiple documentation endpoints
    with consistent branding and configuration.
    """

    def __init__(
        self, app: FastAPI, brand_config: Optional[SynetoBrandConfig] = None, openapi_url: str = "/openapi.json"
    ) -> None:
        """
        Initialize the Syneto docs manager.

        Args:
            app: FastAPI application instance
            brand_config: Syneto brand configuration
            openapi_url: URL to the OpenAPI JSON schema
        """
        self.app = app
        self.brand_config = brand_config or get_default_brand_config()
        self.openapi_url = openapi_url
        self._docs_endpoints: dict[str, str] = {}

    def add_rapidoc(self, url: str = "/docs", **kwargs: Any) -> "SynetoDocsManager":
        """Add RapiDoc documentation endpoint."""
        add_syneto_rapidoc(
            self.app, openapi_url=self.openapi_url, docs_url=url, brand_config=self.brand_config, **kwargs
        )
        self._docs_endpoints["rapidoc"] = url
        return self

    def add_swagger(self, url: str = "/swagger", **kwargs: Any) -> "SynetoDocsManager":
        """Add SwaggerUI documentation endpoint."""
        add_syneto_swagger(
            self.app, openapi_url=self.openapi_url, docs_url=url, brand_config=self.brand_config, **kwargs
        )
        self._docs_endpoints["swagger"] = url
        return self

    def add_redoc(self, url: str = "/redoc", **kwargs: Any) -> "SynetoDocsManager":
        """Add ReDoc documentation endpoint."""
        add_syneto_redoc(self.app, openapi_url=self.openapi_url, docs_url=url, brand_config=self.brand_config, **kwargs)
        self._docs_endpoints["redoc"] = url
        return self

    def add_elements(self, url: str = "/elements", **kwargs: Any) -> "SynetoDocsManager":
        """Add Elements documentation endpoint."""
        add_syneto_elements(
            self.app, openapi_url=self.openapi_url, docs_url=url, brand_config=self.brand_config, **kwargs
        )
        self._docs_endpoints["elements"] = url
        return self

    def add_scalar(self, url: str = "/scalar", **kwargs: Any) -> "SynetoDocsManager":
        """Add Scalar documentation endpoint."""
        add_syneto_scalar(
            self.app, openapi_url=self.openapi_url, docs_url=url, brand_config=self.brand_config, **kwargs
        )
        self._docs_endpoints["scalar"] = url
        return self

    def add_all(self, **kwargs: Any) -> "SynetoDocsManager":
        """Add all documentation endpoints."""
        return (
            self.add_rapidoc(**kwargs)
            .add_swagger(**kwargs)
            .add_redoc(**kwargs)
            .add_elements(**kwargs)
            .add_scalar(**kwargs)
        )

    def add_docs_index(self, url: str = "/docs-index") -> "SynetoDocsManager":
        """
        Add a documentation index page that lists all available documentation tools.

        Args:
            url: URL for the documentation index page

        Returns:
            Self for method chaining
        """

        @self.app.get(url, response_class=HTMLResponse, include_in_schema=False)
        def get_docs_index() -> str:
            return self._render_docs_index()

        return self

    def _render_docs_index(self) -> str:
        """Render the documentation index page."""
        endpoints_html = ""
        for tool, url in self._docs_endpoints.items():
            endpoints_html += f"""
            <div class="doc-tool">
                <h3>{tool.title()}</h3>
                <p>View API documentation using {tool.title()}</p>
                <a href="{url}" class="doc-link">Open {tool.title()} →</a>
            </div>
            """

        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{self.app.title} - API Documentation</title>
            <link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">
            <style>
            {self.brand_config.to_css_variables()}

            body {{
                font-family: {self.brand_config.regular_font};
                background-color: {self.brand_config.background_color};
                color: {self.brand_config.text_color};
                margin: 0;
                padding: 2rem;
                line-height: 1.6;
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
            }}

            h1 {{
                color: {self.brand_config.primary_color};
                text-align: center;
                margin-bottom: 2rem;
            }}

            .docs-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 2rem;
            }}

            .doc-tool {{
                background: {self.brand_config.header_color};
                border: 1px solid {self.brand_config.nav_bg_color};
                border-radius: 8px;
                padding: 1.5rem;
                text-align: center;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }}

            .doc-tool:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(173, 15, 108, 0.2);
            }}

            .doc-tool h3 {{
                color: {self.brand_config.primary_color};
                margin-top: 0;
            }}

            .doc-link {{
                display: inline-block;
                background: {self.brand_config.primary_color};
                color: {self.brand_config.text_color};
                text-decoration: none;
                padding: 0.75rem 1.5rem;
                border-radius: 4px;
                margin-top: 1rem;
                transition: background-color 0.2s ease;
            }}

            .doc-link:hover {{
                background: {self.brand_config.nav_accent_color};
            }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{self.app.title} - API Documentation</h1>
                <p style="text-align: center; font-size: 1.1em; margin-bottom: 3rem;">
                    Choose your preferred documentation tool to explore the API
                </p>
                <div class="docs-grid">
                    {endpoints_html}
                </div>
            </div>
        </body>
        </html>
        """

    @property
    def endpoints(self) -> dict[str, str]:
        """Get all registered documentation endpoints."""
        return self._docs_endpoints.copy()
