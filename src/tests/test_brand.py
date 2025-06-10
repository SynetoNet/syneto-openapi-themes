"""
Tests for the brand configuration module.
"""

from syneto_openapi_themes.brand import (
    SynetoBrandConfig,
    SynetoColors,
    SynetoTheme,
    get_default_brand_config,
    get_light_brand_config,
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
        assert SynetoColors.ACCENT_BLUE == "#1e3a8a"
        assert SynetoColors.ACCENT_GREEN == "#059669"
        assert SynetoColors.ACCENT_YELLOW == "#d97706"


class TestSynetoTheme:
    """Test the SynetoTheme enum."""

    def test_theme_values(self):
        """Test theme enum values."""
        assert SynetoTheme.DARK.value == "dark"
        assert SynetoTheme.LIGHT.value == "light"
        assert SynetoTheme.AUTO.value == "auto"


class TestSynetoBrandConfig:
    """Test the SynetoBrandConfig class."""

    def test_default_initialization(self):
        """Test default brand config initialization."""
        config = SynetoBrandConfig()

        assert config.company_name == "Syneto"
        assert config.theme == SynetoTheme.DARK
        assert config.primary_color == SynetoColors.PRIMARY_MAGENTA
        assert config.background_color == SynetoColors.PRIMARY_DARK
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
        assert attrs["primary-color"] == SynetoColors.PRIMARY_MAGENTA
        assert attrs["bg-color"] == SynetoColors.PRIMARY_DARK
        assert "logo" in attrs

    def test_to_css_variables(self):
        """Test conversion to CSS variables."""
        config = SynetoBrandConfig()
        css = config.to_css_variables()

        assert "--syneto-primary-color" in css
        assert SynetoColors.PRIMARY_MAGENTA in css
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
        assert config.background_color == SynetoColors.NEUTRAL_100
        assert config.text_color == SynetoColors.NEUTRAL_900
