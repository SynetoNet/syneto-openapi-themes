"""
Syneto-branded RapiDoc implementation.
"""

from typing import Any, Optional

from openapipages import RapiDoc

from .brand import SynetoBrandConfig, get_default_brand_config


class SynetoRapiDoc(RapiDoc):
    """
    Syneto-branded RapiDoc documentation generator.

    Extends OpenAPIPages RapiDoc with Syneto theming and branding.
    """

    def __init__(
        self,
        openapi_url: str = "/openapi.json",
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoRapiDoc.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            **kwargs: Additional RapiDoc configuration options
        """
        self.brand_config = brand_config or get_default_brand_config()

        # Store RapiDoc-specific configuration for use in rendering
        self.rapidoc_config = {
            "theme": self.brand_config.theme.value,
            "bg_color": self.brand_config.background_color,
            "text_color": self.brand_config.text_color,
            "header_color": self.brand_config.header_color,
            "primary_color": self.brand_config.primary_color,
            "nav_bg_color": self.brand_config.nav_bg_color,
            "nav_text_color": self.brand_config.nav_text_color,
            "nav_hover_bg_color": self.brand_config.nav_hover_bg_color,
            "nav_hover_text_color": self.brand_config.nav_hover_text_color,
            "nav_accent_color": self.brand_config.nav_accent_color,
            "nav_accent_text_color": self.brand_config.nav_accent_text_color,
            "regular_font": self.brand_config.regular_font,
            "mono_font": self.brand_config.mono_font,
            "logo": self.brand_config.logo_url,
            "render_style": "read",
            "schema_style": "table",
            "default_schema_tab": "schema",
            "response_area_height": "400px",
            "show_info": "true",
            "allow_authentication": "true",
            "allow_server_selection": "true",
            "allow_api_list_style_selection": "true",
            "show_header": "true",
            "show_components": "true",
            "update_route": "true",
            "route_prefix": "#",
            "sort_tags": "true",
            "goto_path": "",
            "fill_request_fields_with_example": "true",
            "persist_auth": "false",
            **kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": kwargs.get("js_url", "https://unpkg.com/rapidoc/dist/rapidoc-min.js"),
            "head_js_urls": kwargs.get("head_js_urls", []),
            "tail_js_urls": kwargs.get("tail_js_urls", []),
            "head_css_urls": kwargs.get("head_css_urls", []),
            "favicon_url": kwargs.get("favicon_url", self.brand_config.favicon_url),
        }

        super().__init__(**valid_parent_params)

    def render(self, **kwargs: Any) -> str:
        """
        Render the Syneto-branded RapiDoc HTML.

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
        Inject Syneto-specific customizations into the HTML.

        Args:
            html: Base HTML from OpenAPIPages

        Returns:
            HTML with Syneto customizations
        """
        # Add Syneto CSS variables and custom styles
        custom_styles = f"""
        <style>
        {self.brand_config.to_css_variables()}
        {self.brand_config.get_loading_css()}

        /* Syneto-specific RapiDoc customizations */
        rapi-doc {{
            --green: {self.brand_config.primary_color};
            --blue: {self.brand_config.primary_color};
            --orange: {self.brand_config.primary_color};
            --red: var(--syneto-accent-red, #f01932);
        }}

        /* Custom scrollbar styling */
        rapi-doc::-webkit-scrollbar {{
            width: 8px;
        }}

        rapi-doc::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}

        rapi-doc::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        rapi-doc::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        /* Loading state styling */
        .syneto-rapidoc-container {{
            position: relative;
            min-height: 100vh;
        }}

        .syneto-rapidoc-loading {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 9999;
            background: {self.brand_config.background_color};
        }}

        /* Error state styling */
        .syneto-rapidoc-error {{
            padding: 2rem;
            text-align: center;
            background: {self.brand_config.background_color};
            color: {self.brand_config.text_color};
            font-family: {self.brand_config.regular_font};
        }}
        </style>
        """

        # Add custom JavaScript for enhanced functionality
        custom_scripts = """
        <script>
        (function() {
            // Enhanced loading and error handling
            const rapidocElement = document.querySelector('rapi-doc');
            const container = document.querySelector('.syneto-rapidoc-container');

            if (rapidocElement && container) {
                // Show loading state
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-rapidoc-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                container.appendChild(loadingDiv);

                // Handle load completion
                rapidocElement.addEventListener('spec-loaded', function() {
                    setTimeout(() => {
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                    }, 500);
                });

                // Handle load errors
                rapidocElement.addEventListener('spec-load-error', function(e) {
                    if (loadingDiv.parentNode) {
                        loadingDiv.innerHTML = `
                            <div class="syneto-error">
                                <h3>Failed to Load API Documentation</h3>
                                <p>Unable to load the OpenAPI specification.</p>
                                <p>Please check the URL and try again.</p>
                                <p><small>Error: ${e.detail || 'Unknown error'}</small></p>
                            </div>
                        `;
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

    def get_authentication_config(self) -> dict[str, Any]:
        """
        Get authentication configuration for RapiDoc.

        Returns:
            Dictionary with authentication settings
        """
        return {
            "allow_authentication": True,
            "persist_auth": False,
            "api_key_name": "X-API-Key",
            "api_key_location": "header",
            "jwt_header_name": "Authorization",
            "jwt_token_prefix": "Bearer ",
        }

    def with_jwt_auth(self, jwt_url: str = "/auth/token") -> "SynetoRapiDoc":
        """
        Configure JWT authentication.

        Args:
            jwt_url: URL for JWT token endpoint

        Returns:
            Self for method chaining
        """
        self.rapidoc_config.update(
            {
                "allow_authentication": "true",
                "persist_auth": "true",
            }
        )
        return self

    def with_api_key_auth(self, api_key_name: str = "X-API-Key") -> "SynetoRapiDoc":
        """
        Configure API key authentication.

        Args:
            api_key_name: Name of the API key header

        Returns:
            Self for method chaining
        """
        self.rapidoc_config.update(
            {
                "allow_authentication": "true",
                "api_key_name": api_key_name,
            }
        )
        return self
