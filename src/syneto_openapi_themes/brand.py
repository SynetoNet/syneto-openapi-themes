"""
Syneto brand configuration and theming utilities.
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
from enum import Enum


class SynetoColors:
    """Official Syneto color palette."""
    
    # Primary colors
    PRIMARY_MAGENTA = "#ad0f6c"
    PRIMARY_DARK = "#07080d"
    PRIMARY_LIGHT = "#fcfdfe"
    
    # Secondary colors
    SECONDARY_DARK = "#0f141f"
    SECONDARY_MEDIUM = "#161c2d"
    SECONDARY_LIGHT = "#c4c6ca"
    
    # Accent colors
    ACCENT_RED = "#f01932"
    ACCENT_BLUE = "#1e3a8a"
    ACCENT_GREEN = "#059669"
    ACCENT_YELLOW = "#d97706"
    
    # Neutral colors
    NEUTRAL_100 = "#f8fafc"
    NEUTRAL_200 = "#e2e8f0"
    NEUTRAL_300 = "#cbd5e1"
    NEUTRAL_400 = "#94a3b8"
    NEUTRAL_500 = "#64748b"
    NEUTRAL_600 = "#475569"
    NEUTRAL_700 = "#334155"
    NEUTRAL_800 = "#1e293b"
    NEUTRAL_900 = "#0f172a"


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
    
    # Theme configuration
    theme: SynetoTheme = SynetoTheme.DARK
    primary_color: str = SynetoColors.PRIMARY_MAGENTA
    background_color: str = SynetoColors.PRIMARY_DARK
    text_color: str = SynetoColors.PRIMARY_LIGHT
    
    # Navigation colors
    nav_bg_color: str = SynetoColors.SECONDARY_DARK
    nav_text_color: str = SynetoColors.SECONDARY_LIGHT
    nav_hover_bg_color: str = SynetoColors.SECONDARY_MEDIUM
    nav_hover_text_color: str = SynetoColors.PRIMARY_LIGHT
    nav_accent_color: str = SynetoColors.PRIMARY_MAGENTA
    nav_accent_text_color: str = SynetoColors.PRIMARY_LIGHT
    
    # Header colors
    header_color: str = SynetoColors.SECONDARY_MEDIUM
    
    # Typography
    regular_font: str = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    mono_font: str = "'JetBrains Mono', 'Fira Code', 'Monaco', 'Consolas', monospace"
    
    # Custom CSS and JS
    custom_css_urls: list[str] = None
    custom_js_urls: list[str] = None
    
    def __post_init__(self) -> None:
        """Initialize default values for mutable fields."""
        if self.custom_css_urls is None:
            self.custom_css_urls = []
        if self.custom_js_urls is None:
            self.custom_js_urls = []
    
    def to_rapidoc_attributes(self) -> Dict[str, str]:
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
        background_color=SynetoColors.NEUTRAL_100,
        text_color=SynetoColors.NEUTRAL_900,
        nav_bg_color=SynetoColors.NEUTRAL_200,
        nav_text_color=SynetoColors.NEUTRAL_700,
        nav_hover_bg_color=SynetoColors.NEUTRAL_300,
        nav_hover_text_color=SynetoColors.NEUTRAL_900,
        header_color=SynetoColors.NEUTRAL_200,
    ) 