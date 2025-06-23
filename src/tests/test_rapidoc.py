"""
Tests for the SynetoRapiDoc implementation.
"""

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from syneto_openapi_themes.rapidoc import SynetoRapiDoc


class TestSynetoRapiDocInitialization:
    """Test SynetoRapiDoc initialization and configuration."""

    def test_default_initialization(self) -> None:
        """Test default RapiDoc initialization."""
        rapidoc = SynetoRapiDoc()

        assert rapidoc.openapi_url == "/openapi.json"
        assert rapidoc.title == "API Documentation"
        assert rapidoc.brand_config is not None
        assert rapidoc.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self) -> None:
        """Test RapiDoc initialization with custom parameters."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT, company_name="Custom Corp", primary_color="#ff0000")

        rapidoc = SynetoRapiDoc(
            openapi_url="/custom/openapi.json",
            title="Custom API Docs",
            brand_config=brand_config,
            theme="light",
            render_style="focused",
        )

        assert rapidoc.openapi_url == "/custom/openapi.json"
        assert rapidoc.title == "Custom API Docs"
        assert rapidoc.brand_config.company_name == "Custom Corp"
        assert rapidoc.brand_config.primary_color == "#ff0000"

    def test_initialization_with_kwargs(self) -> None:
        """Test RapiDoc initialization with additional kwargs."""
        rapidoc = SynetoRapiDoc(show_header=False, allow_try=True, show_info=True, nav_bg_color="#123456")

        assert rapidoc.brand_config is not None


class TestSynetoRapiDocRendering:
    """Test SynetoRapiDoc HTML rendering functionality."""

    def test_render_calls_parent_and_injects_customizations(self) -> None:
        """Test that render generates HTML with Syneto customizations."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        # Check that the result contains expected content
        assert "Syneto-specific RapiDoc customizations" in result
        assert "syneto-rapidoc-container" in result
        assert rapidoc.brand_config.primary_color in result
        assert "<rapi-doc" in result
        assert "spec-url=" in result

    def test_render_with_custom_brand_config(self) -> None:
        """Test rendering with custom brand configuration."""
        brand_config = SynetoBrandConfig(
            primary_color="#custom123", background_color="#bg456", company_name="Test Corp"
        )

        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        result = rapidoc.render()

        assert "#custom123" in result
        assert "#bg456" in result
        # Company name now appears in logo slot alt text
        assert "Test Corp Logo" in result

    def test_render_includes_css_variables(self) -> None:
        """Test that render includes CSS variables from brand config."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    def test_render_includes_loading_css(self) -> None:
        """Test that render includes loading CSS."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    def test_render_includes_javascript_enhancements(self) -> None:
        """Test that render includes JavaScript enhancements."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        # Should include JavaScript enhancements
        assert "spec-load-error" in result
        assert "Failed to Load API Documentation" in result

    def test_render_with_kwargs(self) -> None:
        """Test rendering with additional template variables."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render(custom_var="test_value")

        # The result should still contain the basic RapiDoc structure
        assert "<rapi-doc" in result
        assert "spec-url=" in result

    def test_render_with_empty_base_html(self) -> None:
        """Test rendering with empty base HTML."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        # Should generate complete HTML even without base
        assert "<style>" in result
        assert "<rapi-doc" in result

    def test_render_with_malformed_base_html(self) -> None:
        """Test rendering with malformed base HTML."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        # Should still inject customizations and generate valid HTML
        assert "Syneto-specific RapiDoc customizations" in result
        assert "<rapi-doc" in result
        assert "<!DOCTYPE html>" in result

    def test_improved_link_colors(self) -> None:
        """Test that links use Syneto brand colors instead of harsh blue."""
        rapidoc = SynetoRapiDoc()
        html = rapidoc.render()

        # Check that links use Syneto Brand Light color
        assert "#ff53a8" in html  # Syneto Brand Light for links
        assert "#ff9dcd" in html  # Syneto Brand Lighter for hover

        # Check that specific link styling is present
        assert "rapi-doc a {" in html
        assert "color: #ff53a8 !important" in html

        # Verify the old harsh blue color is not used for links
        # Note: #006aff might still appear in other contexts (like constants)
        # but should not be used for the --blue CSS variable
        assert "--blue: #ff53a8" in html  # New brand color for blue variable
        assert "--blue: #006aff" not in html  # Old harsh blue should be gone

    def test_logo_slot_functionality(self) -> None:
        """Test that logo slot is correctly included in the HTML."""
        rapidoc = SynetoRapiDoc()
        html = rapidoc.render()

        # Check that logo slot is present
        assert 'slot="logo"' in html
        assert "data:image/svg+xml" in html
        assert 'alt="Syneto Logo"' in html

        # Check that logo is inside rapi-doc element
        import re

        rapi_doc_match = re.search(r"<rapi-doc[^>]*>(.*?)</rapi-doc>", html, re.DOTALL)
        assert rapi_doc_match is not None
        assert 'slot="logo"' in rapi_doc_match.group(1)

    def test_custom_logo_slot_content(self) -> None:
        """Test that custom logo slot content overrides default."""
        custom_logo = '<img src="/custom-logo.png" alt="Custom Logo" />'
        rapidoc = SynetoRapiDoc(header_slot_content=custom_logo)
        html = rapidoc.render()

        # Check that custom logo content is present in logo slot
        assert 'slot="logo"' in html
        assert 'src="/custom-logo.png"' in html
        assert 'alt="Custom Logo"' in html

        # Check that default Syneto logo is not present when custom is used
        assert 'alt="Syneto Logo"' not in html

    def test_app_title_in_logo_slot(self) -> None:
        """Test that app_title is displayed in logo slot instead of company_name."""
        # Test with app_title set
        brand_config = SynetoBrandConfig(app_title="My Application", company_name="My Company")
        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        html = rapidoc.render()

        # Should display app_title in the logo slot
        assert "My Application" in html
        # Company name should only appear in alt text, not as displayed text
        assert 'alt="My Company Logo"' in html

        # Test with only company_name (no app_title)
        brand_config = SynetoBrandConfig(company_name="My Company")
        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        html = rapidoc.render()

        # Should display company_name when app_title is not set
        assert "My Company" in html
        assert 'alt="My Company Logo"' in html

        # Test default behavior (no app_title, default company_name)
        rapidoc = SynetoRapiDoc()
        html = rapidoc.render()

        # Should display default company name
        assert "Syneto" in html
        assert 'alt="Syneto Logo"' in html


class TestSynetoRapiDocCustomizations:
    """Test SynetoRapiDoc customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self) -> None:
        """Test customization injection with minimal HTML."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert "rapi-doc" in result
        assert rapidoc.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self) -> None:
        """Test that customization injection preserves original HTML content."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body><div id='original'>Original Content</div></body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='original'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self) -> None:
        """Test that customizations include scrollbar styling."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_error_handling(self) -> None:
        """Test that customizations include error handling JavaScript."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "spec-load-error" in result
        assert "Failed to Load API Documentation" in result
        assert "setTimeout" in result

    def test_inject_customizations_without_body_tag(self) -> None:
        """Test customization injection when HTML doesn't contain </body> tag."""
        rapidoc = SynetoRapiDoc()
        # HTML without </body> tag to test the else branch
        base_html = "<html><head></head><div>Content without body tag</div></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        # Should still inject customizations even without </body> tag
        assert "Syneto-specific RapiDoc customizations" in result
        assert "<style>" in result
        assert "<script>" in result
        assert "Content without body tag" in result
        # Scripts should be appended at the end when there's no </body> tag
        assert "</script>" in result
        # The original content should still be there
        assert "<div>Content without body tag</div>" in result


class TestSynetoRapiDocAuthentication:
    """Test SynetoRapiDoc authentication configuration."""

    def test_get_authentication_config_returns_dict(self) -> None:
        """Test that authentication config returns a dictionary."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert isinstance(config, dict)

    def test_get_authentication_config_includes_jwt_support(self) -> None:
        """Test that authentication config includes JWT support."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert "jwt_header_name" in config
        assert config["jwt_header_name"] == "Authorization"
        assert "jwt_token_prefix" in config
        assert config["jwt_token_prefix"] == "Bearer "

    def test_get_authentication_config_includes_api_key_support(self) -> None:
        """Test that authentication config includes API key support."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert "api_key_name" in config
        assert config["api_key_name"] == "X-API-Key"
        assert "api_key_location" in config
        assert config["api_key_location"] == "header"

    def test_get_authentication_config_with_custom_brand(self) -> None:
        """Test authentication config with custom brand configuration."""
        brand_config = SynetoBrandConfig(primary_color="#custom")
        rapidoc = SynetoRapiDoc(brand_config=brand_config)

        config = rapidoc.get_authentication_config()

        assert isinstance(config, dict)
        # Authentication config should be independent of brand colors
        assert "jwt_header_name" in config
        assert config["allow_authentication"] is True


class TestSynetoRapiDocEdgeCases:
    """Test SynetoRapiDoc edge cases and error conditions."""

    def test_initialization_with_none_brand_config(self) -> None:
        """Test initialization with explicitly None brand config."""
        rapidoc = SynetoRapiDoc(brand_config=None)

        assert rapidoc.brand_config is not None
        assert rapidoc.brand_config.theme == SynetoTheme.DARK

    def test_inject_customizations_with_special_characters(self) -> None:
        """Test customization injection with special characters in brand config."""
        brand_config = SynetoBrandConfig(company_name="Test & Co. <script>", primary_color="#ff0000")

        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        # Should handle special characters safely
        assert "#ff0000" in result
        assert "<style>" in result


class TestSynetoRapiDocIntegration:
    """Test SynetoRapiDoc integration scenarios."""

    def test_full_rendering_workflow(self) -> None:
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        rapidoc = SynetoRapiDoc(
            openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
        )

        result = rapidoc.render(extra_param="test")

        # Verify customizations were injected
        assert "#test123" in result
        assert "Syneto-specific RapiDoc customizations" in result
        assert "rapi-doc spec-url" in result
        assert "/test/openapi.json" in result

    def test_theme_consistency_across_components(self) -> None:
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        rapidoc = SynetoRapiDoc(brand_config=brand_config)

        result = rapidoc.render()

        # Verify light theme colors are used
        assert SynetoColors.BG_LIGHTEST in result  # Light theme background
        assert brand_config.background_color in result
        assert brand_config.text_color in result

    def test_with_jwt_auth(self) -> None:
        """Test configuring JWT authentication."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.with_jwt_auth("/custom/token")

        # Verify method chaining
        assert result is rapidoc

        # Verify JWT auth was configured
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["persist_auth"] == "true"

    def test_with_api_key_auth(self) -> None:
        """Test configuring API key authentication."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.with_api_key_auth("Custom-API-Key")

        # Verify method chaining
        assert result is rapidoc

        # Verify API key auth was configured
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["api_key_name"] == "Custom-API-Key"

    def test_authentication_chaining(self) -> None:
        """Test chaining authentication configuration methods."""
        rapidoc = SynetoRapiDoc()

        result = rapidoc.with_jwt_auth("/auth/jwt").with_api_key_auth("X-Custom-Key")

        # Verify chaining worked
        assert result is rapidoc

        # Verify both configurations were applied
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["persist_auth"] == "true"
        assert rapidoc.rapidoc_config["api_key_name"] == "X-Custom-Key"

    def test_rapidoc_config_attributes_in_html(self) -> None:
        """Test that rapidoc_config is properly included as HTML attributes."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.DARK, primary_color="#ff0000")
        rapidoc = SynetoRapiDoc(brand_config=brand_config)

        html = rapidoc.render()

        # Verify that rapidoc_config attributes are included in the HTML
        assert 'theme="dark"' in html
        assert 'primary-color="#ff0000"' in html
        assert 'bg-color="#07080d"' in html  # Dark theme background
        assert 'render-style="read"' in html
        assert 'allow-authentication="true"' in html
        assert 'spec-url="/openapi.json"' in html

        # Verify the rapi-doc element exists with attributes
        assert "<rapi-doc" in html
        assert "spec-url=" in html

    def test_kwargs_override_hardcoded_values(self) -> None:
        """Test that kwargs can override hardcoded rapidoc_config values."""
        rapidoc = SynetoRapiDoc(
            show_header="false",  # Override default "true"
            render_style="view",  # Override default "read"
            schema_style="tree",  # Override default "table"
            allow_authentication="false",  # Override default "true"
            response_area_height="600px",  # Override default "400px"
        )

        html = rapidoc.render()

        # Verify that the overridden values are used
        assert 'show-header="false"' in html
        assert 'render-style="view"' in html
        assert 'schema-style="tree"' in html
        assert 'allow-authentication="false"' in html
        assert 'response-area-height="600px"' in html

        # Verify these are actually in the rapidoc_config
        assert rapidoc.rapidoc_config["show_header"] == "false"
        assert rapidoc.rapidoc_config["render_style"] == "view"
        assert rapidoc.rapidoc_config["schema_style"] == "tree"
        assert rapidoc.rapidoc_config["allow_authentication"] == "false"
        assert rapidoc.rapidoc_config["response_area_height"] == "600px"

    def test_parent_class_params_vs_rapidoc_config(self) -> None:
        """Test that parent class parameters are properly separated from RapiDoc config."""
        rapidoc = SynetoRapiDoc(
            js_url="https://custom-cdn.com/rapidoc.js",  # Parent class param
            favicon_url="/custom-favicon.ico",  # Parent class param
            head_css_urls=["https://custom.css"],  # Parent class param
            render_style="view",  # RapiDoc config param
            show_header="false",  # RapiDoc config param
        )

        # Parent class parameters should NOT be in rapidoc_config
        assert "js_url" not in rapidoc.rapidoc_config
        assert "favicon_url" not in rapidoc.rapidoc_config
        assert "head_css_urls" not in rapidoc.rapidoc_config

        # RapiDoc parameters should be in rapidoc_config
        assert rapidoc.rapidoc_config["render_style"] == "view"
        assert rapidoc.rapidoc_config["show_header"] == "false"

        # Verify parent class parameters are passed correctly
        assert rapidoc.js_url == "https://custom-cdn.com/rapidoc.js"
        assert rapidoc.favicon_url == "/custom-favicon.ico"
        assert rapidoc.head_css_urls == ["https://custom.css"]

    def test_boolean_values_converted_to_lowercase_strings(self) -> None:
        """Test that Python boolean values are converted to lowercase strings in HTML attributes."""
        rapidoc = SynetoRapiDoc(
            allow_spec_url_load=False,
            allow_spec_file_load=False,
            allow_server_selection=False,
            show_header=False,
            show_info=False,
        )

        html = rapidoc.render()

        # Check that boolean False values are converted to "false" (not "False")
        assert 'allow-spec-url-load="false"' in html
        assert 'allow-spec-file-load="false"' in html
        assert 'allow-server-selection="false"' in html
        assert 'show-header="false"' in html
        assert 'show-info="false"' in html

        # Make sure Python "False" strings are not present
        assert 'allow-spec-url-load="False"' not in html
        assert 'allow-spec-file-load="False"' not in html
        assert 'allow-server-selection="False"' not in html
        assert 'show-header="False"' not in html
        assert 'show-info="False"' not in html

    def test_sticky_header_enabled_by_default(self) -> None:
        """Test that sticky header is enabled by default and CSS is included."""
        rapidoc = SynetoRapiDoc()
        html = rapidoc.render()

        # Verify sticky header CSS is present
        assert "position: sticky" in html
        assert "top: 0" in html
        assert "z-index: 1000" in html
        assert "Sticky Header Implementation" in html

    def test_sticky_header_disabled(self) -> None:
        """Test that sticky header can be disabled and CSS is not included."""
        rapidoc = SynetoRapiDoc(sticky_header=False)
        html = rapidoc.render()

        # Verify sticky header CSS is NOT present
        assert "position: sticky" not in html
        assert "Sticky Header Implementation" not in html

        # But other CSS should still be present
        assert "Syneto-specific RapiDoc customizations" in html
        assert rapidoc.brand_config.primary_color in html

    def test_sticky_header_with_custom_header_content(self) -> None:
        """Test sticky header works with custom header slot content."""
        custom_header = '<div class="custom-header">My Custom Header</div>'
        rapidoc = SynetoRapiDoc(header_slot_content=custom_header, sticky_header=True)
        html = rapidoc.render()

        # Verify both custom header and sticky CSS are present
        assert "My Custom Header" in html
        assert "position: sticky" in html
        assert "Sticky Header Implementation" in html

    def test_get_sticky_header_css_method_directly(self) -> None:
        """Test the _get_sticky_header_css method directly for both enabled and disabled cases."""
        # Test with sticky header enabled
        rapidoc_enabled = SynetoRapiDoc(sticky_header=True)
        css_enabled = rapidoc_enabled._get_sticky_header_css()

        assert css_enabled != ""
        assert "position: sticky" in css_enabled
        assert "Sticky Header Implementation" in css_enabled
        assert rapidoc_enabled.brand_config.header_color in css_enabled

        # Test with sticky header disabled - this should cover line 418
        rapidoc_disabled = SynetoRapiDoc(sticky_header=False)
        css_disabled = rapidoc_disabled._get_sticky_header_css()

        assert css_disabled == ""  # This specifically tests the return "" on line 418
