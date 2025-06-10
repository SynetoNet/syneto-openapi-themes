"""
Syneto-branded Scalar implementation.
"""

from typing import Any, Optional

from openapipages import Scalar

from .brand import SynetoBrandConfig, get_default_brand_config


class SynetoScalar(Scalar):
    """
    Syneto-branded Scalar documentation generator.

    Extends OpenAPIPages Scalar with Syneto theming and branding.
    """

    def __init__(
        self,
        openapi_url: str = "/openapi.json",
        title: str = "API Documentation",
        brand_config: Optional[SynetoBrandConfig] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoScalar.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            **kwargs: Additional Scalar configuration options
        """
        self.brand_config = brand_config or get_default_brand_config()

        # Store Scalar-specific configuration for use in rendering
        self.scalar_config = {
            "layout": "modern",
            "theme": self.brand_config.theme.value,
            "showSidebar": True,
            "hideModels": False,
            "hideDownloadButton": False,
            "darkMode": self.brand_config.theme.value == "dark",
            "customCss": "",
            "searchHotKey": "k",
            "metaData": {
                "title": title,
                "description": "API Documentation powered by Syneto",
                "ogDescription": "API Documentation powered by Syneto",
            },
            **kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": kwargs.get("js_url", "https://cdn.jsdelivr.net/npm/@scalar/api-reference"),
            "head_js_urls": kwargs.get("head_js_urls", []),
            "tail_js_urls": kwargs.get("tail_js_urls", []),
            "head_css_urls": kwargs.get("head_css_urls", []),
            "favicon_url": kwargs.get("favicon_url", self.brand_config.favicon_url),
            "proxy_url": kwargs.get("proxy_url", ""),
        }

        super().__init__(**valid_parent_params)

    def render(self, **kwargs: Any) -> str:
        """
        Render the Syneto-branded Scalar HTML.

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
        Inject Syneto-specific customizations into the Scalar HTML.

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

        /* Syneto Scalar Theme */
        .scalar-app {{
            --scalar-color-1: {self.brand_config.primary_color};
            --scalar-color-2: {self.brand_config.nav_accent_color};
            --scalar-color-3: {self.brand_config.background_color};
            --scalar-background-1: {self.brand_config.background_color};
            --scalar-background-2: {self.brand_config.header_color};
            --scalar-background-3: {self.brand_config.nav_bg_color};
            --scalar-text-1: {self.brand_config.text_color};
            --scalar-text-2: {self.brand_config.nav_text_color};
            --scalar-text-3: {self.brand_config.nav_hover_text_color};
            --scalar-border-color: {self.brand_config.nav_bg_color};
            --scalar-font: {self.brand_config.regular_font};
            --scalar-font-code: {self.brand_config.mono_font};
        }}

        /* Sidebar styling */
        .scalar-sidebar {{
            background-color: {self.brand_config.nav_bg_color} !important;
            color: {self.brand_config.nav_text_color} !important;
        }}

        .scalar-sidebar .scalar-sidebar-item {{
            color: {self.brand_config.nav_text_color} !important;
        }}

        .scalar-sidebar .scalar-sidebar-item:hover {{
            background-color: {self.brand_config.nav_hover_bg_color} !important;
            color: {self.brand_config.nav_hover_text_color} !important;
        }}

        .scalar-sidebar .scalar-sidebar-item.active {{
            background-color: {self.brand_config.nav_accent_color} !important;
            color: {self.brand_config.nav_accent_text_color} !important;
        }}

        /* Main content styling */
        .scalar-content {{
            background-color: {self.brand_config.background_color} !important;
            color: {self.brand_config.text_color} !important;
        }}

        /* Header styling */
        .scalar-header h1 {{
            color: {self.brand_config.primary_color} !important;
            font-family: {self.brand_config.regular_font} !important;
        }}

        /* Button styling */
        .scalar-button--primary {{
            background-color: {self.brand_config.primary_color} !important;
            border-color: {self.brand_config.primary_color} !important;
        }}

        .scalar-button--primary:hover {{
            background-color: {self.brand_config.nav_accent_color} !important;
            border-color: {self.brand_config.nav_accent_color} !important;
        }}

        /* Method badges */
        .scalar-method-get {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .scalar-method-post {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .scalar-method-put {{
            background-color: {self.brand_config.primary_color} !important;
        }}

        .scalar-method-delete {{
            background-color: #f01932 !important;
        }}

        /* Custom scrollbar styling */
        .scalar-sidebar::-webkit-scrollbar {{
            width: 8px;
        }}

        .scalar-sidebar::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}

        .scalar-sidebar::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .scalar-sidebar::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        .scalar-content::-webkit-scrollbar {{
            width: 8px;
        }}

        .scalar-content::-webkit-scrollbar-track {{
            background: {self.brand_config.background_color};
        }}

        .scalar-content::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}

        .scalar-content::-webkit-scrollbar-thumb:hover {{
            background: {self.brand_config.nav_accent_color};
        }}

        /* Loading and error states */
        .syneto-scalar-container {{
            position: relative;
            min-height: 100vh;
        }}

        .syneto-scalar-loading {{
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
            // Enhanced Scalar initialization
            console.log('Syneto Scalar Theme loaded');

            // Add loading state management
            const scalarContainer = document.querySelector('#scalar-container');
            if (scalarContainer) {
                // Show loading state
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-scalar-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                scalarContainer.appendChild(loadingDiv);

                // Enhanced error handling
                window.addEventListener('error', function(e) {
                    if (e.message && e.message.includes('scalar')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.innerHTML = `
                                <div class="syneto-error">
                                    <h3>Failed to Load API Documentation</h3>
                                    <p>Unable to load the Scalar interface.</p>
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

                // Remove loading state when Scalar is ready
                const checkScalarReady = setInterval(() => {
                    if (document.querySelector('.scalar-app')) {
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                        clearInterval(checkScalarReady);
                    }
                }, 100);
            }

            // Enhanced interactive features
            document.addEventListener('DOMContentLoaded', function() {
                // Add keyboard shortcuts
                document.addEventListener('keydown', function(e) {
                    if (e.ctrlKey || e.metaKey) {
                        switch(e.key) {
                            case 'k':
                                e.preventDefault();
                                const searchInput = document.querySelector('.scalar-search input');
                                if (searchInput) {
                                    searchInput.focus();
                                }
                                break;
                        }
                    }
                });

                // Add theme toggle functionality
                const themeToggle = document.querySelector('.scalar-theme-toggle');
                if (themeToggle) {
                    themeToggle.addEventListener('click', function() {
                        document.body.classList.toggle('scalar-dark-mode');
                    });
                }
            });
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

    def get_configuration(self) -> dict[str, Any]:
        """
        Get Scalar configuration.

        Returns:
            Dictionary with Scalar settings
        """
        return {
            "layout": self.scalar_config.get("layout", "modern"),
            "theme": self.scalar_config.get("theme", self.brand_config.theme.value),
            "showSidebar": self.scalar_config.get("showSidebar", True),
            "hideModels": self.scalar_config.get("hideModels", False),
            "hideDownloadButton": self.scalar_config.get("hideDownloadButton", False),
            "darkMode": self.scalar_config.get("darkMode", False),
            "searchHotKey": self.scalar_config.get("searchHotKey", "k"),
        }

    def with_modern_layout(self) -> "SynetoScalar":
        """
        Configure modern layout.

        Returns:
            Self for method chaining
        """
        self.scalar_config["layout"] = "modern"
        return self

    def with_classic_layout(self) -> "SynetoScalar":
        """
        Configure classic layout.

        Returns:
            Self for method chaining
        """
        self.scalar_config["layout"] = "classic"
        return self

    def with_sidebar_hidden(self) -> "SynetoScalar":
        """
        Hide the sidebar.

        Returns:
            Self for method chaining
        """
        self.scalar_config["showSidebar"] = False
        return self

    def with_models_hidden(self) -> "SynetoScalar":
        """
        Hide the models section.

        Returns:
            Self for method chaining
        """
        self.scalar_config["hideModels"] = True
        return self
