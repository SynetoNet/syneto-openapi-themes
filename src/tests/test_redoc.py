"""
Tests for the SynetoRedoc implementation.
"""

from unittest.mock import Mock, patch

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from syneto_openapi_themes.redoc import SynetoReDoc


class TestSynetoRedocInitialization:
    """Test SynetoReDoc initialization and configuration."""

    def test_default_initialization(self) -> None:
        """Test default Redoc initialization."""
        redoc = SynetoReDoc()

        assert redoc.openapi_url == "/openapi.json"
        assert redoc.title == "API Documentation"
        assert redoc.brand_config is not None
        assert redoc.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self) -> None:
        """Test Redoc initialization with custom parameters."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT, company_name="Custom Corp", primary_color="#ff0000")

        redoc = SynetoReDoc(
            openapi_url="/custom/openapi.json",
            title="Custom API Docs",
            brand_config=brand_config,
            hide_download_button=True,
            expand_responses="200,201",
        )

        assert redoc.openapi_url == "/custom/openapi.json"
        assert redoc.title == "Custom API Docs"
        assert redoc.brand_config.company_name == "Custom Corp"
        assert redoc.brand_config.primary_color == "#ff0000"

    def test_initialization_with_none_brand_config(self) -> None:
        """Test initialization with explicitly None brand config."""
        redoc = SynetoReDoc(brand_config=None)

        assert redoc.brand_config is not None
        assert redoc.brand_config.theme == SynetoTheme.DARK


class TestSynetoRedocRendering:
    """Test SynetoRedoc HTML rendering functionality."""

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_calls_parent_and_injects_customizations(self, mock_parent_render: Mock) -> None:
        """Test that render calls parent and injects Syneto customizations."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        result = redoc.render()

        mock_parent_render.assert_called_once()
        assert "Syneto ReDoc Theme" in result
        assert "syneto-redoc-container" in result
        assert redoc.brand_config.primary_color in result

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_with_custom_brand_config(self, mock_parent_render: Mock) -> None:
        """Test rendering with custom brand configuration."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        brand_config = SynetoBrandConfig(primary_color="#custom123", background_color="#bg456", nav_bg_color="#nav789")

        redoc = SynetoReDoc(brand_config=brand_config)
        result = redoc.render()

        assert "#custom123" in result
        assert "#bg456" in result
        assert "#nav789" in result

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_includes_css_variables(self, mock_parent_render: Mock) -> None:
        """Test that render includes CSS variables from brand config."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        result = redoc.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_includes_loading_css(self, mock_parent_render: Mock) -> None:
        """Test that render includes loading CSS."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        result = redoc.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_includes_redoc_specific_styling(self, mock_parent_render: Mock) -> None:
        """Test that render includes Redoc-specific styling."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        result = redoc.render()

        assert ".redoc-wrap" in result
        assert ".menu-content" in result
        assert ".api-content" in result
        assert ".operation-type" in result

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_includes_javascript_enhancements(self, mock_parent_render: Mock) -> None:
        """Test that render includes JavaScript enhancements."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        _ = redoc.render()

        # Should include JavaScript enhancements
        mock_parent_render.assert_called_once()
        # Verify the render method was called (JavaScript is injected during render)
        assert "redoc-container" in redoc.render()

    @patch("syneto_openapi_themes.redoc.ReDoc.render")
    def test_render_with_kwargs(self, mock_parent_render: Mock) -> None:
        """Test rendering with additional template variables."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        redoc = SynetoReDoc()
        _ = redoc.render(custom_var="test_value")

        mock_parent_render.assert_called_once_with(custom_var="test_value")


class TestSynetoRedocCustomizations:
    """Test SynetoRedoc customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self) -> None:
        """Test customization injection with minimal HTML."""
        redoc = SynetoReDoc()
        base_html = "<html><body>Test</body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert ".redoc-wrap" in result
        assert redoc.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self) -> None:
        """Test that customization injection preserves original HTML content."""
        redoc = SynetoReDoc()
        base_html = "<html><body><div id='redoc-container'>Original Content</div></body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='redoc-container'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self) -> None:
        """Test that customizations include scrollbar styling."""
        redoc = SynetoReDoc()
        base_html = "<html><body>Test</body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_method_styling(self) -> None:
        """Test that customizations include HTTP method styling."""
        redoc = SynetoReDoc()
        base_html = "<html><body>Test</body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        assert ".operation-type.post" in result
        assert ".operation-type.get" in result
        assert ".operation-type.put" in result
        assert ".operation-type.delete" in result

    def test_inject_syneto_customizations_includes_error_handling(self) -> None:
        """Test that customizations include error handling JavaScript."""
        redoc = SynetoReDoc()
        base_html = "<html><body>Test</body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        assert "addEventListener" in result
        assert "Failed to Load API Documentation" in result
        assert "setTimeout" in result


class TestSynetoRedocEdgeCases:
    """Test SynetoRedoc edge cases and error conditions."""

    def test_render_with_empty_base_html(self) -> None:
        """Test rendering with empty base HTML."""
        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = ""

            redoc = SynetoReDoc()
            result = redoc.render()

            # Should still inject customizations even with empty base
            assert "<style>" in result

    def test_render_with_malformed_base_html(self) -> None:
        """Test rendering with malformed base HTML."""
        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Unclosed tag"

            redoc = SynetoReDoc()
            result = redoc.render()

            # Should still inject customizations
            assert "Syneto ReDoc Theme" in result
            assert "Unclosed tag" in result

    def test_inject_customizations_with_special_characters(self) -> None:
        """Test customization injection with special characters in brand config."""
        brand_config = SynetoBrandConfig(company_name="Test & Co. <script>", primary_color="#ff0000")

        redoc = SynetoReDoc(brand_config=brand_config)
        base_html = "<html><body>Test</body></html>"

        result = redoc._inject_syneto_customizations(base_html)

        # Should handle special characters safely
        assert "#ff0000" in result
        assert "<style>" in result


class TestSynetoRedocIntegration:
    """Test SynetoRedoc integration scenarios."""

    def test_full_rendering_workflow(self) -> None:
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = """
            <html>
                <head><title>API Docs</title></head>
                <body>
                    <div id="redoc-container"></div>
                    <script>
                        Redoc.init('/openapi.json', {}, document.getElementById('redoc-container'));
                    </script>
                </body>
            </html>
            """

            redoc = SynetoReDoc(
                openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
            )

            result = redoc.render(extra_param="test")

            # Verify parent was called with correct parameters
            mock_render.assert_called_once_with(extra_param="test")

            # Verify customizations were injected
            assert "#test123" in result
            assert "Syneto ReDoc Theme" in result
            assert "redoc-container" in result
            assert "API Docs" in result

    def test_theme_consistency_across_components(self) -> None:
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        redoc = SynetoReDoc(brand_config=brand_config)

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = redoc.render()

            # Verify theme colors are used consistently
            assert brand_config.background_color in result
            assert brand_config.text_color in result
            assert brand_config.primary_color in result

    def test_navigation_styling(self) -> None:
        """Test that navigation elements are properly styled."""
        redoc = SynetoReDoc()

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = redoc.render()

            assert ".menu-content" in result
            assert ".api-content" in result
            assert "background-color" in result

    def test_method_badge_colors(self) -> None:
        """Test that HTTP method badges have correct colors."""
        redoc = SynetoReDoc()

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = redoc.render()

            # Check that different methods have different styling
            assert ".operation-type.post" in result
            assert ".operation-type.get" in result
            assert ".operation-type.put" in result
            assert ".operation-type.delete" in result
            assert "#f01932" in result  # Delete method color

    def test_dark_theme_specific_styling(self) -> None:
        """Test dark theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.DARK)
        redoc = SynetoReDoc(brand_config=brand_config)

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = redoc.render()

            # Verify dark theme colors
            assert SynetoColors.PRIMARY_DARK in result
            assert SynetoColors.PRIMARY_LIGHT in result  # Text color for dark theme

    def test_light_theme_specific_styling(self) -> None:
        """Test light theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        redoc = SynetoReDoc(brand_config=brand_config)

        with patch("syneto_openapi_themes.redoc.ReDoc.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = redoc.render()

            # Verify light theme colors are applied
            assert brand_config.background_color in result
            assert brand_config.text_color in result

    def test_get_theme_config(self) -> None:
        """Test getting theme configuration."""
        redoc = SynetoReDoc()
        config = redoc.get_theme_config()

        assert isinstance(config, dict)
        assert "colors" in config
        assert "typography" in config
        assert "sidebar" in config
        assert "rightPanel" in config

        # Verify nested structure
        assert "primary" in config["colors"]
        assert "text" in config["colors"]
        assert "background" in config["colors"]

    def test_with_custom_theme(self) -> None:
        """Test applying custom theme configuration."""
        redoc = SynetoReDoc()
        custom_theme = {"colors": {"primary": {"main": "#custom123"}}}

        result = redoc.with_custom_theme(custom_theme)

        # Verify method chaining
        assert result is redoc

        # Verify custom theme was applied
        assert redoc.redoc_config["theme"]["colors"]["primary"]["main"] == "#custom123"

    def test_with_search_disabled(self) -> None:
        """Test disabling search functionality."""
        redoc = SynetoReDoc()
        result = redoc.with_search_disabled()

        # Verify method chaining
        assert result is redoc

        # Verify search was disabled
        assert redoc.redoc_config["disableSearch"] is True

    def test_theme_configuration_chaining(self) -> None:
        """Test chaining theme configuration methods."""
        redoc = SynetoReDoc()
        custom_theme = {"colors": {"primary": {"main": "#chained123"}}}

        result = redoc.with_custom_theme(custom_theme).with_search_disabled()

        # Verify chaining worked
        assert result is redoc

        # Verify both configurations were applied
        assert redoc.redoc_config["theme"]["colors"]["primary"]["main"] == "#chained123"
        assert redoc.redoc_config["disableSearch"] is True
