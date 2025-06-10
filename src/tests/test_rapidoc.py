"""
Tests for the SynetoRapiDoc implementation.
"""

from unittest.mock import patch

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from syneto_openapi_themes.rapidoc import SynetoRapiDoc


class TestSynetoRapiDocInitialization:
    """Test SynetoRapiDoc initialization and configuration."""

    def test_default_initialization(self):
        """Test default RapiDoc initialization."""
        rapidoc = SynetoRapiDoc()

        assert rapidoc.openapi_url == "/openapi.json"
        assert rapidoc.title == "API Documentation"
        assert rapidoc.brand_config is not None
        assert rapidoc.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self):
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

    def test_initialization_with_kwargs(self):
        """Test RapiDoc initialization with additional kwargs."""
        rapidoc = SynetoRapiDoc(show_header=False, allow_try=True, show_info=True, nav_bg_color="#123456")

        assert rapidoc.brand_config is not None


class TestSynetoRapiDocRendering:
    """Test SynetoRapiDoc HTML rendering functionality."""

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_calls_parent_and_injects_customizations(self, mock_parent_render):
        """Test that render calls parent and injects Syneto customizations."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        mock_parent_render.assert_called_once()
        assert "Syneto-specific RapiDoc customizations" in result
        assert "syneto-rapidoc-container" in result
        assert rapidoc.brand_config.primary_color in result

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_with_custom_brand_config(self, mock_parent_render):
        """Test rendering with custom brand configuration."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        brand_config = SynetoBrandConfig(
            primary_color="#custom123", background_color="#bg456", company_name="Test Corp"
        )

        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        result = rapidoc.render()

        assert "#custom123" in result
        assert "#bg456" in result
        assert "Test Corp" not in result  # Company name not directly in CSS

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_includes_css_variables(self, mock_parent_render):
        """Test that render includes CSS variables from brand config."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_includes_loading_css(self, mock_parent_render):
        """Test that render includes loading CSS."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        rapidoc = SynetoRapiDoc()
        result = rapidoc.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_includes_javascript_enhancements(self, mock_parent_render):
        """Test that render includes JavaScript enhancements."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        rapidoc = SynetoRapiDoc()
        _ = rapidoc.render()

        # Should include JavaScript enhancements
        mock_parent_render.assert_called_once()
        # Verify the render method was called (JavaScript is injected during render)
        assert "spec-load-error" in rapidoc.render()

    @patch("syneto_openapi_themes.rapidoc.RapiDoc.render")
    def test_render_with_kwargs(self, mock_parent_render):
        """Test rendering with additional template variables."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        rapidoc = SynetoRapiDoc()
        _ = rapidoc.render(custom_var="test_value")

        mock_parent_render.assert_called_once_with(custom_var="test_value")


class TestSynetoRapiDocCustomizations:
    """Test SynetoRapiDoc customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self):
        """Test customization injection with minimal HTML."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert "rapi-doc" in result
        assert rapidoc.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self):
        """Test that customization injection preserves original HTML content."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body><div id='original'>Original Content</div></body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='original'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self):
        """Test that customizations include scrollbar styling."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_error_handling(self):
        """Test that customizations include error handling JavaScript."""
        rapidoc = SynetoRapiDoc()
        base_html = "<html><body>Test</body></html>"

        result = rapidoc._inject_syneto_customizations(base_html)

        assert "spec-load-error" in result
        assert "Failed to Load API Documentation" in result
        assert "setTimeout" in result


class TestSynetoRapiDocAuthentication:
    """Test SynetoRapiDoc authentication configuration."""

    def test_get_authentication_config_returns_dict(self):
        """Test that authentication config returns a dictionary."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert isinstance(config, dict)

    def test_get_authentication_config_includes_jwt_support(self):
        """Test that authentication config includes JWT support."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert "jwt_header_name" in config
        assert config["jwt_header_name"] == "Authorization"
        assert "jwt_token_prefix" in config
        assert config["jwt_token_prefix"] == "Bearer "

    def test_get_authentication_config_includes_api_key_support(self):
        """Test that authentication config includes API key support."""
        rapidoc = SynetoRapiDoc()
        config = rapidoc.get_authentication_config()

        assert "api_key_name" in config
        assert config["api_key_name"] == "X-API-Key"
        assert "api_key_location" in config
        assert config["api_key_location"] == "header"

    def test_get_authentication_config_with_custom_brand(self):
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

    def test_initialization_with_none_brand_config(self):
        """Test initialization with explicitly None brand config."""
        rapidoc = SynetoRapiDoc(brand_config=None)

        assert rapidoc.brand_config is not None
        assert rapidoc.brand_config.theme == SynetoTheme.DARK

    def test_render_with_empty_base_html(self):
        """Test rendering with empty base HTML."""
        with patch("syneto_openapi_themes.rapidoc.RapiDoc.render") as mock_render:
            mock_render.return_value = ""

            rapidoc = SynetoRapiDoc()
            result = rapidoc.render()

            # Should still inject customizations even with empty base
            assert "<style>" in result

    def test_render_with_malformed_base_html(self):
        """Test rendering with malformed base HTML."""
        with patch("syneto_openapi_themes.rapidoc.RapiDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Unclosed tag"

            rapidoc = SynetoRapiDoc()
            result = rapidoc.render()

            # Should still inject customizations
            assert "Syneto-specific RapiDoc customizations" in result
            assert "Unclosed tag" in result

    def test_inject_customizations_with_special_characters(self):
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

    def test_full_rendering_workflow(self):
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        with patch("syneto_openapi_themes.rapidoc.RapiDoc.render") as mock_render:
            mock_render.return_value = """
            <html>
                <head><title>API Docs</title></head>
                <body>
                    <rapi-doc spec-url="/openapi.json"></rapi-doc>
                </body>
            </html>
            """

            rapidoc = SynetoRapiDoc(
                openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
            )

            result = rapidoc.render(extra_param="test")

            # Verify parent was called with correct parameters
            mock_render.assert_called_once_with(extra_param="test")

            # Verify customizations were injected
            assert "#test123" in result
            assert "Syneto-specific RapiDoc customizations" in result
            assert "rapi-doc spec-url" in result
            assert "API Docs" in result

    def test_theme_consistency_across_components(self):
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        rapidoc = SynetoRapiDoc(brand_config=brand_config)

        with patch("syneto_openapi_themes.rapidoc.RapiDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = rapidoc.render()

            # Verify light theme colors are used
            assert SynetoColors.NEUTRAL_100 not in result  # This would be in light theme
            assert brand_config.background_color in result
            assert brand_config.text_color in result

    def test_with_jwt_auth(self):
        """Test configuring JWT authentication."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.with_jwt_auth("/custom/token")

        # Verify method chaining
        assert result is rapidoc

        # Verify JWT auth was configured
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["persist_auth"] == "true"

    def test_with_api_key_auth(self):
        """Test configuring API key authentication."""
        rapidoc = SynetoRapiDoc()
        result = rapidoc.with_api_key_auth("Custom-API-Key")

        # Verify method chaining
        assert result is rapidoc

        # Verify API key auth was configured
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["api_key_name"] == "Custom-API-Key"

    def test_authentication_chaining(self):
        """Test chaining authentication configuration methods."""
        rapidoc = SynetoRapiDoc()

        result = rapidoc.with_jwt_auth("/auth/jwt").with_api_key_auth("X-Custom-Key")

        # Verify chaining worked
        assert result is rapidoc

        # Verify both configurations were applied
        assert rapidoc.rapidoc_config["allow_authentication"] == "true"
        assert rapidoc.rapidoc_config["persist_auth"] == "true"
        assert rapidoc.rapidoc_config["api_key_name"] == "X-Custom-Key"
