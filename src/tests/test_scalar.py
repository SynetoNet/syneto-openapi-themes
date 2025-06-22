"""
Tests for the SynetoScalar implementation.
"""

from unittest.mock import Mock, patch

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from syneto_openapi_themes.scalar import SynetoScalar


class TestSynetoScalarInitialization:
    """Test SynetoScalar initialization and configuration."""

    def test_default_initialization(self) -> None:
        """Test default Scalar initialization."""
        scalar = SynetoScalar()

        assert scalar.openapi_url == "/openapi.json"
        assert scalar.title == "API Documentation"
        assert scalar.brand_config is not None
        assert scalar.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self) -> None:
        """Test Scalar initialization with custom parameters."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT, company_name="Custom Corp", primary_color="#ff0000")

        scalar = SynetoScalar(
            openapi_url="/custom/openapi.json",
            title="Custom API Docs",
            brand_config=brand_config,
            show_sidebar=False,
            hide_download_button=True,
        )

        assert scalar.openapi_url == "/custom/openapi.json"
        assert scalar.title == "Custom API Docs"
        assert scalar.brand_config.company_name == "Custom Corp"
        assert scalar.brand_config.primary_color == "#ff0000"

    def test_initialization_with_none_brand_config(self) -> None:
        """Test initialization with explicitly None brand config."""
        scalar = SynetoScalar(brand_config=None)

        assert scalar.brand_config is not None
        assert scalar.brand_config.theme == SynetoTheme.DARK


class TestSynetoScalarRendering:
    """Test SynetoScalar HTML rendering functionality."""

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_calls_parent_and_injects_customizations(self, mock_parent_render: Mock) -> None:
        """Test that render calls parent and injects Syneto customizations."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        result = scalar.render()

        mock_parent_render.assert_called_once()
        assert "Syneto Scalar Theme" in result
        assert "syneto-scalar-container" in result
        assert scalar.brand_config.primary_color in result

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_with_custom_brand_config(self, mock_parent_render: Mock) -> None:
        """Test rendering with custom brand configuration."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        brand_config = SynetoBrandConfig(primary_color="#custom123", background_color="#bg456", nav_bg_color="#nav789")

        scalar = SynetoScalar(brand_config=brand_config)
        result = scalar.render()

        assert "#custom123" in result
        assert "#bg456" in result
        assert "#nav789" in result

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_includes_css_variables(self, mock_parent_render: Mock) -> None:
        """Test that render includes CSS variables from brand config."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        result = scalar.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_includes_loading_css(self, mock_parent_render: Mock) -> None:
        """Test that render includes loading CSS."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        result = scalar.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_includes_scalar_specific_styling(self, mock_parent_render: Mock) -> None:
        """Test that render includes Scalar-specific styling."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        result = scalar.render()

        assert ".scalar-app" in result
        assert ".scalar-sidebar" in result
        assert ".scalar-content" in result
        assert ".scalar-method" in result

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_includes_javascript_enhancements(self, mock_parent_render: Mock) -> None:
        """Test that render includes JavaScript enhancements."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        _ = scalar.render()

        # Should include JavaScript enhancements
        mock_parent_render.assert_called_once()
        # Verify the render method was called (JavaScript is injected during render)
        assert "scalar-container" in scalar.render()

    @patch("syneto_openapi_themes.scalar.Scalar.render")
    def test_render_with_kwargs(self, mock_parent_render: Mock) -> None:
        """Test rendering with additional template variables."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        scalar = SynetoScalar()
        _ = scalar.render(custom_var="test_value")

        mock_parent_render.assert_called_once_with(custom_var="test_value")


class TestSynetoScalarCustomizations:
    """Test SynetoScalar customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self) -> None:
        """Test customization injection with minimal HTML."""
        scalar = SynetoScalar()
        base_html = "<html><body>Test</body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert ".scalar-app" in result
        assert scalar.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self) -> None:
        """Test that customization injection preserves original HTML content."""
        scalar = SynetoScalar()
        base_html = "<html><body><div id='scalar-container'>Original Content</div></body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='scalar-container'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self) -> None:
        """Test that customizations include scrollbar styling."""
        scalar = SynetoScalar()
        base_html = "<html><body>Test</body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_method_styling(self) -> None:
        """Test that customizations include HTTP method styling."""
        scalar = SynetoScalar()
        base_html = "<html><body>Test</body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        assert ".scalar-method-post" in result
        assert ".scalar-method-get" in result
        assert ".scalar-method-put" in result
        assert ".scalar-method-delete" in result

    def test_inject_syneto_customizations_includes_error_handling(self) -> None:
        """Test that customizations include error handling JavaScript."""
        scalar = SynetoScalar()
        base_html = "<html><body>Test</body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        assert "addEventListener" in result
        assert "Failed to Load API Documentation" in result
        assert "setTimeout" in result


class TestSynetoScalarEdgeCases:
    """Test SynetoScalar edge cases and error conditions."""

    def test_render_with_empty_base_html(self) -> None:
        """Test rendering with empty base HTML."""
        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = ""

            scalar = SynetoScalar()
            result = scalar.render()

            # Should still inject customizations even with empty base
            assert "<style>" in result

    def test_render_with_malformed_base_html(self) -> None:
        """Test rendering with malformed base HTML."""
        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Unclosed tag"

            scalar = SynetoScalar()
            result = scalar.render()

            # Should still inject customizations
            assert "Syneto Scalar Theme" in result
            assert "Unclosed tag" in result

    def test_inject_customizations_with_special_characters(self) -> None:
        """Test customization injection with special characters in brand config."""
        brand_config = SynetoBrandConfig(company_name="Test & Co. <script>", primary_color="#ff0000")

        scalar = SynetoScalar(brand_config=brand_config)
        base_html = "<html><body>Test</body></html>"

        result = scalar._inject_syneto_customizations(base_html)

        # Should handle special characters safely
        assert "#ff0000" in result
        assert "<style>" in result


class TestSynetoScalarIntegration:
    """Test SynetoScalar integration scenarios."""

    def test_full_rendering_workflow(self) -> None:
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = """
            <html>
                <head><title>API Docs</title></head>
                <body>
                    <div id="scalar-container"></div>
                    <script>
                        createApiReference({
                            spec: { url: '/openapi.json' }
                        }, document.getElementById('scalar-container'));
                    </script>
                </body>
            </html>
            """

            scalar = SynetoScalar(
                openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
            )

            result = scalar.render(extra_param="test")

            # Verify parent was called with correct parameters
            mock_render.assert_called_once_with(extra_param="test")

            # Verify customizations were injected
            assert "#test123" in result
            assert "Syneto Scalar Theme" in result
            assert "scalar-container" in result
            assert "API Docs" in result

    def test_theme_consistency_across_components(self) -> None:
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        scalar = SynetoScalar(brand_config=brand_config)

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            # Verify theme colors are used consistently
            assert brand_config.background_color in result
            assert brand_config.text_color in result
            assert brand_config.primary_color in result

    def test_sidebar_styling(self) -> None:
        """Test that sidebar elements are properly styled."""
        scalar = SynetoScalar()

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            assert ".scalar-sidebar" in result
            assert ".scalar-content" in result
            assert "background-color" in result
            assert "border-color" in result

    def test_method_badge_colors(self) -> None:
        """Test that HTTP method badges have correct colors."""
        scalar = SynetoScalar()

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            # Check that different methods have different styling
            assert ".scalar-method-post" in result
            assert ".scalar-method-get" in result
            assert ".scalar-method-put" in result
            assert ".scalar-method-delete" in result
            assert "#f01932" in result  # Delete method color

    def test_dark_theme_specific_styling(self) -> None:
        """Test dark theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.DARK)
        scalar = SynetoScalar(brand_config=brand_config)

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            # Verify dark theme colors
            assert SynetoColors.PRIMARY_DARK in result
            assert SynetoColors.PRIMARY_LIGHT in result  # Text color for dark theme

    def test_light_theme_specific_styling(self) -> None:
        """Test light theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        scalar = SynetoScalar(brand_config=brand_config)

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            # Verify light theme colors are applied
            assert brand_config.background_color in result
            assert brand_config.text_color in result

    def test_interactive_features_styling(self) -> None:
        """Test that interactive features are properly styled."""
        scalar = SynetoScalar()

        with patch("syneto_openapi_themes.scalar.Scalar.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = scalar.render()

            # Check for interactive elements styling
            assert "button" in result
            assert "hover" in result
            assert "addEventListener" in result
            assert "keydown" in result

    def test_get_configuration(self) -> None:
        """Test getting Scalar configuration."""
        scalar = SynetoScalar()
        config = scalar.get_configuration()

        assert isinstance(config, dict)
        assert "layout" in config
        assert "theme" in config
        assert "showSidebar" in config
        assert "hideModels" in config
        assert "hideDownloadButton" in config
        assert "darkMode" in config
        assert "searchHotKey" in config

    def test_with_modern_layout(self) -> None:
        """Test configuring modern layout."""
        scalar = SynetoScalar()
        result = scalar.with_modern_layout()

        # Verify method chaining
        assert result is scalar

        # Verify layout was set
        assert scalar.scalar_config["layout"] == "modern"

    def test_with_classic_layout(self) -> None:
        """Test configuring classic layout."""
        scalar = SynetoScalar()
        result = scalar.with_classic_layout()

        # Verify method chaining
        assert result is scalar

        # Verify layout was set
        assert scalar.scalar_config["layout"] == "classic"

    def test_with_sidebar_hidden(self) -> None:
        """Test hiding the sidebar."""
        scalar = SynetoScalar()
        result = scalar.with_sidebar_hidden()

        # Verify method chaining
        assert result is scalar

        # Verify sidebar was hidden
        assert scalar.scalar_config["showSidebar"] is False

    def test_with_models_hidden(self) -> None:
        """Test hiding the models section."""
        scalar = SynetoScalar()
        result = scalar.with_models_hidden()

        # Verify method chaining
        assert result is scalar

        # Verify models were hidden
        assert scalar.scalar_config["hideModels"] is True

    def test_configuration_chaining(self) -> None:
        """Test chaining configuration methods."""
        scalar = SynetoScalar()

        result = scalar.with_classic_layout().with_sidebar_hidden().with_models_hidden()

        # Verify chaining worked
        assert result is scalar

        # Verify all configurations were applied
        assert scalar.scalar_config["layout"] == "classic"
        assert scalar.scalar_config["showSidebar"] is False
        assert scalar.scalar_config["hideModels"] is True
