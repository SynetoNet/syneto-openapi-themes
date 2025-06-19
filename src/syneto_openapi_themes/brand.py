"""
Syneto brand configuration and theming utilities.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SynetoColors:
    """Official Syneto color palette - Color Chart v4.0 (2024)."""

    # Brand Color (Primary Magenta)
    BRAND_PRIMARY = "#ad0f6c"
    BRAND_LIGHT = "#ff53a8"
    BRAND_LIGHTER = "#ff9dcd"
    BRAND_DARK = "#800541"

    # Contrast Color (Green)
    CONTRAST_PRIMARY = "#1bdc77"
    CONTRAST_LIGHT = "#49e392"
    CONTRAST_LIGHTER = "#8deebb"
    CONTRAST_DARK = "#0e6e3c"

    # Accent Color (Purple/Blue)
    ACCENT_PRIMARY = "#724fff"
    ACCENT_LIGHT = "#9c84ff"
    ACCENT_LIGHTER = "#c7b9ff"
    ACCENT_DARK = "#392880"

    # Info Color (Blue)
    INFO_PRIMARY = "#006aff"
    INFO_LIGHT = "#4d97ff"
    INFO_LIGHTER = "#99c3ff"
    INFO_DARK = "#003580"

    # Warning Color (Yellow)
    WARNING_PRIMARY = "#f7db00"
    WARNING_LIGHT = "#f9e64d"
    WARNING_LIGHTER = "#fcf199"
    WARNING_DARK = "#7c6e00"

    # Caution Color (Orange)
    CAUTION_PRIMARY = "#ff8c00"
    CAUTION_LIGHT = "#ffa333"
    CAUTION_LIGHTER = "#ffba66"
    CAUTION_DARK = "#cc7000"

    # Warning Color (Red)
    DANGER_PRIMARY = "#f01932"
    DANGER_LIGHT = "#f55e70"
    DANGER_LIGHTER = "#f9a3ad"
    DANGER_DARK = "#780d19"

    # Dark / Neutral Colors (for light on dark theme)
    NEUTRAL_DARKEST = "#07080d"  # Background Color - darkest
    NEUTRAL_DARKER = "#0f141f"  # Dark / Neutral Color - darker
    NEUTRAL_DARK = "#161c2d"  # Dark / Neutral Color - dark
    NEUTRAL_MEDIUM = "#5c606c"  # Dark / Neutral Color - medium
    NEUTRAL_LIGHT = "#b9bbc0"  # Dark / Neutral Color - light

    # Background Colors (light tints)
    BG_LIGHTEST = "#fcfdfe"  # Background Color - lightest
    BG_LIGHTER = "#f9fafe"  # Background Color - lighter
    BG_LIGHT = "#f5f7fd"  # Background Color - light
    BG_MEDIUM_LIGHT = "#c4c6ca"  # Background Color - medium light
    BG_MEDIUM_DARK = "#7b7c7f"  # Background Color - medium dark

    # Legacy color aliases for backwards compatibility
    PRIMARY_MAGENTA = BRAND_PRIMARY
    PRIMARY_DARK = NEUTRAL_DARKEST
    PRIMARY_LIGHT = BG_LIGHTEST
    SECONDARY_DARK = NEUTRAL_DARKER
    SECONDARY_MEDIUM = NEUTRAL_DARK
    SECONDARY_LIGHT = BG_MEDIUM_LIGHT
    ACCENT_RED = DANGER_PRIMARY
    ACCENT_BLUE = INFO_PRIMARY
    ACCENT_GREEN = CONTRAST_PRIMARY
    ACCENT_YELLOW = WARNING_PRIMARY
    NEUTRAL_100 = BG_LIGHTEST
    NEUTRAL_200 = BG_LIGHTER
    NEUTRAL_300 = BG_LIGHT
    NEUTRAL_400 = BG_MEDIUM_LIGHT
    NEUTRAL_500 = BG_MEDIUM_DARK
    NEUTRAL_600 = NEUTRAL_LIGHT
    NEUTRAL_700 = NEUTRAL_MEDIUM
    NEUTRAL_800 = NEUTRAL_DARK
    NEUTRAL_900 = NEUTRAL_DARKEST


class SynetoTheme(Enum):
    """Available Syneto theme variants."""

    DARK = "dark"
    LIGHT = "light"
    AUTO = "auto"


@dataclass
class SynetoBrandConfig:
    """Configuration for Syneto branding."""

    # Logo and branding
    logo_url: str = "/static/syneto-logo.svg"
    favicon_url: str = "/static/favicon.ico"
    company_name: str = "Syneto"

    # Theme configuration - using light on dark colors from Color Chart v4.0
    theme: SynetoTheme = SynetoTheme.DARK
    primary_color: str = SynetoColors.BRAND_PRIMARY
    background_color: str = SynetoColors.NEUTRAL_DARKEST
    text_color: str = SynetoColors.BG_LIGHTEST

    # Navigation colors - optimized for light on dark theme
    nav_bg_color: str = SynetoColors.NEUTRAL_DARKER
    nav_text_color: str = SynetoColors.NEUTRAL_LIGHT
    nav_hover_bg_color: str = SynetoColors.NEUTRAL_DARK
    nav_hover_text_color: str = SynetoColors.BG_LIGHTEST
    nav_accent_color: str = SynetoColors.BRAND_PRIMARY
    nav_accent_text_color: str = SynetoColors.BG_LIGHTEST

    # Header colors
    header_color: str = SynetoColors.NEUTRAL_DARK

    # Typography
    regular_font: str = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    mono_font: str = "'JetBrains Mono', 'Fira Code', 'Monaco', 'Consolas', monospace"

    # Custom CSS and JS
    custom_css_urls: Optional[list[str]] = None
    custom_js_urls: Optional[list[str]] = None

    def __post_init__(self) -> None:
        """Initialize default values for mutable fields."""
        if self.custom_css_urls is None:
            self.custom_css_urls = []
        if self.custom_js_urls is None:
            self.custom_js_urls = []

    def to_rapidoc_attributes(self) -> dict[str, str]:
        """Convert brand config to RapiDoc HTML attributes."""
        return {
            "theme": self.theme.value,
            "bg-color": self.background_color,
            "text-color": self.text_color,
            "header-color": self.header_color,
            "primary-color": self.primary_color,
            "nav-bg-color": self.nav_bg_color,
            "nav-text-color": self.nav_text_color,
            "nav-hover-bg-color": self.nav_hover_bg_color,
            "nav-hover-text-color": self.nav_hover_text_color,
            "nav-accent-color": self.nav_accent_color,
            "nav-accent-text-color": self.nav_accent_text_color,
            "regular-font": self.regular_font,
            "mono-font": self.mono_font,
            "logo": self.logo_url,
        }

    def to_css_variables(self) -> str:
        """Convert brand config to CSS custom properties."""
        return f"""
        :root {{
            --syneto-primary-color: {self.primary_color};
            --syneto-bg-color: {self.background_color};
            --syneto-text-color: {self.text_color};
            --syneto-header-color: {self.header_color};
            --syneto-nav-bg-color: {self.nav_bg_color};
            --syneto-nav-text-color: {self.nav_text_color};
            --syneto-nav-hover-bg-color: {self.nav_hover_bg_color};
            --syneto-nav-hover-text-color: {self.nav_hover_text_color};
            --syneto-nav-accent-color: {self.nav_accent_color};
            --syneto-nav-accent-text-color: {self.nav_accent_text_color};
            --syneto-regular-font: {self.regular_font};
            --syneto-mono-font: {self.mono_font};
        }}
        """

    def get_loading_css(self) -> str:
        """Get CSS for loading indicator with Syneto branding."""
        return f"""
        .syneto-loading {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-size: 18px;
            color: {self.nav_text_color};
            background-color: {self.background_color};
            font-family: {self.regular_font};
        }}

        .syneto-loading::after {{
            content: '';
            width: 20px;
            height: 20px;
            margin-left: 10px;
            border: 2px solid {self.nav_bg_color};
            border-top: 2px solid {self.primary_color};
            border-radius: 50%;
            animation: syneto-spin 1s linear infinite;
        }}

        @keyframes syneto-spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}

        .syneto-error {{
            text-align: center;
            padding: 2rem;
            background-color: {self.background_color};
            color: {self.text_color};
            font-family: {self.regular_font};
        }}

        .syneto-error h3 {{
            color: #f01932;
            margin-bottom: 1rem;
        }}

        .syneto-error p {{
            margin: 0.5rem 0;
        }}
        """


def get_default_brand_config() -> SynetoBrandConfig:
    """Get the default Syneto brand configuration."""
    return SynetoBrandConfig()


def get_light_brand_config() -> SynetoBrandConfig:
    """Get a light theme Syneto brand configuration."""
    return SynetoBrandConfig(
        theme=SynetoTheme.LIGHT,
        background_color=SynetoColors.BG_LIGHTEST,
        text_color=SynetoColors.NEUTRAL_DARKEST,
        nav_bg_color=SynetoColors.BG_LIGHTER,
        nav_text_color=SynetoColors.NEUTRAL_MEDIUM,
        nav_hover_bg_color=SynetoColors.BG_LIGHT,
        nav_hover_text_color=SynetoColors.NEUTRAL_DARKEST,
        header_color=SynetoColors.BG_LIGHTER,
    )
