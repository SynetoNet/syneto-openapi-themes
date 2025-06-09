"""
Syneto-branded RapiDoc implementation.
"""

from typing import Optional, Dict, Any, Union
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
        **kwargs: Any
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
        
        # Apply Syneto defaults
        syneto_defaults = {
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
        }
        
        # Merge with user-provided kwargs (user values take precedence)
        final_config = {**syneto_defaults, **kwargs}
        
        super().__init__(
            openapi_url=openapi_url,
            title=title,
            **final_config
        )
    
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
                    if (loadingDiv.parentNode) {
                        loadingDiv.innerHTML = `
                            <div class="syneto-error">
                                <h3>Loading Timeout</h3>
                                <p>The API documentation is taking longer than expected to load.</p>
                                <p>Please refresh the page or check your connection.</p>
                            </div>
                        `;
                    }
                }, 30000); // 30 second timeout
            }
            
            // Add authentication helpers if needed
            if (window.location.hash.includes('auth')) {
                // Handle authentication state
                console.log('Syneto RapiDoc: Authentication mode detected');
            }
        })();
        </script>
        """
        
        # Inject custom CSS and JS before closing head tag
        if "</head>" in html:
            html = html.replace("</head>", f"{custom_styles}</head>")
        
        # Wrap rapi-doc element in container and inject scripts before closing body
        if "<rapi-doc" in html and "</body>" in html:
            html = html.replace("<rapi-doc", '<div class="syneto-rapidoc-container"><rapi-doc')
            html = html.replace("</rapi-doc>", "</rapi-doc></div>")
            html = html.replace("</body>", f"{custom_scripts}</body>")
        
        # Add favicon if specified
        if self.brand_config.favicon_url and "<head>" in html:
            favicon_link = f'<link rel="icon" type="image/x-icon" href="{self.brand_config.favicon_url}">'
            html = html.replace("<head>", f"<head>{favicon_link}")
        
        return html
    
    def get_authentication_config(self) -> Dict[str, Any]:
        """
        Get authentication configuration for the documentation.
        
        Returns:
            Dictionary with authentication settings
        """
        return {
            "allow_authentication": "true",
            "persist_auth": "false",
            "api_key_name": "X-API-Key",
            "api_key_location": "header",
        }
    
    def with_jwt_auth(self, jwt_url: str = "/auth/token") -> "SynetoRapiDoc":
        """
        Configure RapiDoc for JWT authentication.
        
        Args:
            jwt_url: URL for JWT token endpoint
            
        Returns:
            Self for method chaining
        """
        # This would be implemented based on specific JWT requirements
        return self
    
    def with_api_key_auth(self, api_key_name: str = "X-API-Key") -> "SynetoRapiDoc":
        """
        Configure RapiDoc for API key authentication.
        
        Args:
            api_key_name: Name of the API key header
            
        Returns:
            Self for method chaining
        """
        # This would be implemented based on specific API key requirements
        return self 