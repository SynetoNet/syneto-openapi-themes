"""
Syneto-branded SwaggerUI implementation.
"""

from typing import Any, Optional

from openapipages import SwaggerUI

from .brand import SynetoBrandConfig, get_default_brand_config


class SynetoSwaggerUI(SwaggerUI):
    """
    Syneto-branded SwaggerUI documentation generator.

    Extends OpenAPIPages SwaggerUI with Syneto theming and branding.
    """

    def __init__(
        self,
        openapi_url: str = "/openapi.json",
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoSwaggerUI.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            **kwargs: Additional SwaggerUI configuration options
        """
        self.brand_config = brand_config or get_default_brand_config()

        # Store SwaggerUI-specific configuration for use in rendering
        self.swagger_config = {
            "deepLinking": True,
            "displayOperationId": False,
            "defaultModelsExpandDepth": 1,
            "defaultModelExpandDepth": 1,
            "defaultModelRendering": "example",
            "displayRequestDuration": True,
            "docExpansion": "list",
            "filter": True,
            "showExtensions": True,
            "showCommonExtensions": True,
            "tryItOutEnabled": True,
            **kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": kwargs.get("js_url", "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"),
            "head_js_urls": kwargs.get("head_js_urls", []),
            "tail_js_urls": kwargs.get("tail_js_urls", []),
            "head_css_urls": kwargs.get("head_css_urls", []),
            "favicon_url": kwargs.get("favicon_url", self.brand_config.favicon_url),
            "css_url": kwargs.get("css_url", "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css"),
            "oauth2_redirect_url": kwargs.get("oauth2_redirect_url", "/docs/oauth2-redirect"),
            "init_oauth": kwargs.get("init_oauth"),
            "swagger_ui_parameters": kwargs.get("swagger_ui_parameters", self.swagger_config),
            "swagger_ui_presets": kwargs.get("swagger_ui_presets"),
        }

        super().__init__(**valid_parent_params)

    def render(self, **kwargs: Any) -> str:
        """
        Render the Syneto-branded SwaggerUI HTML.

        Args:
            **kwargs: Additional template variables

        Returns:
            Complete HTML string for the documentation page
        """
        # Get base HTML from OpenAPIPages
        base_html = super().render(**kwargs)

        # Inject Syneto customizations
        return self._inject_syneto_customizations(base_html)

    def _inject_syneto_customizations(self, html: str) -> str:
        """
        Inject Syneto-specific customizations into the SwaggerUI HTML.

        Args:
            html: Base HTML from OpenAPIPages

        Returns:
            HTML with Syneto customizations
        """
        # Add Syneto CSS customizations
        custom_styles = f"""
        <style>
        {self.brand_config.to_css_variables()}
        {self.brand_config.get_loading_css()}

        /* Syneto SwaggerUI Theme */
        .swagger-ui .topbar {{
            background-color: {self.brand_config.nav_bg_color};
            border-bottom: 2px solid {self.brand_config.primary_color};
        }}

        .swagger-ui .topbar .download-url-wrapper .select-label {{
            color: {self.brand_config.nav_text_color};
        }}

        .swagger-ui .info .title {{
            color: {self.brand_config.primary_color};
            font-family: {self.brand_config.regular_font};
        }}

        .swagger-ui .scheme-container {{
            background: {self.brand_config.header_color};
            border: 1px solid {self.brand_config.nav_bg_color};
        }}

        .swagger-ui .opblock.opblock-post {{
            border-color: {self.brand_config.primary_color};
            background: rgba(173, 15, 108, 0.1);
        }}

        .swagger-ui .opblock.opblock-post .opblock-summary-method {{
            background: {self.brand_config.primary_color};
        }}

        .swagger-ui .opblock.opblock-get {{
            border-color: {self.brand_config.primary_color};
            background: rgba(173, 15, 108, 0.05);
        }}

        .swagger-ui .opblock.opblock-get .opblock-summary-method {{
            background: {self.brand_config.primary_color};
        }}

        .swagger-ui .opblock.opblock-put {{
            border-color: {self.brand_config.primary_color};
            background: rgba(173, 15, 108, 0.05);
        }}

        .swagger-ui .opblock.opblock-put .opblock-summary-method {{
            background: {self.brand_config.primary_color};
        }}

        .swagger-ui .opblock.opblock-delete {{
            border-color: #f01932;
            background: rgba(240, 25, 50, 0.1);
        }}

        .swagger-ui .opblock.opblock-delete .opblock-summary-method {{
            background: #f01932;
        }}

        .swagger-ui .btn.authorize {{
            background-color: {self.brand_config.primary_color};
            border-color: {self.brand_config.primary_color};
        }}

        .swagger-ui .btn.authorize:hover {{
            background-color: {self.brand_config.nav_accent_color};
            border-color: {self.brand_config.nav_accent_color};
        }}

        .swagger-ui .btn.execute {{
            background-color: {self.brand_config.primary_color};
            border-color: {self.brand_config.primary_color};
        }}

        .swagger-ui .btn.execute:hover {{
            background-color: {self.brand_config.nav_accent_color};
            border-color: {self.brand_config.nav_accent_color};
        }}

        /* Custom scrollbar */
        .swagger-ui ::-webkit-scrollbar {{
            width: 8px;
        }}

        .swagger-ui ::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}

        .swagger-ui ::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .swagger-ui ::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        /* Loading and error states */
        .syneto-swagger-container {{
            position: relative;
            min-height: 100vh;
        }}

        .syneto-swagger-loading {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 9999;
            background: {self.brand_config.background_color};
        }}
        </style>
        """

        # Add custom JavaScript
        custom_scripts = """
        <script>
        (function() {
            // Enhanced SwaggerUI initialization
            console.log('Syneto SwaggerUI Theme loaded');

            // Add loading state management
            const swaggerContainer = document.querySelector('#swagger-ui');
            if (swaggerContainer) {
                // Show loading state
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-swagger-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                swaggerContainer.appendChild(loadingDiv);

                // Enhanced error handling
                window.addEventListener('error', function(e) {
                    if (e.message && e.message.includes('swagger')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.innerHTML = `
                                <div class="syneto-error">
                                    <h3>Failed to Load API Documentation</h3>
                                    <p>Unable to load the SwaggerUI interface.</p>
                                    <p>Please check the OpenAPI specification and try again.</p>
                                </div>
                            `;
                        }
                    }
                });

                // Set a timeout for loading
                setTimeout(() => {
                    if (loadingDiv.parentNode && loadingDiv.textContent.includes('Loading')) {
                        loadingDiv.innerHTML = `
                            <div class="syneto-error">
                                <h3>Loading Timeout</h3>
                                <p>The API documentation is taking longer than expected to load.</p>
                                <p>Please refresh the page or check your connection.</p>
                            </div>
                        `;
                    }
                }, 10000);

                // Remove loading state when SwaggerUI is ready
                const checkSwaggerReady = setInterval(() => {
                    if (document.querySelector('.swagger-ui')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                        clearInterval(checkSwaggerReady);
                    }
                }, 100);
            }
        })();
        </script>
        """

        # Inject styles and scripts into the HTML
        if "<head>" in html:
            html = html.replace("<head>", f"<head>{custom_styles}")
        else:
            html = f"{custom_styles}{html}"

        if "</body>" in html:
            html = html.replace("</body>", f"{custom_scripts}</body>")
        else:
            html = f"{html}{custom_scripts}"

        return html

    def get_oauth_config(self) -> dict[str, Any]:
        """
        Get OAuth2 configuration for SwaggerUI.

        Returns:
            Dictionary with OAuth2 settings
        """
        return {
            "clientId": "syneto-api-client",
            "realm": "syneto",
            "appName": "Syneto API Documentation",
            "scopeSeparator": " ",
            "scopes": ["read", "write"],
            "additionalQueryStringParams": {},
            "useBasicAuthenticationWithAccessCodeGrant": False,
        }

    def with_oauth2(
        self,
        client_id: str,
        realm: str = "syneto",
        scopes: Optional[list[str]] = None,
    ) -> "SynetoSwaggerUI":
        """
        Configure OAuth2 authentication.

        Args:
            client_id: OAuth2 client ID
            realm: OAuth2 realm
            scopes: List of OAuth2 scopes

        Returns:
            Self for method chaining
        """
        oauth_config = {
            "clientId": client_id,
            "realm": realm,
            "scopes": scopes or ["read", "write"],
        }
        self.swagger_config.update({"initOAuth": oauth_config})
        return self

    def with_api_key_auth(self, api_key_name: str = "X-API-Key") -> "SynetoSwaggerUI":
        """
        Configure API key authentication.

        Args:
            api_key_name: Name of the API key header

        Returns:
            Self for method chaining
        """
        # API key auth is typically handled via OpenAPI spec
        # This method can be used to set UI preferences
        self.swagger_config.update(
            {
                "persistAuthorization": True,
                "tryItOutEnabled": True,
            }
        )
        return self
