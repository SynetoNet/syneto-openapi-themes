"""
Syneto brand configuration and theming utilities.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional
from urllib.parse import quote


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


# Official Syneto logo as SVG content
# fmt: off
SYNETO_LOGO_SVG = '<?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 3056.45 530"><defs><style>.i{fill:url(#e);}.j{fill:url(#d);}.k{fill:url(#g);}.l{fill:url(#f);}.m{fill:url(#h);}.n{fill:url(#c);}.o{fill:url(#b);}.p{fill:#fff;}.q{fill:#ff0982;}.r{fill:none;stroke:#fff;stroke-miterlimit:10;stroke-width:40px;}</style><linearGradient id="b" x1="1698.47" y1="166.26" x2="1724.72" y2="140.01" gradientTransform="matrix(1, 0, 0, 1, 0, 0)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".86" stop-color="#5d5d5d" stop-opacity=".51"/><stop offset="1" stop-color="#000" stop-opacity=".8"/></linearGradient><linearGradient id="c" x1="636" y1="392.32" x2="664.91" y2="363.41" xlink:href="#b"/><linearGradient id="d" x1="1156.89" y1="415.74" x2="1193.71" y2="378.92" xlink:href="#b"/><linearGradient id="e" x1="2420.88" y1="380.93" x2="2449.9" y2="351.91" xlink:href="#b"/><linearGradient id="f" x1="2711.11" y1="386.4" x2="2726.07" y2="371.44" xlink:href="#b"/><linearGradient id="g" x1="1135.75" y1="107.14" x2="1039.6" y2="203.3" gradientTransform="matrix(1, 0, 0, 1, 0, 0)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".86" stop-color="#878787" stop-opacity=".23"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></linearGradient><linearGradient id="h" x1="1615.07" y1="259.32" x2="1540.68" y2="259.32" xlink:href="#b"/></defs><g><circle class="r" cx="295" cy="265" r="170"/><circle class="q" cx="295" cy="265" r="110"/></g><g><polygon class="p" points="958.64 415.74 973.89 415.74 958.64 400.49 958.64 415.74"/><path class="p" d="M2544.79,168.65l20.7,20.7c-.5-.86-1.01-1.71-1.54-2.53-5.24-8.12-11.63-14.17-19.16-18.16Z"/><path class="p" d="M669.98,115.26c-18.31,7.31-32.47,17.53-42.48,30.66-10.01,13.13-15.01,28.29-15.01,45.46,0,34.5,20.09,61.61,60.26,81.34,12.35,6.11,28.25,12.42,47.7,18.95,19.45,6.53,33.04,12.85,40.78,18.95,7.74,6.1,11.61,14.62,11.61,25.55,0,9.66-3.59,17.14-10.75,22.46-7.17,5.32-16.93,7.99-29.28,7.99-19.31,0-33.25-3.94-41.84-11.82-8.59-7.88-12.88-20.12-12.88-36.73h-36.98l104.42,104.42c29.65-1.66,53.45-9.28,71.4-22.86,20.44-15.47,30.66-36.77,30.66-63.88,0-33.93-16.75-60.55-50.25-79.85-13.77-7.95-31.37-15.36-52.81-22.25-21.44-6.88-36.41-13.55-44.93-20.02-8.52-6.46-12.78-13.66-12.78-21.61,0-9.08,3.87-16.57,11.61-22.47,5.59-4.25,12.64-6.96,21.16-8.15l-47.1-47.1c-.83,.31-1.66,.62-2.48,.95Z"/><polygon class="p" points="999.4 243.13 956.02 141.23 923.35 108.56 861.84 108.56 961.49 307.23 961.49 381.84 998.24 418.59 1037.3 418.59 1037.3 307.23 1065.64 250.85 1016.82 202.03 999.4 243.13"/><polygon class="p" points="1234.48 108.56 1201.49 108.56 1277.92 184.99 1234.48 108.56"/><polygon class="p" points="1421.52 111.41 1346.99 111.41 1346.99 254.06 1421.52 328.58 1421.52 111.41"/><polygon class="p" points="1344.14 301.48 1306.25 234.81 1179.99 108.56 1159.74 108.56 1159.74 323.44 1234.48 398.18 1234.48 225.67 1344.35 418.59 1418.67 418.59 1418.67 347.24 1344.14 272.71 1344.14 301.48"/><polygon class="p" points="1463.09 415.74 1487.17 415.74 1463.09 391.66 1463.09 415.74"/><polygon class="p" points="1540.68 231.63 1540.68 212.61 1465.94 137.87 1465.94 373 1511.53 418.59 1679.52 418.59 1679.52 361.1 1540.68 361.1 1540.68 287 1615.07 287 1559.71 231.63 1540.68 231.63"/><polygon class="p" points="1658.22 287 1658.22 231.63 1581.21 231.63 1636.57 287 1658.22 287"/><polygon class="p" points="1543.53 169.11 1682.79 169.11 1682.79 111.41 1468.79 111.41 1468.79 119.21 1543.53 193.96 1543.53 169.11"/><polygon class="p" points="1789.82 418.59 1864.56 418.59 1864.56 279.84 1789.82 205.1 1789.82 418.59"/><polygon class="p" points="1698.47 166.26 1750.98 166.26 1698.47 113.75 1698.47 166.26"/><polygon class="o" points="1698.47 166.26 1750.98 166.26 1698.47 113.75 1698.47 166.26"/><path class="p" d="M2112.92,165.71c19.16,0,33.89,7.99,44.18,23.96,10.29,15.97,15.44,39.36,15.44,70.16v14.27c-.06,12.13-.95,23.1-2.64,32.95l56.35,56.35c1.94-3.31,3.78-6.73,5.5-10.3,11.21-23.28,16.82-50.04,16.82-80.28v-14.27c-.14-29.81-5.93-56.25-17.35-79.32-11.43-23.07-27.44-40.85-48.02-53.34-20.59-12.49-44.01-18.74-70.27-18.74s-50.22,6.32-71.01,18.95c-10.9,6.62-20.46,14.71-28.71,24.24l49.62,49.62c9.53-22.83,26.22-34.26,50.1-34.26Z"/><path class="p" d="M2154.15,340.44c-10.22,16.04-24.77,24.06-43.65,24.06-19.88,0-34.85-8.16-44.93-24.49-10.08-16.32-15.12-39.68-15.12-70.06l.21-22.79c.48-12.68,1.87-23.91,4.15-33.73l-53.77-53.77c-3.63,5.41-6.94,11.18-9.89,17.33-11.15,23.21-16.72,50.01-16.72,80.38v17.46c.57,29.25,6.56,55.15,17.99,77.72,11.43,22.57,27.36,39.93,47.8,52.06,20.44,12.14,43.87,18.21,70.27,18.21s49.93-6.28,70.59-18.84c13.16-8.01,24.4-18.2,33.72-30.55l-51.96-51.96c-2.32,7.13-5.21,13.46-8.7,18.94Z"/><g><path class="p" d="M600.27,315.23c0,20.44,5.14,38.51,15.44,54.19,10.29,15.69,25.62,28.04,45.99,37.05,18.01,7.97,37.89,12.41,59.62,13.33l-104.58-104.58h-16.47Z"/><polygon class="p" points="1156.89 415.74 1230.53 415.74 1156.89 342.09 1156.89 415.74"/><path class="p" d="M2399.26,349.73c11.43,22.57,27.36,39.93,47.8,52.06,20.44,12.14,43.87,18.21,70.27,18.21,.22,0,.43,0,.65,0l-136.17-136.17c1.77,24.45,7.58,46.43,17.45,65.91Z"/></g><g><path class="n" d="M600.27,315.23c0,20.44,5.14,38.51,15.44,54.19,10.29,15.69,25.62,28.04,45.99,37.05,18.01,7.97,37.89,12.41,59.62,13.33l-104.58-104.58h-16.47Z"/><polygon class="j" points="1156.89 415.74 1230.53 415.74 1156.89 342.09 1156.89 415.74"/><path class="i" d="M2399.26,349.73c11.43,22.57,27.36,39.93,47.8,52.06,20.44,12.14,43.87,18.21,70.27,18.21,.22,0,.43,0,.65,0l-136.17-136.17c1.77,24.45,7.58,46.43,17.45,65.91Z"/></g><path class="p" d="M2579.39,256.97v14.27c-.14,30.1-5.32,53.17-15.54,69.2-10.22,16.04-24.77,24.06-43.65,24.06-19.88,0-34.85-8.16-44.93-24.49-10.08-16.32-15.12-39.68-15.12-70.06l.21-22.79c2.09-55.09,21.16-83.17,57.19-84.27l-49.31-49.31c-6.75,2.65-13.25,5.86-19.49,9.65-20.8,12.64-36.77,30.56-47.91,53.77-11.15,23.21-16.72,50.01-16.72,80.38v7.22l156.84,156.84c18.13-2.48,34.75-8.29,49.82-17.45,20.65-12.56,36.59-30.48,47.8-53.77,7.49-15.56,12.47-32.68,14.96-51.34l-76.91-76.91c1.83,10.35,2.75,22,2.75,34.98Z"/><path class="p" d="M2825.54,233.66c-21.44-6.88-36.41-13.55-44.93-20.02-8.52-6.46-12.78-13.66-12.78-21.61,0-9.08,3.87-16.57,11.61-22.47,.27-.2,.54-.39,.81-.59l-45.7-45.7c-10.57,6.22-19.25,13.77-26.02,22.65-10.01,13.13-15.01,28.29-15.01,45.46,0,34.5,20.09,61.61,60.26,81.34,12.35,6.11,28.25,12.42,47.7,18.95,19.45,6.53,33.04,12.85,40.78,18.95,7.74,6.1,11.61,14.62,11.61,25.55,0,9.66-3.59,17.14-10.75,22.46-7.17,5.32-16.93,7.99-29.28,7.99-19.31,0-33.26-3.94-41.84-11.82-8.59-7.88-12.88-20.12-12.88-36.73h-64.88l104.16,104.16c5.04,.39,10.19,.6,15.44,.6,35.63,0,63.67-7.74,84.11-23.21,20.44-15.47,30.66-36.77,30.66-63.88,0-7.25-.77-14.16-2.30-20.74l-70-70c-9.19-3.94-19.43-7.72-30.76-11.36Z"/><path class="p" d="M2696.74,369.43c10.29,15.69,25.62,28.04,45.99,37.05,8.72,3.86,17.88,6.89,27.48,9.1l-88.28-88.28c1.66,15.56,6.58,29.61,14.8,42.13Z"/><path class="l" d="M2696.74,369.43c10.29,15.69,25.62,28.04,45.99,37.05,8.72,3.86,17.88,6.89,27.48,9.1l-88.28-88.28c1.66,15.56,6.58,29.61,14.8,42.13Z"/><path class="p" d="M764.29,174.01c6.08,5.47,9.77,12.71,11.06,21.69l7.69,7.69h67.37c0-18.88-4.9-35.67-14.69-50.36-9.79-14.69-23.53-26.01-41.2-33.96-17.67-7.95-37.66-11.93-59.94-11.93-15.31,0-29.59,1.65-42.86,4.93l52.48,52.48c8.01,1.48,14.71,4.63,20.08,9.46Z"/><polygon class="p" points="1140.02 111.41 1059.31 111.41 1026.08 189.78 1075.68 239.39 1140.02 111.41"/><polygon class="k" points="1140.02 111.41 1059.31 111.41 1026.08 189.78 1075.68 239.39 1140.02 111.41"/><polygon class="p" points="1717.63 111.41 1775.33 169.11 1792.67 169.11 1792.67 186.45 1867.41 261.19 1867.41 169.11 1960.46 169.11 1960.46 119.11 1952.76 111.41 1717.63 111.41"/><path class="p" d="M2566.8,189.66c.53,.82,1.04,1.67,1.54,2.53l89.73,89.73c.12-3,.19-6.03,.19-9.11v-14.27c-.14-29.81-5.93-56.25-17.35-79.32-11.43-23.07-27.44-40.85-48.02-53.34-20.59-12.49-44.01-18.74-70.27-18.74-12.36,0-24.09,1.39-35.2,4.13l60.22,60.22c7.53,3.99,13.92,10.04,19.16,18.16Z"/><path class="p" d="M2813.91,163.58c13.2,0,23.67,3.48,31.41,10.43,7.74,6.96,11.61,16.75,11.61,29.39h74.53c0-18.88-4.9-35.67-14.69-50.36-9.8-14.69-23.53-26.01-41.2-33.96-17.67-7.95-37.66-11.93-59.94-11.93s-43.44,3.66-61.75,10.97c-.71,.28-1.4,.58-2.1,.87l46.28,46.28c4.76-1.12,10.05-1.68,15.87-1.68Z"/><polygon class="m" points="1540.68 287 1540.68 231.63 1559.71 231.63 1615.07 287 1540.68 287"/></g></svg>'  # noqa: E501
# fmt: on


def svg_to_data_uri(svg_content: str) -> str:
    """
    Convert SVG content to a data URI.

    Args:
        svg_content: Raw SVG content as a string

    Returns:
        Data URI string that can be used in img src or CSS background-image
    """
    # Clean up the SVG content
    svg_content = svg_content.strip()

    # Ensure it starts with <?xml or <svg
    if not svg_content.startswith(("<?xml", "<svg")):
        raise ValueError("SVG content must start with <?xml or <svg")

    # URL encode the SVG content, but preserve some characters for better compression
    # We need to encode # as %23 since it has special meaning in URLs
    svg_content = svg_content.replace("#", "%23")

    # Encode other special characters but keep most readable characters
    svg_content = quote(svg_content, safe=":/?#[]@!$&'()*+,;=-._~")

    return f"data:image/svg+xml;utf8,{svg_content}"


@dataclass
class SynetoBrandConfig:
    """Configuration for Syneto branding."""

    # Logo and branding
    logo_url: str = "https://syneto.eu/wp-content/uploads/2021/06/syneto-logo-new-motto-white-1.svg"
    logo_svg: Optional[str] = SYNETO_LOGO_SVG  # Default to official Syneto logo
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
        # Determine logo URL - prefer inline SVG over external URL
        logo_value = self.logo_url
        if self.logo_svg:
            logo_value = svg_to_data_uri(self.logo_svg)

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
            "logo": logo_value,
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


def get_brand_config_with_custom_logo(logo_url: str, **kwargs: Any) -> SynetoBrandConfig:
    """
    Get a Syneto brand configuration with a custom logo URL.

    Args:
        logo_url: URL to the custom logo (can be local path like '/static/logo.svg'
                 or external URL)
        **kwargs: Additional brand configuration overrides

    Returns:
        SynetoBrandConfig with custom logo and any additional overrides

    Examples:
        # Use local logo
        config = get_brand_config_with_custom_logo("/static/my-logo.svg")

        # Use external logo with light theme
        config = get_brand_config_with_custom_logo(
            "https://example.com/logo.svg",
            theme=SynetoTheme.LIGHT
        )
    """
    return SynetoBrandConfig(logo_url=logo_url, **kwargs)


def get_brand_config_with_svg_logo(logo_svg: str, **kwargs: Any) -> SynetoBrandConfig:
    """
    Get a Syneto brand configuration with an inline SVG logo.

    Args:
        logo_svg: SVG content as a string (should start with <?xml or <svg)
        **kwargs: Additional brand configuration overrides

    Returns:
        SynetoBrandConfig with inline SVG logo and any additional overrides

    Examples:
        # Use inline SVG logo
        svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="40" fill="#ad0f6c"/>
        </svg>'''
        config = get_brand_config_with_svg_logo(svg_content)

        # Use inline SVG with light theme
        config = get_brand_config_with_svg_logo(
            svg_content,
            theme=SynetoTheme.LIGHT
        )
    """
    return SynetoBrandConfig(logo_svg=logo_svg, **kwargs)
