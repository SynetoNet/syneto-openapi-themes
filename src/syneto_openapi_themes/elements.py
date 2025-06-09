"""
Syneto-branded Elements implementation.
"""

from typing import Optional, Dict, Any
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
        **kwargs: Any
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
        
        # Apply Syneto defaults for Elements
        syneto_defaults = {
            "layout": "sidebar",
            "hideInternal": False,
            "hideTryIt": False,
            "hideSchemas": False,
            "hideExport": False,
        }
        
        # Merge with user-provided kwargs
        final_config = {**syneto_defaults, **kwargs}
        
        super().__init__(
            openapi_url=openapi_url,
            title=title,
            **final_config
        )
    
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
        body {{
            font-family: {self.brand_config.regular_font};
            background-color: {self.brand_config.background_color};
            color: {self.brand_config.text_color};
        }}
        
        /* Elements specific customizations */
        .sl-elements {{
            --color-primary: {self.brand_config.primary_color};
            --color-success: {SynetoColors.ACCENT_GREEN};
            --color-warning: {SynetoColors.ACCENT_YELLOW};
            --color-danger: {SynetoColors.ACCENT_RED};
            --color-canvas: {self.brand_config.background_color};
            --color-canvas-100: {self.brand_config.header_color};
            --color-canvas-200: {self.brand_config.nav_bg_color};
            --font-family: {self.brand_config.regular_font};
            --font-family-mono: {self.brand_config.mono_font};
        }}
        
        /* Custom scrollbar */
        .sl-elements ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        .sl-elements ::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}
        
        .sl-elements ::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}
        
        .sl-elements ::-webkit-scrollbar-thumb:hover {{
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
        
        /* Header styling */
        .sl-elements .sl-panel .sl-panel-header {{
            background-color: {self.brand_config.nav_bg_color};
            border-bottom: 2px solid {self.brand_config.primary_color};
        }}
        
        /* Sidebar styling */
        .sl-elements .sl-sidebar {{
            background-color: {self.brand_config.nav_bg_color};
            border-right: 1px solid {self.brand_config.header_color};
        }}
        
        /* Try it button */
        .sl-elements .sl-button--primary {{
            background-color: {self.brand_config.primary_color};
            border-color: {self.brand_config.primary_color};
        }}
        
        .sl-elements .sl-button--primary:hover {{
            background-color: {self.brand_config.nav_accent_color};
            border-color: {self.brand_config.nav_accent_color};
        }}
        </style>
        """
        
        # Add custom JavaScript
        custom_scripts = """
        <script>
        (function() {
            // Enhanced Elements initialization
            const container = document.querySelector('.syneto-elements-container');
            if (container) {
                // Show loading indicator
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-elements-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                container.appendChild(loadingDiv);
                
                // Wait for Elements to load
                const checkElements = setInterval(() => {
                    const elementsContainer = document.querySelector('.sl-elements');
                    if (elementsContainer) {
                        clearInterval(checkElements);
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
                        clearInterval(checkElements);
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
        
        if '<div id="elements">' in html and "</body>" in html:
            html = html.replace('<div id="elements">', '<div class="syneto-elements-container"><div id="elements">')
            html = html.replace("</body>", f"{custom_scripts}</body>")
        
        # Add favicon
        if self.brand_config.favicon_url and "<head>" in html:
            favicon_link = f'<link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">'
            html = html.replace("<head>", f"<head>{favicon_link}")
        
        return html 