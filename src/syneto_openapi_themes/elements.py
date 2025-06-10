"""
Syneto-branded Elements implementation.
"""

from typing import Any, Optional

from openapipages import Elements

from .brand import SynetoBrandConfig, get_default_brand_config


class SynetoElements(Elements):
    """
    Syneto-branded Elements documentation generator.

    Extends OpenAPIPages Elements with Syneto theming and branding.
    """

    def __init__(
        self,
        openapi_url: str = "/openapi.json",
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoElements.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            **kwargs: Additional Elements configuration options
        """
        self.brand_config = brand_config or get_default_brand_config()

        # Store Elements-specific configuration for use in rendering
        self.elements_config = {
            "layout": "sidebar",
            "hideInternal": False,
            "hideSchemas": False,
            "hideExport": False,
            "hideTryIt": False,
            "tryItCredentialsPolicy": "include",
            "tryItCorsProxy": "",
            "router": "hash",
            "basePath": "/",
            **kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": kwargs.get("js_url", "https://unpkg.com/@stoplight/elements/web-components.min.js"),
            "head_js_urls": kwargs.get("head_js_urls", []),
            "tail_js_urls": kwargs.get("tail_js_urls", []),
            "head_css_urls": kwargs.get("head_css_urls", []),
            "favicon_url": kwargs.get("favicon_url", self.brand_config.favicon_url),
            "css_url": kwargs.get("css_url", "https://unpkg.com/@stoplight/elements/styles.min.css"),
        }

        super().__init__(**valid_parent_params)

    def render(self, **kwargs: Any) -> str:
        """
        Render the Syneto-branded Elements HTML.

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
        Inject Syneto-specific customizations into the Elements HTML.

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

        /* Syneto Elements Theme */
        elements-api {{
            --color-primary: {self.brand_config.primary_color};
            --color-primary-light: {self.brand_config.nav_accent_color};
            --color-primary-dark: {self.brand_config.primary_color};
            --color-secondary: {self.brand_config.nav_bg_color};
            --color-success: #28a745;
            --color-warning: #ffc107;
            --color-danger: #f01932;
            --color-info: {self.brand_config.primary_color};
            --color-light: {self.brand_config.background_color};
            --color-dark: {self.brand_config.text_color};
            --font-family: {self.brand_config.regular_font};
            --font-family-mono: {self.brand_config.mono_font};
        }}

        /* Sidebar styling */
        .sl-elements-sidebar {{
            background-color: {self.brand_config.nav_bg_color} !important;
            color: {self.brand_config.nav_text_color} !important;
        }}

        .sl-elements-sidebar .sl-stack-item {{
            color: {self.brand_config.nav_text_color} !important;
        }}

        .sl-elements-sidebar .sl-stack-item:hover {{
            background-color: {self.brand_config.nav_hover_bg_color} !important;
            color: {self.brand_config.nav_hover_text_color} !important;
        }}

        .sl-elements-sidebar .sl-stack-item.sl-stack-item--active {{
            background-color: {self.brand_config.nav_accent_color} !important;
            color: {self.brand_config.nav_accent_text_color} !important;
        }}

        /* Main content styling */
        .sl-elements-content {{
            background-color: {self.brand_config.background_color} !important;
            color: {self.brand_config.text_color} !important;
        }}

        /* Header styling */
        .sl-elements-header h1 {{
            color: {self.brand_config.primary_color} !important;
            font-family: {self.brand_config.regular_font} !important;
        }}

        /* Button styling */
        .sl-button--primary {{
            background-color: {self.brand_config.primary_color} !important;
            border-color: {self.brand_config.primary_color} !important;
        }}

        .sl-button--primary:hover {{
            background-color: {self.brand_config.nav_accent_color} !important;
            border-color: {self.brand_config.nav_accent_color} !important;
        }}

        /* Method badges */
        .sl-http-method--get {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .sl-http-method--post {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .sl-http-method--put {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .sl-http-method--delete {{
            background-color: #f01932 !important;
        }}

        /* Custom scrollbar styling */
        .sl-elements-sidebar::-webkit-scrollbar {{
            width: 8px;
        }}

        .sl-elements-sidebar::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}

        .sl-elements-sidebar::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .sl-elements-sidebar::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        .sl-elements-content::-webkit-scrollbar {{
            width: 8px;
        }}

        .sl-elements-content::-webkit-scrollbar-track {{
            background: {self.brand_config.background_color};
        }}

        .sl-elements-content::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .sl-elements-content::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        /* Loading and error states */
        .syneto-elements-container {{
            position: relative;
            min-height: 100vh;
        }}

        .syneto-elements-loading {{
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
            // Enhanced Elements initialization
            console.log('Syneto Elements Theme loaded');

            // Add loading state management
            const elementsContainer = document.querySelector('elements-api');
            if (elementsContainer) {
                // Show loading state
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-elements-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                elementsContainer.appendChild(loadingDiv);

                // Enhanced error handling
                window.addEventListener('error', function(e) {
                    if (e.message && e.message.includes('elements')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.innerHTML = `
                                <div class="syneto-error">
                                    <h3>Failed to Load API Documentation</h3>
                                    <p>Unable to load the Elements interface.</p>
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

                // Remove loading state when Elements is ready
                const checkElementsReady = setInterval(() => {
                    if (document.querySelector('.sl-elements-api')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                        clearInterval(checkElementsReady);
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

    def get_layout_config(self) -> dict[str, Any]:
        """
        Get layout configuration for Elements.

        Returns:
            Dictionary with layout settings
        """
        return {
            "layout": self.elements_config.get("layout", "sidebar"),
            "hideInternal": self.elements_config.get("hideInternal", False),
            "hideSchemas": self.elements_config.get("hideSchemas", False),
            "hideExport": self.elements_config.get("hideExport", False),
            "hideTryIt": self.elements_config.get("hideTryIt", False),
            "tryItCredentialsPolicy": self.elements_config.get("tryItCredentialsPolicy", "include"),
            "router": self.elements_config.get("router", "hash"),
            "basePath": self.elements_config.get("basePath", "/"),
        }

    def with_sidebar_layout(self) -> "SynetoElements":
        """
        Configure sidebar layout.

        Returns:
            Self for method chaining
        """
        self.elements_config["layout"] = "sidebar"
        return self

    def with_stacked_layout(self) -> "SynetoElements":
        """
        Configure stacked layout.

        Returns:
            Self for method chaining
        """
        self.elements_config["layout"] = "stacked"
        return self

    def with_try_it_disabled(self) -> "SynetoElements":
        """
        Disable Try It functionality.

        Returns:
            Self for method chaining
        """
        self.elements_config["hideTryIt"] = True
        return self
