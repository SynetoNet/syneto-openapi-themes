"""
Syneto-branded Scalar implementation.
"""

from typing import Optional, Dict, Any
from openapipages import Scalar
from .brand import SynetoBrandConfig, get_default_brand_config, SynetoColors


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
        **kwargs: Any
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
        
        # Apply Syneto defaults for Scalar
        syneto_defaults = {
            "layout": "modern",
            "theme": self.brand_config.theme.value,
            "showSidebar": True,
            "hideModels": False,
            "hideDownloadButton": False,
            "darkMode": self.brand_config.theme.value == "dark",
            "customCss": self._get_syneto_scalar_css(),
        }
        
        # Merge with user-provided kwargs
        final_config = {**syneto_defaults, **kwargs}
        
        super().__init__(
            openapi_url=openapi_url,
            title=title,
            **final_config
        )
    
    def _get_syneto_scalar_css(self) -> str:
        """Get Syneto-specific CSS for Scalar."""
        return f"""
        :root {{
            --scalar-color-1: {self.brand_config.primary_color};
            --scalar-color-2: {self.brand_config.nav_accent_color};
            --scalar-color-3: {self.brand_config.background_color};
            --scalar-color-accent: {self.brand_config.primary_color};
            --scalar-background-1: {self.brand_config.background_color};
            --scalar-background-2: {self.brand_config.header_color};
            --scalar-background-3: {self.brand_config.nav_bg_color};
            --scalar-background-accent: {self.brand_config.primary_color};
            --scalar-border-color: {self.brand_config.nav_bg_color};
            --scalar-font: {self.brand_config.regular_font};
            --scalar-font-code: {self.brand_config.mono_font};
        }}
        
        .scalar-app {{
            --scalar-sidebar-background-1: {self.brand_config.nav_bg_color};
            --scalar-sidebar-item-hover-color: {self.brand_config.nav_hover_bg_color};
            --scalar-sidebar-item-active-background: {self.brand_config.primary_color};
        }}
        """
    
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
        body {{
            font-family: {self.brand_config.regular_font};
            background-color: {self.brand_config.background_color};
            color: {self.brand_config.text_color};
        }}
        
        {self._get_syneto_scalar_css()}
        
        /* Custom scrollbar */
        .scalar-app ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        .scalar-app ::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}
        
        .scalar-app ::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}
        
        .scalar-app ::-webkit-scrollbar-thumb:hover {{
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
        
        /* Method badges customization */
        .scalar-app .http-method.get {{
            background-color: {self.brand_config.primary_color};
        }}
        
        .scalar-app .http-method.post {{
            background-color: {self.brand_config.primary_color};
        }}
        
        .scalar-app .http-method.put {{
            background-color: {SynetoColors.ACCENT_BLUE};
        }}
        
        .scalar-app .http-method.delete {{
            background-color: {SynetoColors.ACCENT_RED};
        }}
        
        .scalar-app .http-method.patch {{
            background-color: {SynetoColors.ACCENT_YELLOW};
        }}
        
        /* Button styling */
        .scalar-app .scalar-button--primary {{
            background-color: {self.brand_config.primary_color};
            border-color: {self.brand_config.primary_color};
        }}
        
        .scalar-app .scalar-button--primary:hover {{
            background-color: {self.brand_config.nav_accent_color};
            border-color: {self.brand_config.nav_accent_color};
        }}
        </style>
        """
        
        # Add custom JavaScript
        custom_scripts = """
        <script>
        (function() {
            // Enhanced Scalar initialization
            const container = document.querySelector('.syneto-scalar-container');
            if (container) {
                // Show loading indicator
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-scalar-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                container.appendChild(loadingDiv);
                
                // Wait for Scalar to load
                const checkScalar = setInterval(() => {
                    const scalarApp = document.querySelector('.scalar-app');
                    if (scalarApp) {
                        clearInterval(checkScalar);
                        setTimeout(() => {
                            if (loadingDiv.parentNode) {
                                loadingDiv.parentNode.removeChild(loadingDiv);
                            }
                        }, 500);
                    }
                }, 100);
                
                // Set timeout for loading
                setTimeout(() => {
                    if (loadingDiv.parentNode) {
                        clearInterval(checkScalar);
                        loadingDiv.innerHTML = `
                            <div class="syneto-error">
                                <h3>Loading Timeout</h3>
                                <p>The API documentation is taking longer than expected to load.</p>
                                <p>Please refresh the page or check your connection.</p>
                            </div>
                        `;
                    }
                }, 30000);
            }
        })();
        </script>
        """
        
        # Inject customizations
        if "</head>" in html:
            html = html.replace("</head>", f"{custom_styles}</head>")
        
        if '<div id="scalar">' in html and "</body>" in html:
            html = html.replace('<div id="scalar">', '<div class="syneto-scalar-container"><div id="scalar">')
            html = html.replace("</body>", f"{custom_scripts}</body>")
        
        # Add favicon
        if self.brand_config.favicon_url and "<head>" in html:
            favicon_link = f'<link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">'
            html = html.replace("<head>", f"<head>{favicon_link}")
        
        return html 