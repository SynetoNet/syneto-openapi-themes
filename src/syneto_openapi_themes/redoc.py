"""
Syneto-branded ReDoc implementation.
"""

from typing import Any, Optional

from openapipages import ReDoc

from .brand import SynetoBrandConfig, get_default_brand_config


class SynetoReDoc(ReDoc):
    """
    Syneto-branded ReDoc documentation generator.

    Extends OpenAPIPages ReDoc with Syneto theming and branding.
    """

    def __init__(
        self,
        openapi_url: str = "/openapi.json",
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoReDoc.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            **kwargs: Additional ReDoc configuration options
        """
        self.brand_config = brand_config or get_default_brand_config()

        # Store ReDoc-specific configuration for use in rendering
        self.redoc_config = {
            "scrollYOffset": 0,
            "hideDownloadButton": False,
            "disableSearch": False,
            "hideLoading": False,
            "nativeScrollbars": False,
            "theme": {
                "colors": {
                    "primary": {
                        "main": self.brand_config.primary_color,
                    },
                    "text": {
                        "primary": self.brand_config.text_color,
                    },
                    "background": {
                        "main": self.brand_config.background_color,
                    },
                },
                "typography": {
                    "fontSize": "14px",
                    "lineHeight": "1.5em",
                    "code": {
                        "fontSize": "13px",
                        "fontFamily": self.brand_config.mono_font,
                    },
                    "headings": {
                        "fontFamily": self.brand_config.regular_font,
                        "fontWeight": "600",
                    },
                },
                "sidebar": {
                    "backgroundColor": self.brand_config.nav_bg_color,
                    "textColor": self.brand_config.nav_text_color,
                },
                "rightPanel": {
                    "backgroundColor": self.brand_config.header_color,
                },
            },
            **kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": kwargs.get("js_url", "https://cdn.jsdelivr.net/npm/redoc@2/bundles/redoc.standalone.js"),
            "head_js_urls": kwargs.get("head_js_urls", []),
            "tail_js_urls": kwargs.get("tail_js_urls", []),
            "head_css_urls": kwargs.get("head_css_urls", []),
            "favicon_url": kwargs.get("favicon_url", self.brand_config.favicon_url),
            "with_google_fonts": kwargs.get("with_google_fonts", True),
            "ui_parameters": kwargs.get("ui_parameters", self.redoc_config),
        }

        super().__init__(**valid_parent_params)

    def render(self, **kwargs: Any) -> str:
        """
        Render the Syneto-branded ReDoc HTML.

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
        Inject Syneto-specific customizations into the ReDoc HTML.

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

        /* Syneto ReDoc Theme */
        .redoc-wrap {{
            font-family: {self.brand_config.regular_font};
        }}

        .menu-content {{
            background-color: {self.brand_config.nav_bg_color} !important;
            color: {self.brand_config.nav_text_color} !important;
        }}

        .menu-content .menu-item {{
            color: {self.brand_config.nav_text_color} !important;
        }}

        .menu-content .menu-item:hover {{
            background-color: {self.brand_config.nav_hover_bg_color} !important;
            color: {self.brand_config.nav_hover_text_color} !important;
        }}

        .menu-content .menu-item.active {{
            background-color: {self.brand_config.nav_accent_color} !important;
            color: {self.brand_config.nav_accent_text_color} !important;
        }}

        .api-content {{
            background-color: {self.brand_config.background_color} !important;
            color: {self.brand_config.text_color} !important;
        }}

        .api-info h1 {{
            color: {self.brand_config.primary_color} !important;
            font-family: {self.brand_config.regular_font} !important;
        }}

        .operation-type.post {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .operation-type.get {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .operation-type.put {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .operation-type.delete {{
            background-color: #f01932 !important;
        }}

        .http-verb.post {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .http-verb.get {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .http-verb.put {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .http-verb.delete {{
            background-color: #f01932 !important;
        }}

        /* Custom scrollbar styling */
        .menu-content::-webkit-scrollbar {{
            width: 8px;
        }}

        .menu-content::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}

        .menu-content::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .menu-content::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        .api-content::-webkit-scrollbar {{
            width: 8px;
        }}

        .api-content::-webkit-scrollbar-track {{
            background: {self.brand_config.background_color};
        }}

        .api-content::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .api-content::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        /* Loading and error states */
        .syneto-redoc-container {{
            position: relative;
            min-height: 100vh;
        }}

        .syneto-redoc-loading {{
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
            // Enhanced ReDoc initialization
            console.log('Syneto ReDoc Theme loaded');

            // Add loading state management
            const redocContainer = document.querySelector('#redoc-container');
            if (redocContainer) {
                // Show loading state
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-redoc-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                redocContainer.appendChild(loadingDiv);

                // Enhanced error handling
                window.addEventListener('error', function(e) {
                    if (e.message && e.message.includes('redoc')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.innerHTML = `
                                <div class="syneto-error">
                                    <h3>Failed to Load API Documentation</h3>
                                    <p>Unable to load the ReDoc interface.</p>
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

                // Remove loading state when ReDoc is ready
                const checkRedocReady = setInterval(() => {
                    if (document.querySelector('.redoc-wrap')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                        clearInterval(checkRedocReady);
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

    def get_theme_config(self) -> dict[str, Any]:
        """
        Get theme configuration for ReDoc.

        Returns:
            Dictionary with theme settings
        """
        return {
            "colors": {
                "primary": {
                    "main": self.brand_config.primary_color,
                },
                "text": {
                    "primary": self.brand_config.text_color,
                },
                "background": {
                    "main": self.brand_config.background_color,
                },
            },
            "typography": {
                "fontSize": "14px",
                "lineHeight": "1.5em",
                "code": {
                    "fontSize": "13px",
                    "fontFamily": self.brand_config.mono_font,
                },
                "headings": {
                    "fontFamily": self.brand_config.regular_font,
                    "fontWeight": "600",
                },
            },
            "sidebar": {
                "backgroundColor": self.brand_config.nav_bg_color,
                "textColor": self.brand_config.nav_text_color,
            },
            "rightPanel": {
                "backgroundColor": self.brand_config.header_color,
            },
        }

    def with_custom_theme(self, theme_config: dict[str, Any]) -> "SynetoReDoc":
        """
        Apply custom theme configuration.

        Args:
            theme_config: Custom theme configuration

        Returns:
            Self for method chaining
        """
        self.redoc_config["theme"].update(theme_config)
        return self

    def with_search_disabled(self) -> "SynetoReDoc":
        """
        Disable search functionality.

        Returns:
            Self for method chaining
        """
        self.redoc_config["disableSearch"] = True
        return self
