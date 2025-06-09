"""
Syneto-branded SwaggerUI implementation.
"""

from typing import Optional, Dict, Any
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
        **kwargs: Any
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
        
        # Apply Syneto defaults for SwaggerUI
        syneto_defaults = {
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
            const originalSwaggerUIBundle = window.SwaggerUIBundle;
            
            if (originalSwaggerUIBundle) {
                window.SwaggerUIBundle = function(config) {
                    // Add Syneto-specific configuration
                    const synetoConfig = {
                        ...config,
                        onComplete: function() {
                            // Hide loading indicator
                            const loading = document.querySelector('.syneto-swagger-loading');
                            if (loading && loading.parentNode) {
                                loading.parentNode.removeChild(loading);
                            }
                            
                            // Call original onComplete if provided
                            if (config.onComplete) {
                                config.onComplete.apply(this, arguments);
                            }
                        },
                        onFailure: function(error) {
                            // Show error state
                            const loading = document.querySelector('.syneto-swagger-loading');
                            if (loading) {
                                loading.innerHTML = `
                                    <div class="syneto-error">
                                        <h3>Failed to Load API Documentation</h3>
                                        <p>Unable to load the OpenAPI specification.</p>
                                        <p>Please check the URL and try again.</p>
                                        <p><small>Error: ${error.message || 'Unknown error'}</small></p>
                                    </div>
                                `;
                            }
                            
                            // Call original onFailure if provided
                            if (config.onFailure) {
                                config.onFailure.apply(this, arguments);
                            }
                        }
                    };
                    
                    return originalSwaggerUIBundle(synetoConfig);
                };
            }
            
            // Show loading indicator
            const container = document.querySelector('.syneto-swagger-container');
            if (container) {
                const loadingDiv = document.createElement('div');
                loadingDiv.className = 'syneto-swagger-loading syneto-loading';
                loadingDiv.textContent = 'Loading API Documentation...';
                container.appendChild(loadingDiv);
                
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
            }
        })();
        </script>
        """
        
        # Inject customizations
        if "</head>" in html:
            html = html.replace("</head>", f"{custom_styles}</head>")
        
        if '<div id="swagger-ui">' in html and "</body>" in html:
            html = html.replace('<div id="swagger-ui">', '<div class="syneto-swagger-container"><div id="swagger-ui">')
            html = html.replace("</body>", f"{custom_scripts}</body>")
        
        # Add favicon
        if self.brand_config.favicon_url and "<head>" in html:
            favicon_link = f'<link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">'
            html = html.replace("<head>", f"<head>{favicon_link}")
        
        return html 