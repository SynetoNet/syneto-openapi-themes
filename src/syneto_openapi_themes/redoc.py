"""
Syneto-branded ReDoc implementation.
"""

from typing import Optional, Dict, Any
from openapipages import ReDoc
from .brand import SynetoBrandConfig, get_default_brand_config, SynetoColors


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
        **kwargs: Any
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
        
        # Apply Syneto defaults for ReDoc
        syneto_defaults = {
            "scrollYOffset": 60,
            "hideDownloadButton": False,
            "disableSearch": False,
            "hideLoading": False,
            "nativeScrollbars": False,
            "theme": {
                "colors": {
                    "primary": {
                        "main": self.brand_config.primary_color
                    },
                    "success": {
                        "main": SynetoColors.ACCENT_GREEN
                    },
                    "warning": {
                        "main": SynetoColors.ACCENT_YELLOW
                    },
                    "error": {
                        "main": SynetoColors.ACCENT_RED
                    },
                    "gray": {
                        "50": SynetoColors.NEUTRAL_100,
                        "100": SynetoColors.NEUTRAL_200,
                        "200": SynetoColors.NEUTRAL_300,
                        "300": SynetoColors.NEUTRAL_400,
                        "400": SynetoColors.NEUTRAL_500,
                        "500": SynetoColors.NEUTRAL_600,
                        "600": SynetoColors.NEUTRAL_700,
                        "700": SynetoColors.NEUTRAL_800,
                        "800": SynetoColors.NEUTRAL_900,
                        "900": SynetoColors.PRIMARY_DARK
                    }
                },
                "typography": {
                    "fontSize": "14px",
                    "lineHeight": "1.5em",
                    "code": {
                        "fontSize": "13px",
                        "fontFamily": self.brand_config.mono_font
                    },
                    "headings": {
                        "fontFamily": self.brand_config.regular_font,
                        "fontWeight": "600"
                    }
                },
                "sidebar": {
                    "backgroundColor": self.brand_config.nav_bg_color,
                    "textColor": self.brand_config.nav_text_color,
                    "activeTextColor": self.brand_config.primary_color,
                    "groupItems": {
                        "textTransform": "uppercase"
                    },
                    "level1Items": {
                        "textTransform": "none"
                    }
                },
                "rightPanel": {
                    "backgroundColor": self.brand_config.header_color,
                    "textColor": self.brand_config.text_color
                }
            }
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
        
        /* Syneto ReDoc Theme Overrides */
        body {{
            font-family: {self.brand_config.regular_font};
            background-color: {self.brand_config.background_color};
            color: {self.brand_config.text_color};
        }}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {self.brand_config.nav_bg_color};
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: {self.brand_config.primary_color};
            border-radius: 4px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
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
        
        /* ReDoc specific customizations */
        .redoc-wrap {{
            background-color: {self.brand_config.background_color};
        }}
        
        /* Header customizations */
        .api-info h1 {{
            color: {self.brand_config.primary_color} !important;
        }}
        
        /* Method badges */
        .http-verb.get {{
            background-color: {self.brand_config.primary_color} !important;
        }}
        
        .http-verb.post {{
            background-color: {self.brand_config.primary_color} !important;
        }}
        
        .http-verb.put {{
            background-color: {SynetoColors.ACCENT_BLUE} !important;
        }}
        
        .http-verb.delete {{
            background-color: {SynetoColors.ACCENT_RED} !important;
        }}
        
        .http-verb.patch {{
            background-color: {SynetoColors.ACCENT_YELLOW} !important;
        }}
        
        /* Search box */
        .search-box input {{
            background-color: {self.brand_config.header_color} !important;
            border-color: {self.brand_config.primary_color} !important;
            color: {self.brand_config.text_color} !important;
        }}
        
        .search-box input:focus {{
            border-color: {self.brand_config.nav_accent_color} !important;
        }}
        
        /* Code blocks */
        .redoc-json code {{
            background-color: {self.brand_config.header_color} !important;
            color: {self.brand_config.text_color} !important;
        }}
        
        /* Response examples */
        .tab-success {{
            color: {SynetoColors.ACCENT_GREEN} !important;
        }}
        
        .tab-error {{
            color: {SynetoColors.ACCENT_RED} !important;
        }}
        </style>
        """
        
        # Add custom JavaScript
        custom_scripts = """
        <script>
        (function() {
            // Enhanced ReDoc initialization
            const originalRedoc = window.Redoc;
            
            if (originalRedoc && originalRedoc.init) {
                const originalInit = originalRedoc.init;
                
                originalRedoc.init = function(spec, options, element, callback) {
                    // Show loading indicator
                    const container = element || document.body;
                    const loadingDiv = document.createElement('div');
                    loadingDiv.className = 'syneto-redoc-loading syneto-loading';
                    loadingDiv.textContent = 'Loading API Documentation...';
                    container.appendChild(loadingDiv);
                    
                    // Enhanced callback
                    const enhancedCallback = function(error) {
                        // Hide loading indicator
                        if (loadingDiv.parentNode) {
                            loadingDiv.parentNode.removeChild(loadingDiv);
                        }
                        
                        if (error) {
                            // Show error state
                            const errorDiv = document.createElement('div');
                            errorDiv.className = 'syneto-error';
                            errorDiv.innerHTML = `
                                <h3>Failed to Load API Documentation</h3>
                                <p>Unable to load the OpenAPI specification.</p>
                                <p>Please check the URL and try again.</p>
                                <p><small>Error: ${error.message || 'Unknown error'}</small></p>
                            `;
                            container.appendChild(errorDiv);
                        }
                        
                        // Call original callback if provided
                        if (callback) {
                            callback.apply(this, arguments);
                        }
                    };
                    
                    // Set timeout for loading
                    setTimeout(() => {
                        if (loadingDiv.parentNode) {
                            loadingDiv.innerHTML = `
                                <div class="syneto-error">
                                    <h3>Loading Timeout</h3>
                                    <p>The API documentation is taking longer than expected to load.</p>
                                    <p>Please refresh the page or check your connection.</p>
                                </div>
                            `;
                        }
                    }, 30000);
                    
                    return originalInit.call(this, spec, options, element, enhancedCallback);
                };
            }
        })();
        </script>
        """
        
        # Inject customizations
        if "</head>" in html:
            html = html.replace("</head>", f"{custom_styles}</head>")
        
        if '<div id="redoc-container">' in html and "</body>" in html:
            html = html.replace('<div id="redoc-container">', '<div class="syneto-redoc-container"><div id="redoc-container">')
            html = html.replace("</body>", f"{custom_scripts}</body>")
        
        # Add favicon
        if self.brand_config.favicon_url and "<head>" in html:
            favicon_link = f'<link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">'
            html = html.replace("<head>", f"<head>{favicon_link}")
        
        return html 