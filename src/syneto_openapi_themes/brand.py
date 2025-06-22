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
SYNETO_LOGO_SVG = '<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1439.03 540.46"><defs><style>.cls-1{fill:#e40d78;}.cls-2{isolation:isolate;}.cls-3{fill:#fff;}.cls-4{mix-blend-mode:overlay;}</style></defs><g class="cls-2"><g id="Layer_1"><path class="cls-1" d="M434.85,479.9c0,7.9-6.4,14.3-14.3,14.3s-14.31-6.41-14.31-14.3,6.41-14.3,14.31-14.3,14.3,6.41,14.3,14.3Z"/><path class="cls-1" d="M1012.18,479.9c0,7.9-6.4,14.3-14.3,14.3s-14.31-6.41-14.31-14.3,6.41-14.3,14.31-14.3,14.3,6.41,14.3,14.3Z"/><path class="cls-3" d="M56.05,491.11c0-4.14-1.55-7.52-4.65-10.14-3.1-2.62-8.5-4.95-16.19-6.96-8.32-2.09-14.63-4.81-18.91-8.15s-6.43-7.85-6.43-13.53,2.39-10.55,7.18-14.21c4.79-3.66,10.94-5.49,18.47-5.49s14.16,2.18,18.96,6.53c4.81,4.35,7.14,9.66,7,15.93l-.16.31h-5.75c0-5.08-1.8-9.26-5.41-12.54-3.61-3.27-8.49-4.91-14.65-4.91s-10.86,1.36-14.29,4.07c-3.43,2.72-5.15,6.1-5.15,10.13,0,3.83,1.58,7.03,4.75,9.59,3.17,2.56,8.64,4.82,16.4,6.77,8.18,2.09,14.41,4.91,18.68,8.46,4.26,3.55,6.4,8.24,6.4,14.05s-2.48,10.88-7.44,14.47c-4.96,3.59-11.29,5.38-18.99,5.38s-14.22-1.91-19.88-5.72c-5.66-3.81-8.4-9.38-8.23-16.69l.1-.31h5.75c0,5.9,2.21,10.28,6.63,13.12,4.42,2.85,9.63,4.27,15.62,4.27s10.89-1.32,14.6-3.96c3.71-2.64,5.56-6.14,5.56-10.48Z"/><path class="cls-3" d="M82.12,437.07h-6.22v-8.78h6.22v8.78ZM82.12,509.78h-6.22v-56.52h6.22v56.52Z"/><path class="cls-3" d="M104.69,453.26l.57,9.35c1.81-3.31,4.22-5.87,7.23-7.68,3.01-1.81,6.61-2.72,10.79-2.72s7.93,1.04,10.84,3.13,4.99,5.28,6.24,9.56c1.71-3.97,4.13-7.08,7.29-9.33,3.15-2.25,6.99-3.37,11.52-3.37,6.02,0,10.67,2,13.95,6.01,3.27,4.01,4.91,10.2,4.91,18.6v32.96h-6.27v-33.13c0-6.98-1.23-11.91-3.68-14.79-2.45-2.88-5.88-4.32-10.26-4.32-4.84,0-8.58,1.52-11.23,4.55-2.65,3.04-4.28,6.93-4.91,11.67,0,.25,0,.59.03,1.05.02.45.03.78.03.99v33.97h-6.32v-33.13c0-6.84-1.25-11.73-3.73-14.68-2.49-2.95-5.91-4.42-10.27-4.42s-7.93,1.13-10.53,3.38c-2.6,2.25-4.41,5.28-5.46,9.08v39.78h-6.32v-56.52h5.59Z"/><path class="cls-3" d="M239.72,483.09c0,8.46-1.92,15.21-5.75,20.24-3.83,5.03-9.11,7.55-15.83,7.55-3.97,0-7.44-.75-10.42-2.25-2.98-1.5-5.41-3.64-7.29-6.43v29.31h-6.27v-78.25h5.28l.78,8.78c1.88-3.13,4.31-5.55,7.29-7.26,2.98-1.71,6.49-2.56,10.53-2.56,6.79,0,12.1,2.71,15.93,8.12,3.83,5.42,5.75,12.63,5.75,21.65v1.1ZM233.46,481.91c0-7.18-1.43-13.04-4.28-17.57-2.86-4.53-7.04-6.8-12.54-6.8-4.21,0-7.64,1-10.27,3.01-2.63,2-4.61,4.61-5.93,7.82v27.19c1.43,3.1,3.49,5.54,6.19,7.32,2.7,1.78,6.07,2.67,10.11,2.67,5.47,0,9.62-2.06,12.46-6.17,2.84-4.11,4.26-9.57,4.26-16.37v-1.1Z"/><path class="cls-3" d="M260.78,509.78h-6.22v-81.49h6.22v81.49Z"/><path class="cls-3" d="M285.07,437.07h-6.22v-8.78h6.22v8.78ZM285.07,509.78h-6.22v-56.52h6.22v56.52Z"/><path class="cls-3" d="M306.9,509.78v-51.4h-9.35v-5.12h9.35v-8.25c0-5.68,1.42-10.06,4.26-13.16,2.84-3.1,6.82-4.65,11.94-4.65,1.15,0,2.32.09,3.5.26,1.18.17,2.39.42,3.6.73l-.78,5.17c-.84-.21-1.7-.37-2.59-.5-.89-.12-1.92-.18-3.11-.18-3.41,0-6.03,1.08-7.84,3.24-1.81,2.16-2.72,5.19-2.72,9.09v8.25h13.48v5.12h-13.48v51.4h-6.27Z"/><path class="cls-3" d="M353.55,494.48l1.99,6.74h.31l17.08-47.96h7l-24.55,65.56c-1.46,3.83-3.36,7.09-5.69,9.77-2.33,2.68-5.75,4.02-10.24,4.02-.73,0-1.62-.08-2.66-.24-1.04-.16-1.81-.32-2.3-.5l.73-5.22c.42.07,1.09.15,2.01.24.92.09,1.59.13,2.01.13,2.72,0,4.89-.97,6.53-2.9,1.64-1.93,3.03-4.41,4.18-7.44l2.98-7.63-21.84-55.79h6.95l15.52,41.22Z"/><path class="cls-3" d="M510.48,488.57h-34.84l-7.84,21.21h-6.48l28.89-76.06h5.9l28.68,76.06h-6.48l-7.84-21.21ZM477.73,482.98h30.72l-15.15-41.16h-.31l-15.25,41.16Z"/><path class="cls-3" d="M555.67,505.55c4.14,0,7.8-1.18,10.97-3.54,3.17-2.36,4.75-5.64,4.75-9.83h5.54l.1.31c.17,5.22-1.92,9.6-6.27,13.11-4.35,3.52-9.39,5.28-15.1,5.28-7.7,0-13.64-2.64-17.84-7.91-4.2-5.28-6.3-12.06-6.3-20.35v-2.19c0-8.22,2.11-14.97,6.32-20.27,4.21-5.29,10.13-7.94,17.76-7.94,6.2,0,11.36,1.83,15.49,5.49,4.13,3.66,6.12,8.46,5.98,14.42l-.1.31h-5.59c0-4.53-1.52-8.14-4.57-10.84s-6.78-4.05-11.2-4.05c-6.06,0-10.54,2.17-13.45,6.5s-4.36,9.78-4.36,16.36v2.19c0,6.68,1.44,12.18,4.34,16.49,2.89,4.31,7.4,6.47,13.53,6.47Z"/><path class="cls-3" d="M611.09,505.55c4.14,0,7.8-1.18,10.97-3.54,3.17-2.36,4.75-5.64,4.75-9.83h5.54l.1.31c.17,5.22-1.92,9.6-6.27,13.11-4.35,3.52-9.39,5.28-15.1,5.28-7.7,0-13.64-2.64-17.84-7.91-4.2-5.28-6.3-12.06-6.3-20.35v-2.19c0-8.22,2.11-14.97,6.32-20.27,4.21-5.29,10.13-7.94,17.76-7.94,6.2,0,11.36,1.83,15.49,5.49,4.13,3.66,6.12,8.46,5.98,14.42l-.1.31h-5.59c0-4.53-1.52-8.14-4.57-10.84-3.05-2.7-6.78-4.05-11.2-4.05-6.06,0-10.54,2.17-13.45,6.5s-4.36,9.78-4.36,16.36v2.19c0,6.68,1.44,12.18,4.34,16.49,2.89,4.31,7.4,6.47,13.53,6.47Z"/><path class="cls-3" d="M666.78,510.88c-7.07,0-12.95-2.61-17.63-7.84s-7.03-11.84-7.03-19.85v-2.87c0-8.08,2.32-14.78,6.97-20.11,4.65-5.33,10.28-7.99,16.9-7.99s12.38,2.19,16.35,6.58c3.97,4.39,5.96,10.24,5.96,17.55v5.33h-39.91v1.51c0,6.36,1.69,11.68,5.07,15.95,3.38,4.27,7.82,6.41,13.32,6.41,3.9,0,7.23-.54,9.98-1.62,2.75-1.08,5.1-2.63,7.05-4.65l2.66,4.28c-2.13,2.24-4.81,4.02-8.07,5.34-3.26,1.32-7.13,1.98-11.62,1.98ZM666,457.54c-4.63,0-8.52,1.76-11.65,5.29s-4.96,7.94-5.49,13.26l.1.26h33.12v-1.56c0-4.9-1.45-9-4.34-12.29-2.89-3.3-6.81-4.95-11.75-4.95Z"/><path class="cls-3" d="M707.68,509.78h-6.22v-81.49h6.22v81.49Z"/><path class="cls-3" d="M746.18,510.88c-7.07,0-12.95-2.61-17.63-7.84s-7.03-11.84-7.03-19.85v-2.87c0-8.08,2.32-14.78,6.97-20.11,4.65-5.33,10.28-7.99,16.9-7.99s12.38,2.19,16.35,6.58c3.97,4.39,5.96,10.24,5.96,17.55v5.33h-39.91v1.51c0,6.36,1.69,11.68,5.07,15.95,3.38,4.27,7.82,6.41,13.32,6.41,3.9,0,7.23-.54,9.98-1.62,2.75-1.08,5.1-2.63,7.05-4.65l2.66,4.28c-2.13,2.24-4.81,4.02-8.07,5.34-3.26,1.32-7.13,1.98-11.62,1.98ZM745.4,457.54c-4.63,0-8.52,1.76-11.65,5.29s-4.96,7.94-5.49,13.26l.1.26h33.12v-1.56c0-4.9-1.45-9-4.34-12.29-2.89-3.3-6.81-4.95-11.75-4.95Z"/><path class="cls-3" d="M806.1,458.64l-4.65-.31c-3.94,0-7.17,1.11-9.69,3.32-2.53,2.21-4.33,5.25-5.41,9.12v39.02h-6.27v-56.52h5.49l.78,9.4v.63c1.64-3.48,3.83-6.2,6.58-8.15,2.75-1.95,6.02-2.93,9.82-2.93.8,0,1.58.06,2.32.18s1.37.25,1.85.39l-.84,5.85Z"/><path class="cls-3" d="M852.28,509.78c-.42-1.92-.71-3.57-.89-4.96-.17-1.39-.26-2.8-.26-4.23-2.09,2.96-4.88,5.42-8.36,7.37-3.48,1.95-7.4,2.93-11.75,2.93-5.5,0-9.78-1.46-12.83-4.39s-4.57-6.84-4.57-11.75c0-5.22,2.25-9.4,6.76-12.54,4.51-3.13,10.6-4.7,18.26-4.7h12.49v-7c0-4.04-1.3-7.21-3.89-9.51s-6.23-3.45-10.89-3.45c-4.35,0-7.97,1.1-10.84,3.29-2.87,2.19-4.31,4.88-4.31,8.04l-5.75-.05-.1-.31c-.21-4.21,1.72-7.98,5.77-11.31s9.22-4.99,15.49-4.99,11.25,1.58,15.04,4.75c3.8,3.17,5.69,7.71,5.69,13.63v27.79c0,1.99.11,3.92.34,5.8s.6,3.74,1.12,5.59h-6.53ZM831.75,505.34c4.49,0,8.46-1.05,11.91-3.16,3.45-2.11,5.94-4.8,7.47-8.07v-11.81h-12.59c-5.68,0-10.21,1.21-13.61,3.63-3.4,2.42-5.09,5.42-5.09,9.01,0,3.07,1.05,5.56,3.16,7.5,2.11,1.93,5.02,2.9,8.75,2.9Z"/><path class="cls-3" d="M883.83,438.79v14.47h12.43v5.12h-12.43v36.83c0,3.69.67,6.31,2.01,7.86s3.13,2.32,5.36,2.32c1.01,0,1.99-.04,2.95-.13.96-.09,2.06-.24,3.32-.44l.94,4.65c-1.04.45-2.32.8-3.81,1.04-1.5.24-3,.37-4.49.37-3.97,0-7.06-1.25-9.27-3.76-2.21-2.51-3.32-6.48-3.32-11.91v-36.83h-9.77v-5.12h9.77v-14.47h6.32Z"/><path class="cls-3" d="M930.75,510.88c-7.07,0-12.95-2.61-17.63-7.84s-7.03-11.84-7.03-19.85v-2.87c0-8.08,2.32-14.78,6.97-20.11,4.65-5.33,10.28-7.99,16.9-7.99s12.38,2.19,16.35,6.58,5.96,10.24,5.96,17.55v5.33h-39.91v1.51c0,6.36,1.69,11.68,5.07,15.95,3.38,4.27,7.82,6.41,13.32,6.41,3.9,0,7.23-.54,9.98-1.62,2.75-1.08,5.1-2.63,7.05-4.65l2.66,4.28c-2.13,2.24-4.81,4.02-8.07,5.34-3.26,1.32-7.13,1.98-11.62,1.98ZM929.96,457.54c-4.63,0-8.52,1.76-11.65,5.29s-4.96,7.94-5.49,13.26l.1.26h33.12v-1.56c0-4.9-1.45-9-4.34-12.29-2.89-3.3-6.81-4.95-11.75-4.95Z"/><path class="cls-3" d="M1050.64,478.18v31.6h-6.22v-76.06h26.17c7.97,0,14.15,2.03,18.52,6.09,4.37,4.06,6.56,9.43,6.56,16.12s-2.19,12.16-6.56,16.19c-4.37,4.04-10.54,6.06-18.52,6.06h-19.96ZM1050.64,472.85h19.96c6.27,0,10.98-1.59,14.13-4.78,3.15-3.19,4.73-7.2,4.73-12.04s-1.57-8.92-4.7-12.15c-3.13-3.22-7.85-4.83-14.16-4.83h-19.96v33.8Z"/><path class="cls-3" d="M1134.9,458.64l-4.65-.31c-3.94,0-7.17,1.11-9.69,3.32-2.53,2.21-4.33,5.25-5.41,9.12v39.02h-6.27v-56.52h5.49l.78,9.4v.63c1.64-3.48,3.83-6.2,6.58-8.15,2.75-1.95,6.02-2.93,9.82-2.93.8,0,1.58.06,2.32.18s1.37.25,1.85.39l-.84,5.85Z"/><path class="cls-3" d="M1140.75,480.69c0-8.32,2.28-15.15,6.84-20.48,4.56-5.33,10.6-7.99,18.13-7.99s13.62,2.66,18.18,7.99c4.56,5.33,6.84,12.16,6.84,20.48v1.72c0,8.36-2.27,15.19-6.82,20.5-4.55,5.31-10.58,7.97-18.1,7.97s-13.67-2.66-18.23-7.97c-4.56-5.31-6.84-12.15-6.84-20.5v-1.72ZM1147.02,482.38c0,6.54,1.65,12.04,4.96,16.49,3.31,4.45,7.92,6.68,13.84,6.68s10.39-2.23,13.71-6.68c3.32-4.45,4.99-9.95,4.99-16.49v-1.72c0-6.44-1.67-11.9-5.01-16.38-3.34-4.49-7.94-6.73-13.79-6.73s-10.43,2.24-13.74,6.73c-3.31,4.49-4.96,9.95-4.96,16.38v1.72Z"/><path class="cls-3" d="M1213.62,438.79v14.47h12.43v5.12h-12.43v36.83c0,3.69.67,6.31,2.01,7.86s3.13,2.32,5.36,2.32c1.01,0,1.99-.04,2.95-.13.96-.09,2.06-.24,3.32-.44l.94,4.65c-1.04.45-2.32.8-3.81,1.04-1.5.24-3,.37-4.49.37-3.97,0-7.06-1.25-9.27-3.76-2.21-2.51-3.32-6.48-3.32-11.91v-36.83h-9.77v-5.12h9.77v-14.47h6.32Z"/><path class="cls-3" d="M1260.53,510.88c-7.07,0-12.95-2.61-17.63-7.84s-7.03-11.84-7.03-19.85v-2.87c0-8.08,2.32-14.78,6.97-20.11,4.65-5.33,10.28-7.99,16.9-7.99s12.38,2.19,16.35,6.58,5.96,10.24,5.96,17.55v5.33h-39.91v1.51c0,6.36,1.69,11.68,5.07,15.95,3.38,4.27,7.82,6.41,13.32,6.41,3.9,0,7.23-.54,9.98-1.62,2.75-1.08,5.1-2.63,7.05-4.65l2.66,4.28c-2.13,2.24-4.81,4.02-8.07,5.34-3.26,1.32-7.13,1.98-11.62,1.98ZM1259.75,457.54c-4.63,0-8.52,1.76-11.65,5.29s-4.96,7.94-5.49,13.26l.1.26h33.12v-1.56c0-4.9-1.45-9-4.34-12.29-2.89-3.3-6.81-4.95-11.75-4.95Z"/><path class="cls-3" d="M1315.38,505.55c4.14,0,7.8-1.18,10.97-3.54,3.17-2.36,4.75-5.64,4.75-9.83h5.54l.1.31c.17,5.22-1.92,9.6-6.27,13.11-4.35,3.52-9.39,5.28-15.1,5.28-7.7,0-13.64-2.64-17.84-7.91-4.2-5.28-6.3-12.06-6.3-20.35v-2.19c0-8.22,2.11-14.97,6.32-20.27,4.21-5.29,10.13-7.94,17.76-7.94,6.2,0,11.36,1.83,15.49,5.49,4.13,3.66,6.12,8.46,5.98,14.42l-.1.31h-5.59c0-4.53-1.52-8.14-4.57-10.84-3.05-2.7-6.78-4.05-11.2-4.05-6.06,0-10.54,2.17-13.45,6.5-2.91,4.33-4.36,9.78-4.36,16.36v2.19c0,6.68,1.44,12.18,4.34,16.49,2.89,4.31,7.4,6.47,13.53,6.47Z"/><path class="cls-3" d="M1359.68,438.79v14.47h12.43v5.12h-12.43v36.83c0,3.69.67,6.31,2.01,7.86s3.13,2.32,5.36,2.32c1.01,0,1.99-.04,2.95-.13.96-.09,2.06-.24,3.32-.44l.94,4.65c-1.04.45-2.32.8-3.81,1.04-1.5.24-3,.37-4.49.37-3.97,0-7.06-1.25-9.27-3.76-2.21-2.51-3.32-6.48-3.32-11.91v-36.83h-9.77v-5.12h9.77v-14.47h6.32Z"/><path class="cls-3" d="M7.87,294.68v-53.95c14.12,9.91,28.59,17.93,43.32,24.08,14.78,6.14,27.18,9.19,37.28,9.19s19.46-2.57,26.98-7.67c7.5-5.14,11.27-11.31,11.27-18.44,0-7.37-2.41-13.47-7.26-18.31-4.87-4.88-15.38-11.87-31.52-21.04-32.3-17.97-53.42-33.37-63.43-46.12-9.98-12.73-15-26.64-15-41.7,0-19.45,7.56-35.3,22.7-47.58,15.14-12.29,34.64-18.44,58.44-18.44s50.2,6.98,76.26,20.91v49.55c-29.72-18.02-54.03-26.97-72.93-26.97-9.73,0-17.57,2.03-23.53,6.17-5.94,4.14-8.94,9.6-8.94,16.39,0,5.88,2.7,11.52,8.12,16.82,5.41,5.3,14.88,11.74,28.46,19.25l17.9,10.19c42.18,23.88,63.28,50.25,63.28,79.23,0,20.74-8.11,37.72-24.35,51.04-16.22,13.26-37.1,19.93-62.56,19.93-15.08,0-28.47-1.59-40.19-4.81-11.73-3.22-26.51-9.12-44.3-17.74Z"/><path class="cls-3" d="M489.2,59.63v32.21c22.38-24.76,47.78-37.14,76.21-37.14,15.77,0,30.48,4.07,44.04,12.25,13.59,8.17,23.9,19.34,30.94,33.56,7.08,14.23,10.62,36.74,10.62,67.57v144.74h-50.09l.02-144.18c0-25.89-3.95-44.36-11.87-55.45-7.9-11.11-21.07-16.67-39.61-16.68-23.68,0-43.77,11.87-60.26,35.51v180.8h-51.18V59.63h51.18Z"/><path class="cls-3" d="M896.81,184.3c0-39.43-9.99-70.88-29.98-94.38-20.03-23.46-46.78-35.21-80.36-35.21s-63.21,12.08-85.02,36.17c-21.85,24.11-32.76,55.49-32.76,94.01.01,25.68,5.17,48.27,15.54,67.81,10.36,19.55,24.18,35.11,41.42,46.65,17.24,11.55,39.8,17.34,67.68,17.34,20.36,0,38.13-2.19,53.26-6.6,15.15-4.42,30.4-11.74,45.82-22.01v-49.01c-27.88,20.6-58.32,30.84-91.37,30.84-23.67,0-42.98-7.14-57.92-21.45-14.97-14.31-23.09-33.56-24.36-57.82h178.05v-6.33ZM719.87,160.67c3.49-20.01,10.97-35.42,22.42-46.23,11.47-10.85,26.21-16.24,44.19-16.24,17.94,0,32.26,5.39,42.88,16.24,10.66,10.82,16.62,26.22,17.91,46.21l-127.4.02Z"/><path class="cls-3" d="M1025.78,272.12c-24.05,0-36.06-14.48-36.04-43.42l-.02-169.46V7.37s-52.76,51.86-52.76,51.86l-41.34,40.63v4.91h44.02s0,112.31,0,112.31c0,22.94,1.05,38.45,3.17,46.63,2.07,8.2,4.73,14.78,7.81,19.81,3.12,5.06,7.07,9.59,11.87,13.61,15.22,13.42,34.29,20.11,57.22,20.11s43.76-5.39,63.02-16.25v-46.73c-19.98,11.87-38.98,17.87-56.96,17.87Z"/><path class="cls-3" d="M1335.93,96.4c-24.8-24.19-55.84-36.49-92.97-37.15v-.14h-221.25s0,45.17,0,45.17h113.41c-20.55,23.21-30.92,51.33-30.92,84.46-.01,36.67,12.76,67.28,38.25,91.76,25.52,24.49,57.25,36.74,95.23,36.74s71.83-12.08,97.7-36.2c25.88-24.12,38.8-54.45,38.8-90.95-.02-37.6-12.76-68.84-38.24-93.68ZM1299.72,247.19c-15.65,15.5-35.82,23.24-60.4,23.24s-45.04-7.66-60.82-22.94c-15.78-15.34-23.64-35.09-23.66-59.33,0-24.34,7.7-44.45,23.11-60.24,15.41-15.78,35.09-23.62,59.07-23.64h.21c24.73.02,45.22,7.87,61.53,23.64,16.31,15.79,24.46,35.67,24.49,59.69,0,24.24-7.82,44.09-23.53,59.59Z"/><polygon class="cls-3" points="326.11 311.38 276.04 363.25 276.02 198.29 181.82 59.23 234.16 59.23 301.12 160.55 367.61 59.23 419.9 59.23 326.11 198.27 326.11 311.38"/><g class="cls-4"><path class="cls-3" d="M1401.44,63.51h-7.18v22.27h-4.44v-22.27h-7.23v-3.96h18.85v3.96ZM1425.91,66.53l-6.84,19.24h-2.54l-6.84-19.19v19.19h-4.39v-26.22h5.47l7.03,19.48,7.03-19.48h5.47v26.22h-4.39v-19.24Z"/></g></g></g></svg>'  # noqa: E501
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
    app_title: Optional[str] = None  # Application title to display next to logo instead of company_name

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
