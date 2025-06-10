"""
Tests for the SynetoSwaggerUI implementation.
"""

from unittest.mock import patch

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoTheme
from syneto_openapi_themes.swagger import SynetoSwaggerUI


class TestSynetoSwaggerUIInitialization:
    """Test SynetoSwaggerUI initialization and configuration."""

    def test_default_initialization(self):
        """Test default SwaggerUI initialization."""
        swagger = SynetoSwaggerUI()

        assert swagger.openapi_url == "/openapi.json"
        assert swagger.title == "API Documentation"
        assert swagger.brand_config is not None
        assert swagger.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self):
        """Test SwaggerUI initialization with custom parameters."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT, company_name="Custom Corp", primary_color="#ff0000")

        swagger = SynetoSwaggerUI(
            openapi_url="/custom/openapi.json",
            title="Custom API Docs",
            brand_config=brand_config,
            deepLinking=True,
            displayRequestDuration=True,
        )

        assert swagger.openapi_url == "/custom/openapi.json"
        assert swagger.title == "Custom API Docs"
        assert swagger.brand_config.company_name == "Custom Corp"
        assert swagger.brand_config.primary_color == "#ff0000"

    def test_initialization_with_none_brand_config(self):
        """Test initialization with explicitly None brand config."""
        swagger = SynetoSwaggerUI(brand_config=None)

        assert swagger.brand_config is not None
        assert swagger.brand_config.theme == SynetoTheme.DARK


class TestSynetoSwaggerUIRendering:
    """Test SynetoSwaggerUI HTML rendering functionality."""

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_calls_parent_and_injects_customizations(self, mock_parent_render):
        """Test that render calls parent and injects Syneto customizations."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        result = swagger.render()

        mock_parent_render.assert_called_once()
        assert "Syneto SwaggerUI Theme" in result
        assert "syneto-swagger-container" in result
        assert swagger.brand_config.primary_color in result

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_with_custom_brand_config(self, mock_parent_render):
        """Test rendering with custom brand configuration."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        brand_config = SynetoBrandConfig(primary_color="#custom123", background_color="#bg456", nav_bg_color="#nav789")

        swagger = SynetoSwaggerUI(brand_config=brand_config)
        result = swagger.render()

        assert "#custom123" in result
        assert "#bg456" in result
        assert "#nav789" in result

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_includes_css_variables(self, mock_parent_render):
        """Test that render includes CSS variables from brand config."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        result = swagger.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_includes_loading_css(self, mock_parent_render):
        """Test that render includes loading CSS."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        result = swagger.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_includes_swagger_specific_styling(self, mock_parent_render):
        """Test that render includes SwaggerUI-specific styling."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        result = swagger.render()

        assert ".swagger-ui .topbar" in result
        assert ".swagger-ui .opblock" in result
        assert ".swagger-ui .btn.authorize" in result
        assert ".swagger-ui .btn.execute" in result

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_includes_javascript_enhancements(self, mock_parent_render):
        """Test that render includes JavaScript enhancements."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        _ = swagger.render()

        # Should include JavaScript enhancements
        mock_parent_render.assert_called_once()
        # Verify the render method was called (JavaScript is injected during render)
        assert "swagger-ui" in swagger.render()

    @patch("syneto_openapi_themes.swagger.SwaggerUI.render")
    def test_render_with_kwargs(self, mock_parent_render):
        """Test rendering with additional template variables."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        swagger = SynetoSwaggerUI()
        _ = swagger.render(custom_var="test_value")

        mock_parent_render.assert_called_once_with(custom_var="test_value")


class TestSynetoSwaggerUICustomizations:
    """Test SynetoSwaggerUI customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self):
        """Test customization injection with minimal HTML."""
        swagger = SynetoSwaggerUI()
        base_html = "<html><body>Test</body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert ".swagger-ui" in result
        assert swagger.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self):
        """Test that customization injection preserves original HTML content."""
        swagger = SynetoSwaggerUI()
        base_html = "<html><body><div id='swagger-ui'>Original Content</div></body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='swagger-ui'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self):
        """Test that customizations include scrollbar styling."""
        swagger = SynetoSwaggerUI()
        base_html = "<html><body>Test</body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_method_styling(self):
        """Test that customizations include HTTP method styling."""
        swagger = SynetoSwaggerUI()
        base_html = "<html><body>Test</body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        assert ".opblock-post" in result
        assert ".opblock-get" in result
        assert ".opblock-put" in result
        assert ".opblock-delete" in result

    def test_inject_syneto_customizations_includes_error_handling(self):
        """Test that customizations include error handling JavaScript."""
        swagger = SynetoSwaggerUI()
        base_html = "<html><body>Test</body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        assert "addEventListener" in result
        assert "Failed to Load API Documentation" in result
        assert "setTimeout" in result


class TestSynetoSwaggerUIEdgeCases:
    """Test SynetoSwaggerUI edge cases and error conditions."""

    def test_render_with_empty_base_html(self):
        """Test rendering with empty base HTML."""
        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = ""

            swagger = SynetoSwaggerUI()
            result = swagger.render()

            # Should still inject customizations even with empty base
            assert "<style>" in result

    def test_render_with_malformed_base_html(self):
        """Test rendering with malformed base HTML."""
        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = "<html><body>Unclosed tag"

            swagger = SynetoSwaggerUI()
            result = swagger.render()

            # Should still inject customizations
            assert "Syneto SwaggerUI Theme" in result
            assert "Unclosed tag" in result

    def test_inject_customizations_with_special_characters(self):
        """Test customization injection with special characters in brand config."""
        brand_config = SynetoBrandConfig(company_name="Test & Co. <script>", primary_color="#ff0000")

        swagger = SynetoSwaggerUI(brand_config=brand_config)
        base_html = "<html><body>Test</body></html>"

        result = swagger._inject_syneto_customizations(base_html)

        # Should handle special characters safely
        assert "#ff0000" in result
        assert "<style>" in result


class TestSynetoSwaggerUIIntegration:
    """Test SynetoSwaggerUI integration scenarios."""

    def test_full_rendering_workflow(self):
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = """
            <html>
                <head><title>API Docs</title></head>
                <body>
                    <div id="swagger-ui"></div>
                    <script>
                        SwaggerUIBundle({
                            url: '/openapi.json'
                        });
                    </script>
                </body>
            </html>
            """

            swagger = SynetoSwaggerUI(
                openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
            )

            result = swagger.render(extra_param="test")

            # Verify parent was called with correct parameters
            mock_render.assert_called_once_with(extra_param="test")

            # Verify customizations were injected
            assert "#test123" in result
            assert "Syneto SwaggerUI Theme" in result
            assert "swagger-ui" in result
            assert "API Docs" in result

    def test_theme_consistency_across_components(self):
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        swagger = SynetoSwaggerUI(brand_config=brand_config)

        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = swagger.render()

            # Verify theme colors are used consistently
            assert brand_config.background_color in result
            assert brand_config.text_color in result
            assert brand_config.primary_color in result

    def test_authorization_button_styling(self):
        """Test that authorization buttons are properly styled."""
        swagger = SynetoSwaggerUI()

        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = swagger.render()

            assert ".btn.authorize" in result
            assert ".btn.execute" in result
            assert "background-color" in result
            assert "border-color" in result

    def test_method_badge_colors(self):
        """Test that HTTP method badges have correct colors."""
        swagger = SynetoSwaggerUI()

        with patch("syneto_openapi_themes.swagger.SwaggerUI.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = swagger.render()

            # Check that different methods have different styling
            assert ".opblock-post" in result
            assert ".opblock-get" in result
            assert ".opblock-put" in result
            assert ".opblock-delete" in result
            assert "#f01932" in result  # Delete method color

    def test_get_oauth_config(self):
        """Test getting OAuth configuration."""
        swagger = SynetoSwaggerUI()
        config = swagger.get_oauth_config()

        assert isinstance(config, dict)
        assert "clientId" in config
        assert "realm" in config
        assert "appName" in config
        assert "scopeSeparator" in config
        assert "scopes" in config
        assert "additionalQueryStringParams" in config
        assert "useBasicAuthenticationWithAccessCodeGrant" in config

    def test_with_oauth2(self):
        """Test configuring OAuth2 authentication."""
        swagger = SynetoSwaggerUI()
        result = swagger.with_oauth2("custom-client", "custom-realm", ["read", "write", "admin"])

        # Verify method chaining
        assert result is swagger

        # Verify OAuth2 was configured
        assert "initOAuth" in swagger.swagger_config
        oauth_config = swagger.swagger_config["initOAuth"]
        assert oauth_config["clientId"] == "custom-client"
        assert oauth_config["realm"] == "custom-realm"
        assert oauth_config["scopes"] == ["read", "write", "admin"]

    def test_with_api_key_auth(self):
        """Test configuring API key authentication."""
        swagger = SynetoSwaggerUI()
        result = swagger.with_api_key_auth("Custom-API-Key")

        # Verify method chaining
        assert result is swagger

        # Verify API key auth preferences were set
        assert swagger.swagger_config["persistAuthorization"] is True
        assert swagger.swagger_config["tryItOutEnabled"] is True

    def test_authentication_chaining(self):
        """Test chaining authentication configuration methods."""
        swagger = SynetoSwaggerUI()

        result = swagger.with_oauth2("chained-client", "chained-realm").with_api_key_auth("X-Chained-Key")

        # Verify chaining worked
        assert result is swagger

        # Verify both configurations were applied
        assert "initOAuth" in swagger.swagger_config
        assert swagger.swagger_config["persistAuthorization"] is True
        assert swagger.swagger_config["tryItOutEnabled"] is True
