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
        header_slot_content: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize SynetoRapiDoc.

        Args:
            openapi_url: URL to the OpenAPI JSON schema
            title: Title for the documentation page
            brand_config: Syneto brand configuration
            header_slot_content: HTML content for the custom header slot (overrides brand logo/header)
            **kwargs: Additional RapiDoc configuration options. These can override any
                     of the default RapiDoc settings. Common overridable parameters include:
                     - render_style: "read" | "view" | "focused" (default: "read")
                     - schema_style: "tree" | "table" (default: "table")
                     - show_header: "true" | "false" (default: "true")
                     - allow_authentication: "true" | "false" (default: "true")
                     - response_area_height: CSS height value (default: "400px")
                     - theme: "light" | "dark" (overrides brand_config.theme)
                     - And many more RapiDoc attributes. See RapiDoc documentation for full list.
        """
        self.brand_config = brand_config or get_default_brand_config()
        self.header_slot_content = header_slot_content

        # Separate parent class parameters from RapiDoc configuration
        parent_class_params = {"js_url", "head_js_urls", "tail_js_urls", "head_css_urls", "favicon_url"}

        # Extract parent class parameters from kwargs
        parent_kwargs = {k: v for k, v in kwargs.items() if k in parent_class_params}

        # Extract RapiDoc configuration parameters (everything else)
        rapidoc_kwargs = {k: v for k, v in kwargs.items() if k not in parent_class_params}

        # Store RapiDoc-specific configuration for use in rendering
        # Note: rapidoc_kwargs will override any default values below

        # Store RapiDoc-specific configuration for use in rendering
        # Note: rapidoc_kwargs will override any default values below

        self.rapidoc_config = {
            # Brand-based configuration (from SynetoBrandConfig)
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
            # Note: We don't set "logo" here since we use slot="logo" to replace it completely
            # Layout and presentation defaults (can be overridden by kwargs)
            "render_style": "read",
            "schema_style": "table",
            "default_schema_tab": "schema",
            "response_area_height": "400px",
            # Feature toggles (can be overridden by kwargs)
            "show_info": "true",
            "allow_authentication": "true",
            "allow_server_selection": "true",
            "allow_api_list_style_selection": "true",
            "show_header": "true",
            "show_components": "true",
            # Navigation and routing (can be overridden by kwargs)
            "update_route": "true",
            "route_prefix": "#",
            "sort_tags": "true",
            "goto_path": "",
            # Form behavior (can be overridden by kwargs)
            "fill_request_fields_with_example": "true",
            "persist_auth": "false",
            # Security/access controls (can be overridden by kwargs)
            "allow_spec_url_load": "false",  # Disable JSON loading features at the top
            "allow_spec_file_load": "false",
            # UI behavior (can be overridden by kwargs)
            "on_nav_tag_click": "show-description",  # Enable tag description in right pane
            # Apply any user-provided overrides
            **rapidoc_kwargs,
        }

        # Extract only valid parameters for the parent constructor
        valid_parent_params = {
            "title": title,
            "openapi_url": openapi_url,
            "js_url": parent_kwargs.get("js_url", "https://unpkg.com/rapidoc@9.3.8/dist/rapidoc-min.js"),
            "head_js_urls": parent_kwargs.get("head_js_urls", []),
            "tail_js_urls": parent_kwargs.get("tail_js_urls", []),
            "head_css_urls": parent_kwargs.get("head_css_urls", []),
            "favicon_url": parent_kwargs.get("favicon_url", self.brand_config.favicon_url),
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
        # Use our own template with RapiDoc attributes instead of parent's fixed template
        self.head_js_urls.insert(0, self.js_url)
        html_template = self.get_html_template()
        base_html = html_template.format(
            title=self.title,
            favicon_url=self.favicon_url,
            openapi_url=self.openapi_url,
            head_css_str=self.get_head_css_str(),
            head_js_str=self.get_head_js_str(),
            tail_js_str=self.get_tail_js_str(),
        )

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

        /* Syneto-specific RapiDoc customizations using Color Chart v4.0 */
        rapi-doc {{
            --green: #1bdc77;    /* Contrast Color - Green */
            --blue: #ff53a8;     /* Syneto Brand Light - Better for links on dark background */
            --orange: #ff8c00;   /* Caution Color - Orange */
            --red: #f01932;      /* Danger Color - Red */
            --yellow: #f7db00;   /* Warning Color - Yellow */
            --purple: #724fff;   /* Accent Color - Purple */

            /* Override default colors with Syneto brand colors */
            --primary-color: {self.brand_config.primary_color};
            --bg-color: {self.brand_config.background_color};
            --text-color: {self.brand_config.text_color};
            --nav-bg-color: {self.brand_config.nav_bg_color};
            --nav-text-color: {self.brand_config.nav_text_color};
            --nav-hover-bg-color: {self.brand_config.nav_hover_bg_color};
            --nav-hover-text-color: {self.brand_config.nav_hover_text_color};
            --nav-accent-color: {self.brand_config.nav_accent_color};
            --border-color: #161c2d;
            --light-border-color: #5c606c;
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

        /* Enhanced tag navigation styling */
        rapi-doc::part(section-navbar) {{
            background: {self.brand_config.nav_bg_color};
            border-right: 1px solid #161c2d;
        }}

        rapi-doc::part(section-navbar-item) {{
            color: {self.brand_config.nav_text_color};
            border-bottom: 1px solid #161c2d;
        }}

        rapi-doc::part(section-navbar-item):hover {{
            background: {self.brand_config.nav_hover_bg_color};
            color: {self.brand_config.nav_hover_text_color};
        }}

        rapi-doc::part(section-navbar-item-active) {{
            background: {self.brand_config.nav_accent_color};
            color: {self.brand_config.nav_accent_text_color};
        }}

        /* Right panel styling for tag descriptions */
        rapi-doc::part(section-main-content) {{
            background: {self.brand_config.background_color};
        }}

        /* Improve button styling with Syneto colors */
        rapi-doc::part(btn-primary) {{
            background: {self.brand_config.primary_color};
            border-color: {self.brand_config.primary_color};
        }}

        rapi-doc::part(btn-primary):hover {{
            background: #800541;
            border-color: #800541;
        }}

        /* Status code styling with proper colors */
        rapi-doc .status-code.success {{
            background: #1bdc77;
            color: #07080d;
        }}

        rapi-doc .status-code.error {{
            background: #f01932;
            color: #fcfdfe;
        }}

        rapi-doc .status-code.warning {{
            background: #f7db00;
            color: #07080d;
        }}

        rapi-doc .status-code.info {{
            background: #724fff;  /* Syneto Accent Primary - Purple instead of harsh blue */
            color: #fcfdfe;
        }}

        /* Link styling with Syneto brand colors */
        rapi-doc a {{
            color: #ff53a8 !important;  /* Syneto Brand Light */
            text-decoration: none;
        }}

        rapi-doc a:hover {{
            color: #ff9dcd !important;  /* Syneto Brand Lighter for hover */
            text-decoration: underline;
        }}

        rapi-doc a:visited {{
            color: #ff53a8 !important;  /* Keep same color for visited links */
        }}

        /* Schema links and references */
        rapi-doc .m-markdown-small a,
        rapi-doc .descr a {{
            color: #ff53a8 !important;
        }}

        rapi-doc .m-markdown-small a:hover,
        rapi-doc .descr a:hover {{
            color: #ff9dcd !important;
        }}
        </style>
        """

        # Add custom JavaScript for enhanced functionality
        custom_scripts = """
        <script>
        // Prevent CustomElementRegistry errors on page reload
        (function() {
            // Store original define method
            const originalDefine = customElements.define;

            // Override define to prevent duplicate registrations
            customElements.define = function(name, constructor, options) {
                if (!customElements.get(name)) {
                    originalDefine.call(this, name, constructor, options);
                } else {
                    console.debug(`Custom element '${name}' already registered, skipping redefinition`);
                }
            };
        })();
        </script>
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

    def get_html_template(self) -> str:
        """
        Return the HTML template for RapiDoc with Syneto configuration.

        Returns:
            HTML template string with RapiDoc configuration attributes
        """
        # Convert rapidoc_config to HTML attributes
        rapidoc_attributes = []
        for key, value in self.rapidoc_config.items():
            # Convert Python dict keys to kebab-case HTML attributes
            attr_name = key.replace("_", "-")

            # Convert Python boolean values to lowercase strings for HTML/JavaScript
            if isinstance(value, bool):
                attr_value = str(value).lower()
            else:
                attr_value = str(value)

            rapidoc_attributes.append(f'{attr_name}="{attr_value}"')

        attributes_str = " ".join(rapidoc_attributes)

        # Create logo slot content to replace the RapiDoc logo completely
        logo_slot = ""
        if self.header_slot_content:
            # If custom header slot content is provided, use it as the logo replacement
            logo_slot = (
                f'<div slot="logo" style="display: flex; align-items: center; margin: 0 16px;">'
                f"{self.header_slot_content}</div>"
            )
        elif self.brand_config.logo_svg:
            # Create a logo replacement with the SVG logo using the brand config SVG
            from .brand import svg_to_data_uri

            # Use the original SVG - it's already white on transparent
            svg_data_uri = svg_to_data_uri(self.brand_config.logo_svg)

            # Use app_title if available, otherwise fall back to company_name
            display_name = self.brand_config.app_title or self.brand_config.company_name

            logo_slot = (
                """<div slot="logo" style="display: flex; align-items: center; """
                + f"""padding: 4px 16px; height: 48px;">
                <img src="{svg_data_uri}"
                     alt="{self.brand_config.company_name} Logo"
                     style="height: 100%; width: auto; margin-right: 12px; """
                + f"""object-fit: contain; filter: invert(1) !important;" />
                <span style="color: {self.brand_config.text_color}; """
                + f"""font-family: {self.brand_config.regular_font}; """
                + f"""font-weight: 600; font-size: 18px;">
                    {display_name}
                </span>
            </div>"""
            )

        html = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8"/>
                <title>{{title}}</title>
                <link rel="shortcut icon" href="{{favicon_url}}">
                {{head_css_str}}
                {{head_js_str}}
            </head>
            <body>
                <div class="syneto-rapidoc-container">
                    <noscript>
                        RapiDoc requires Javascript to function. Please enable it to browse the documentation.
                    </noscript>
                    <rapi-doc spec-url="{{openapi_url}}" {attributes_str}>
                        {logo_slot}
                    </rapi-doc>
                </div>
                {{tail_js_str}}
            </body>
        </html>
        """
        return html
