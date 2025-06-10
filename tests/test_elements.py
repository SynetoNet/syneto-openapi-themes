"""
Tests for the elements module.
"""

from unittest.mock import patch

from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoColors, SynetoTheme
from syneto_openapi_themes.elements import SynetoElements


class TestSynetoElementsInitialization:
    """Test SynetoElements initialization and configuration."""

    def test_default_initialization(self):
        """Test default Elements initialization."""
        elements = SynetoElements()

        assert elements.openapi_url == "/openapi.json"
        assert elements.title == "API Documentation"
        assert elements.brand_config is not None
        assert elements.brand_config.theme == SynetoTheme.DARK

    def test_custom_initialization(self):
        """Test Elements initialization with custom parameters."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT, company_name="Custom Corp", primary_color="#ff0000")

        elements = SynetoElements(
            openapi_url="/custom/openapi.json",
            title="Custom API Docs",
            brand_config=brand_config,
            layout="stacked",
            hideInternal=True,
        )

        assert elements.openapi_url == "/custom/openapi.json"
        assert elements.title == "Custom API Docs"
        assert elements.brand_config.company_name == "Custom Corp"
        assert elements.brand_config.primary_color == "#ff0000"

    def test_initialization_with_none_brand_config(self):
        """Test initialization with explicitly None brand config."""
        elements = SynetoElements(brand_config=None)

        assert elements.brand_config is not None
        assert elements.brand_config.theme == SynetoTheme.DARK


class TestSynetoElementsRendering:
    """Test SynetoElements HTML rendering functionality."""

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_calls_parent_and_injects_customizations(self, mock_parent_render):
        """Test that render calls parent and injects Syneto customizations."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        result = elements.render()

        mock_parent_render.assert_called_once()
        assert "Syneto Elements Theme" in result
        assert "syneto-elements-container" in result
        assert elements.brand_config.primary_color in result

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_with_custom_brand_config(self, mock_parent_render):
        """Test rendering with custom brand configuration."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        brand_config = SynetoBrandConfig(primary_color="#custom123", background_color="#bg456", nav_bg_color="#nav789")

        elements = SynetoElements(brand_config=brand_config)
        result = elements.render()

        assert "#custom123" in result
        assert "#bg456" in result
        assert "#nav789" in result

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_includes_css_variables(self, mock_parent_render):
        """Test that render includes CSS variables from brand config."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        result = elements.render()

        assert "--syneto-primary-color" in result
        assert "--syneto-bg-color" in result
        assert ":root" in result

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_includes_loading_css(self, mock_parent_render):
        """Test that render includes loading CSS."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        result = elements.render()

        assert ".syneto-loading" in result
        assert ".syneto-error" in result
        assert "@keyframes syneto-spin" in result

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_includes_elements_specific_styling(self, mock_parent_render):
        """Test that render includes Elements-specific styling."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        result = elements.render()

        # Should include Elements-specific CSS classes
        assert ".sl-elements-sidebar" in result
        assert ".sl-button--primary" in result

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_includes_javascript_enhancements(self, mock_parent_render):
        """Test that render includes JavaScript enhancements."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        _ = elements.render()

        # Should include JavaScript enhancements
        mock_parent_render.assert_called_once()
        # Verify the render method was called (JavaScript is injected during render)
        assert "checkElements" in elements.render()

    @patch("syneto_openapi_themes.elements.Elements.render")
    def test_render_with_kwargs(self, mock_parent_render):
        """Test rendering with additional template variables."""
        mock_parent_render.return_value = "<html><head></head><body>Base HTML</body></html>"

        elements = SynetoElements()
        _ = elements.render(custom_var="test_value")

        mock_parent_render.assert_called_once_with(custom_var="test_value")


class TestSynetoElementsCustomizations:
    """Test SynetoElements customization injection."""

    def test_inject_syneto_customizations_with_minimal_html(self):
        """Test customization injection with minimal HTML."""
        elements = SynetoElements()
        base_html = "<html><body>Test</body></html>"

        result = elements._inject_syneto_customizations(base_html)

        assert "<style>" in result
        assert ".sl-elements" in result
        assert elements.brand_config.primary_color in result

    def test_inject_syneto_customizations_preserves_original_content(self):
        """Test that customization injection preserves original HTML content."""
        elements = SynetoElements()
        base_html = "<html><body><div id='elements-container'>Original Content</div></body></html>"

        result = elements._inject_syneto_customizations(base_html)

        assert "Original Content" in result
        assert "<div id='elements-container'>" in result

    def test_inject_syneto_customizations_includes_scrollbar_styling(self):
        """Test that customizations include scrollbar styling."""
        elements = SynetoElements()
        base_html = "<html><body>Test</body></html>"

        result = elements._inject_syneto_customizations(base_html)

        assert "::-webkit-scrollbar" in result
        assert "::-webkit-scrollbar-thumb" in result
        assert "::-webkit-scrollbar-track" in result

    def test_inject_syneto_customizations_includes_color_variables(self):
        """Test that customizations include color variables."""
        elements = SynetoElements()
        base_html = "<html><body>Test</body></html>"

        result = elements._inject_syneto_customizations(base_html)

        assert "--color-primary" in result
        assert "--color-success" in result
        assert "--color-warning" in result
        assert "--color-danger" in result

    def test_inject_syneto_customizations_includes_error_handling(self):
        """Test that customizations include error handling JavaScript."""
        elements = SynetoElements()
        base_html = "<html><body>Test</body></html>"

        result = elements._inject_syneto_customizations(base_html)

        assert "Loading Timeout" in result
        assert "setTimeout" in result


class TestSynetoElementsEdgeCases:
    """Test SynetoElements edge cases and error conditions."""

    def test_render_with_empty_base_html(self):
        """Test rendering with empty base HTML."""
        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = ""

            elements = SynetoElements()
            result = elements.render()

            # Should still inject customizations even with empty base
            assert "<style>" in result

    def test_render_with_malformed_base_html(self):
        """Test rendering with malformed base HTML."""
        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Unclosed tag"

            elements = SynetoElements()
            result = elements.render()

            # Should still inject customizations
            assert "Syneto Elements Theme" in result
            assert "Unclosed tag" in result

    def test_inject_customizations_with_special_characters(self):
        """Test customization injection with special characters in brand config."""
        brand_config = SynetoBrandConfig(company_name="Test & Co. <script>", primary_color="#ff0000")

        elements = SynetoElements(brand_config=brand_config)
        base_html = "<html><body>Test</body></html>"

        result = elements._inject_syneto_customizations(base_html)

        # Should handle special characters safely
        assert "#ff0000" in result
        assert "<style>" in result


class TestSynetoElementsIntegration:
    """Test SynetoElements integration scenarios."""

    def test_full_rendering_workflow(self):
        """Test complete rendering workflow from initialization to final HTML."""
        brand_config = SynetoBrandConfig(
            theme=SynetoTheme.LIGHT, primary_color="#test123", company_name="Integration Test Corp"
        )

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = """
            <html>
                <head><title>API Docs</title></head>
                <body>
                    <div class="sl-elements"></div>
                </body>
            </html>
            """

            elements = SynetoElements(
                openapi_url="/test/openapi.json", title="Integration Test API", brand_config=brand_config
            )

            result = elements.render(extra_param="test")

            # Verify parent was called with correct parameters
            mock_render.assert_called_once_with(extra_param="test")

            # Verify customizations were injected
            assert "#test123" in result
            assert "Syneto Elements Theme" in result
            assert "sl-elements" in result
            assert "API Docs" in result

    def test_theme_consistency_across_components(self):
        """Test that theme settings are consistent across all components."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        elements = SynetoElements(brand_config=brand_config)

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = elements.render()

            # Verify theme colors are used consistently
            assert brand_config.background_color in result
            assert brand_config.text_color in result
            assert brand_config.primary_color in result

    def test_sidebar_styling(self):
        """Test that sidebar elements are properly styled."""
        elements = SynetoElements()

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = elements.render()

            assert ".sl-elements-sidebar" in result
            assert ".sl-stack-item" in result
            assert "background-color" in result
            assert "border-color" in result

    def test_button_styling(self):
        """Test that buttons are properly styled."""
        elements = SynetoElements()

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = elements.render()

            assert ".sl-button--primary" in result
            assert "background-color" in result
            assert "border-color" in result

    def test_dark_theme_specific_styling(self):
        """Test dark theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.DARK)
        elements = SynetoElements(brand_config=brand_config)

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = elements.render()

            # Verify dark theme colors
            assert SynetoColors.PRIMARY_DARK in result
            assert SynetoColors.PRIMARY_LIGHT in result  # Text color for dark theme

    def test_light_theme_specific_styling(self):
        """Test light theme specific styling elements."""
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)
        elements = SynetoElements(brand_config=brand_config)

        with patch("syneto_openapi_themes.elements.Elements.render") as mock_render:
            mock_render.return_value = "<html><body>Test</body></html>"

            result = elements.render()

            # Verify light theme colors are applied
            assert brand_config.background_color in result
            assert brand_config.text_color in result

    def test_configuration_options(self):
        """Test that configuration options are properly applied."""
        elements = SynetoElements(layout="stacked", hideInternal=True, hideTryIt=False, hideSchemas=True)

        # Configuration should be stored and accessible
        assert elements.brand_config is not None

    def test_get_layout_config(self):
        """Test getting layout configuration."""
        elements = SynetoElements()
        config = elements.get_layout_config()

        assert isinstance(config, dict)
        assert "layout" in config
        assert "hideInternal" in config
        assert "hideSchemas" in config
        assert "hideExport" in config
        assert "hideTryIt" in config
        assert "tryItCredentialsPolicy" in config
        assert "router" in config
        assert "basePath" in config

    def test_with_sidebar_layout(self):
        """Test configuring sidebar layout."""
        elements = SynetoElements()
        result = elements.with_sidebar_layout()

        # Verify method chaining
        assert result is elements

        # Verify layout was set
        assert elements.elements_config["layout"] == "sidebar"

    def test_with_stacked_layout(self):
        """Test configuring stacked layout."""
        elements = SynetoElements()
        result = elements.with_stacked_layout()

        # Verify method chaining
        assert result is elements

        # Verify layout was set
        assert elements.elements_config["layout"] == "stacked"

    def test_with_try_it_disabled(self):
        """Test disabling Try It functionality."""
        elements = SynetoElements()
        result = elements.with_try_it_disabled()

        # Verify method chaining
        assert result is elements

        # Verify Try It was disabled
        assert elements.elements_config["hideTryIt"] is True

    def test_layout_configuration_chaining(self):
        """Test chaining layout configuration methods."""
        elements = SynetoElements()

        result = elements.with_stacked_layout().with_try_it_disabled()

        # Verify chaining worked
        assert result is elements

        # Verify both configurations were applied
        assert elements.elements_config["layout"] == "stacked"
        assert elements.elements_config["hideTryIt"] is True
