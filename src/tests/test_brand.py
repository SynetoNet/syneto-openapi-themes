"""
Tests for the brand configuration module.
"""

import pytest

from syneto_openapi_themes.brand import (
    SynetoBrandConfig,
    SynetoColors,
    SynetoTheme,
    get_brand_config_with_custom_logo,
    get_brand_config_with_svg_logo,
    get_default_brand_config,
    get_light_brand_config,
    svg_to_data_uri,
)


class TestSynetoColors:
    """Test the SynetoColors class."""

    def test_primary_colors(self):
        """Test primary color constants."""
        assert SynetoColors.PRIMARY_MAGENTA == "#ad0f6c"
        assert SynetoColors.PRIMARY_DARK == "#07080d"
        assert SynetoColors.PRIMARY_LIGHT == "#fcfdfe"

    def test_accent_colors(self):
        """Test accent color constants."""
        assert SynetoColors.ACCENT_RED == "#f01932"
        assert SynetoColors.ACCENT_BLUE == "#006aff"  # Updated to Color Chart v4.0 - Info Color
        assert SynetoColors.ACCENT_GREEN == "#1bdc77"  # Updated to Color Chart v4.0 - Contrast Color
        assert SynetoColors.ACCENT_YELLOW == "#f7db00"  # Updated to Color Chart v4.0 - Warning Color


class TestSynetoTheme:
    """Test the SynetoTheme enum."""

    def test_theme_values(self):
        """Test theme enum values."""
        assert SynetoTheme.DARK.value == "dark"
        assert SynetoTheme.LIGHT.value == "light"
        assert SynetoTheme.AUTO.value == "auto"


class TestSvgToDataUri:
    """Test the svg_to_data_uri function."""

    def test_valid_svg_content(self):
        """Test converting valid SVG content to data URI."""
        svg_content = '<?xml version="1.0" encoding="UTF-8"?>'
        svg_content += '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
        svg_content += '<circle cx="50" cy="50" r="40" fill="#ad0f6c"/>'
        svg_content += "</svg>"
        result = svg_to_data_uri(svg_content)

        assert result.startswith("data:image/svg+xml;utf8,")
        assert "%3C?xml" in result  # URL encoded <?xml
        assert "%2523ad0f6c" in result  # URL encoded #ad0f6c (# becomes %23, then % becomes %25)

    def test_svg_without_xml_declaration(self):
        """Test converting SVG content without XML declaration."""
        svg_content = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
        svg_content += '<circle cx="50" cy="50" r="40" fill="#ad0f6c"/>'
        svg_content += "</svg>"
        result = svg_to_data_uri(svg_content)

        assert result.startswith("data:image/svg+xml;utf8,")
        assert "%3Csvg" in result  # URL encoded <svg

    def test_invalid_svg_content(self):
        """Test error handling for invalid SVG content."""
        invalid_content = "This is not SVG content"

        with pytest.raises(ValueError, match=r"SVG content must start with <\?xml or <svg"):
            svg_to_data_uri(invalid_content)


class TestSynetoBrandConfig:
    """Test the SynetoBrandConfig class."""

    def test_default_initialization(self):
        """Test default brand config initialization."""
        config = SynetoBrandConfig()

        assert config.company_name == "Syneto"
        assert config.theme == SynetoTheme.DARK
        assert config.primary_color == SynetoColors.BRAND_PRIMARY  # Updated to new color constant
        assert config.background_color == SynetoColors.NEUTRAL_DARKEST  # Updated to new color constant
        assert config.custom_css_urls == []
        assert config.custom_js_urls == []

    def test_custom_initialization(self):
        """Test custom brand config initialization."""
        config = SynetoBrandConfig(company_name="Custom Company", theme=SynetoTheme.LIGHT, primary_color="#ff0000")

        assert config.company_name == "Custom Company"
        assert config.theme == SynetoTheme.LIGHT
        assert config.primary_color == "#ff0000"

    def test_to_rapidoc_attributes(self):
        """Test conversion to RapiDoc attributes."""
        config = SynetoBrandConfig()
        attrs = config.to_rapidoc_attributes()

        assert attrs["theme"] == "dark"
        assert attrs["primary-color"] == SynetoColors.BRAND_PRIMARY  # Updated to new color constant
        assert attrs["bg-color"] == SynetoColors.NEUTRAL_DARKEST  # Updated to new color constant
        assert "logo" in attrs

    def test_to_css_variables(self):
        """Test conversion to CSS variables."""
        config = SynetoBrandConfig()
        css = config.to_css_variables()

        assert "--syneto-primary-color" in css
        assert SynetoColors.BRAND_PRIMARY in css  # Updated to new color constant
        assert ":root" in css

    def test_get_loading_css(self):
        """Test loading CSS generation."""
        config = SynetoBrandConfig()
        css = config.get_loading_css()

        assert ".syneto-loading" in css
        assert ".syneto-error" in css
        assert "@keyframes syneto-spin" in css


class TestBrandConfigHelpers:
    """Test brand config helper functions."""

    def test_get_default_brand_config(self):
        """Test default brand config helper."""
        config = get_default_brand_config()

        assert isinstance(config, SynetoBrandConfig)
        assert config.theme == SynetoTheme.DARK
        assert config.company_name == "Syneto"

    def test_get_light_brand_config(self):
        """Test light brand config helper."""
        config = get_light_brand_config()

        assert isinstance(config, SynetoBrandConfig)
        assert config.theme == SynetoTheme.LIGHT
        assert config.background_color == SynetoColors.BG_LIGHTEST  # Updated to new color constant
        assert config.text_color == SynetoColors.NEUTRAL_DARKEST  # Updated to new color constant

    def test_get_brand_config_with_custom_logo(self):
        """Test custom logo brand config helper."""
        logo_url = "/static/my-logo.svg"
        config = get_brand_config_with_custom_logo(logo_url)

        assert isinstance(config, SynetoBrandConfig)
        assert config.logo_url == logo_url
        assert config.theme == SynetoTheme.DARK  # Default theme

    def test_get_brand_config_with_custom_logo_and_kwargs(self):
        """Test custom logo brand config helper with additional kwargs."""
        logo_url = "/static/my-logo.svg"
        config = get_brand_config_with_custom_logo(logo_url, theme=SynetoTheme.LIGHT, company_name="My Company")

        assert isinstance(config, SynetoBrandConfig)
        assert config.logo_url == logo_url
        assert config.theme == SynetoTheme.LIGHT
        assert config.company_name == "My Company"

    def test_get_brand_config_with_svg_logo(self):
        """Test SVG logo brand config helper."""
        svg_content = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
        svg_content += '<circle cx="50" cy="50" r="40" fill="#ad0f6c"/>'
        svg_content += "</svg>"
        config = get_brand_config_with_svg_logo(svg_content)

        assert isinstance(config, SynetoBrandConfig)
        assert config.logo_svg == svg_content
        assert config.theme == SynetoTheme.DARK  # Default theme

    def test_get_brand_config_with_svg_logo_and_kwargs(self):
        """Test SVG logo brand config helper with additional kwargs."""
        svg_content = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
        svg_content += '<circle cx="50" cy="50" r="40" fill="#ad0f6c"/>'
        svg_content += "</svg>"
        config = get_brand_config_with_svg_logo(svg_content, theme=SynetoTheme.LIGHT, company_name="My Company")

        assert isinstance(config, SynetoBrandConfig)
        assert config.logo_svg == svg_content
        assert config.theme == SynetoTheme.LIGHT
        assert config.company_name == "My Company"
