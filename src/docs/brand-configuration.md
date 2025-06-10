# Brand Configuration

This guide covers how to customize the Syneto branding and theming for your OpenAPI documentation.

## Overview

The `SynetoBrandConfig` class is the central configuration point for all branding and theming options. It allows you to customize colors, fonts, logos, and other visual elements while maintaining the Syneto design language.

## Default Configuration

### Dark Theme (Default)

```python
from syneto_openapi_themes import get_default_brand_config

# Get the default dark theme configuration
brand_config = get_default_brand_config()
```

The default configuration uses:
- **Primary Color**: Syneto Magenta (`#ad0f6c`)
- **Background**: Dark (`#07080d`)
- **Text**: Light (`#fcfdfe`)
- **Navigation**: Dark theme colors
- **Fonts**: Inter for regular text, JetBrains Mono for code

### Light Theme

```python
from syneto_openapi_themes import get_light_brand_config

# Get the light theme configuration
brand_config = get_light_brand_config()
```

The light configuration uses:
- **Primary Color**: Syneto Magenta (`#ad0f6c`)
- **Background**: Light (`#f8fafc`)
- **Text**: Dark (`#0f172a`)
- **Navigation**: Light theme colors

## Color Palette

### Syneto Colors

The `SynetoColors` class provides the official Syneto color palette:

```python
from syneto_openapi_themes import SynetoColors

# Primary colors
SynetoColors.PRIMARY_MAGENTA    # #ad0f6c - Main brand color
SynetoColors.PRIMARY_DARK       # #07080d - Dark backgrounds
SynetoColors.PRIMARY_LIGHT      # #fcfdfe - Light text/backgrounds

# Secondary colors
SynetoColors.SECONDARY_DARK     # #0f141f - Navigation backgrounds
SynetoColors.SECONDARY_MEDIUM   # #161c2d - Headers, hover states
SynetoColors.SECONDARY_LIGHT    # #c4c6ca - Secondary text

# Accent colors
SynetoColors.ACCENT_RED         # #f01932 - Error states, DELETE methods
SynetoColors.ACCENT_BLUE        # #1e3a8a - Info states, GET methods
SynetoColors.ACCENT_GREEN       # #059669 - Success states, POST methods
SynetoColors.ACCENT_YELLOW      # #d97706 - Warning states, PUT methods

# Neutral colors (for light themes)
SynetoColors.NEUTRAL_100        # #f8fafc - Lightest
SynetoColors.NEUTRAL_200        # #e2e8f0
SynetoColors.NEUTRAL_300        # #cbd5e1
SynetoColors.NEUTRAL_400        # #94a3b8
SynetoColors.NEUTRAL_500        # #64748b
SynetoColors.NEUTRAL_600        # #475569
SynetoColors.NEUTRAL_700        # #334155
SynetoColors.NEUTRAL_800        # #1e293b
SynetoColors.NEUTRAL_900        # #0f172a - Darkest
```

### Color Usage Guidelines

- **Primary Magenta**: Use for brand elements, primary buttons, links
- **Accent Colors**: Use for HTTP method badges, status indicators
- **Neutral Colors**: Use for text, borders, backgrounds in light themes
- **Secondary Colors**: Use for navigation, headers, subtle backgrounds

## Custom Configuration

### Basic Customization

```python
from syneto_openapi_themes import SynetoBrandConfig, SynetoTheme, SynetoColors

custom_config = SynetoBrandConfig(
    # Basic branding
    company_name="My Company",
    logo_url="/static/my-logo.svg",
    favicon_url="/static/my-favicon.ico",
    
    # Theme selection
    theme=SynetoTheme.LIGHT,
    
    # Primary colors
    primary_color=SynetoColors.ACCENT_BLUE,
    background_color=SynetoColors.NEUTRAL_100,
    text_color=SynetoColors.NEUTRAL_900,
)
```

### Advanced Color Customization

```python
custom_config = SynetoBrandConfig(
    # Main colors
    primary_color="#1e40af",           # Custom blue
    background_color="#f8fafc",        # Light background
    text_color="#1e293b",              # Dark text
    
    # Navigation colors
    nav_bg_color="#e2e8f0",            # Light nav background
    nav_text_color="#475569",          # Nav text
    nav_hover_bg_color="#cbd5e1",      # Nav hover background
    nav_hover_text_color="#1e293b",    # Nav hover text
    nav_accent_color="#1e40af",        # Nav accent (active items)
    nav_accent_text_color="#ffffff",   # Nav accent text
    
    # Header color
    header_color="#f1f5f9",            # Header background
)
```

### Typography Customization

```python
custom_config = SynetoBrandConfig(
    # Font families
    regular_font="'Roboto', 'Helvetica Neue', Arial, sans-serif",
    mono_font="'Source Code Pro', 'Courier New', monospace",
)
```

### Custom Assets

```python
custom_config = SynetoBrandConfig(
    # Logo and favicon
    logo_url="https://cdn.example.com/logo.svg",
    favicon_url="https://cdn.example.com/favicon.ico",
    
    # Additional CSS and JavaScript
    custom_css_urls=[
        "/static/custom-theme.css",
        "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"
    ],
    custom_js_urls=[
        "/static/custom-analytics.js",
        "/static/custom-interactions.js"
    ]
)
```

## Theme Variants

### SynetoTheme Options

```python
from syneto_openapi_themes import SynetoTheme

# Available theme options
SynetoTheme.DARK    # Dark theme (default)
SynetoTheme.LIGHT   # Light theme
SynetoTheme.AUTO    # Auto-detect based on user preference
```

### Creating Theme Variants

```python
# Corporate dark theme
corporate_dark = SynetoBrandConfig(
    theme=SynetoTheme.DARK,
    primary_color=SynetoColors.ACCENT_BLUE,
    company_name="Corporate API",
    logo_url="/static/corporate-logo-dark.svg"
)

# Corporate light theme
corporate_light = SynetoBrandConfig(
    theme=SynetoTheme.LIGHT,
    primary_color=SynetoColors.ACCENT_BLUE,
    background_color=SynetoColors.NEUTRAL_50,
    text_color=SynetoColors.NEUTRAL_900,
    company_name="Corporate API",
    logo_url="/static/corporate-logo-light.svg"
)

# High contrast theme
high_contrast = SynetoBrandConfig(
    theme=SynetoTheme.DARK,
    primary_color="#00ff00",           # Bright green
    background_color="#000000",        # Pure black
    text_color="#ffffff",              # Pure white
    nav_bg_color="#111111",
    nav_text_color="#ffffff"
)
```

## Tool-Specific Customization

### RapiDoc Attributes

The brand configuration automatically converts to RapiDoc-specific attributes:

```python
brand_config = SynetoBrandConfig(
    theme=SynetoTheme.DARK,
    primary_color="#ad0f6c"
)

# Get RapiDoc attributes
attributes = brand_config.to_rapidoc_attributes()
# Returns: {
#     "theme": "dark",
#     "primary-color": "#ad0f6c",
#     "bg-color": "#07080d",
#     ...
# }
```

### CSS Variables

Generate CSS custom properties for use in custom stylesheets:

```python
brand_config = SynetoBrandConfig()
css_vars = brand_config.to_css_variables()

# Returns CSS like:
# :root {
#     --syneto-primary-color: #ad0f6c;
#     --syneto-bg-color: #07080d;
#     --syneto-text-color: #fcfdfe;
#     ...
# }
```

### Loading States

Get branded loading CSS:

```python
brand_config = SynetoBrandConfig()
loading_css = brand_config.get_loading_css()

# Returns CSS for loading indicators with Syneto branding
```

## Best Practices

### Color Accessibility

1. **Contrast Ratios**: Ensure sufficient contrast between text and background colors
2. **Color Blindness**: Don't rely solely on color to convey information
3. **Testing**: Test your color combinations with accessibility tools

```python
# Good contrast example
accessible_config = SynetoBrandConfig(
    background_color="#ffffff",        # White background
    text_color="#1a202c",              # Dark text (high contrast)
    primary_color="#2b6cb0",           # Blue with good contrast
)
```

### Brand Consistency

1. **Logo Variants**: Provide appropriate logo variants for different backgrounds
2. **Color Harmony**: Use colors from the Syneto palette for consistency
3. **Typography**: Stick to 1-2 font families maximum

```python
# Consistent branding example
consistent_config = SynetoBrandConfig(
    # Use official Syneto colors
    primary_color=SynetoColors.PRIMARY_MAGENTA,
    background_color=SynetoColors.PRIMARY_DARK,
    
    # Provide appropriate logo
    logo_url="/static/syneto-logo-white.svg",  # White logo for dark background
    
    # Use recommended fonts
    regular_font="'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    mono_font="'JetBrains Mono', 'Fira Code', monospace"
)
```

### Performance Considerations

1. **Asset Optimization**: Optimize logos and custom assets
2. **CDN Usage**: Use CDNs for external fonts and assets
3. **CSS Minification**: Minify custom CSS files

```python
# Performance-optimized configuration
optimized_config = SynetoBrandConfig(
    # Optimized SVG logo
    logo_url="/static/logo-optimized.svg",
    
    # CDN fonts
    custom_css_urls=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
    ],
    
    # Minified custom CSS
    custom_css_urls=["/static/theme.min.css"]
)
```

## Examples

### E-commerce API Theme

```python
ecommerce_config = SynetoBrandConfig(
    company_name="ShopAPI",
    theme=SynetoTheme.LIGHT,
    primary_color=SynetoColors.ACCENT_GREEN,    # Green for commerce
    background_color=SynetoColors.NEUTRAL_50,
    text_color=SynetoColors.NEUTRAL_900,
    logo_url="/static/shop-logo.svg",
    custom_css_urls=["/static/ecommerce-theme.css"]
)
```

### Financial API Theme

```python
financial_config = SynetoBrandConfig(
    company_name="FinanceAPI",
    theme=SynetoTheme.DARK,
    primary_color=SynetoColors.ACCENT_BLUE,     # Blue for trust
    background_color="#0a0e1a",                 # Very dark blue
    text_color=SynetoColors.NEUTRAL_100,
    nav_bg_color="#1a2332",
    logo_url="/static/finance-logo.svg"
)
```

### Healthcare API Theme

```python
healthcare_config = SynetoBrandConfig(
    company_name="HealthAPI",
    theme=SynetoTheme.LIGHT,
    primary_color="#0ea5e9",                    # Medical blue
    background_color="#fefefe",
    text_color="#1e293b",
    nav_bg_color="#f0f9ff",                     # Light blue tint
    logo_url="/static/health-logo.svg"
)
```

## Troubleshooting

### Common Issues

1. **Colors Not Applying**: Check that color values are valid hex codes
2. **Fonts Not Loading**: Verify font URLs are accessible
3. **Logo Not Displaying**: Ensure logo URL is correct and accessible
4. **CSS Conflicts**: Check for conflicting custom CSS

### Debugging

```python
# Debug configuration
debug_config = SynetoBrandConfig(
    primary_color="#ff0000",  # Bright red to easily spot issues
    background_color="#ffff00",  # Bright yellow background
)

# Test configuration
print(f"Primary color: {debug_config.primary_color}")
print(f"CSS variables: {debug_config.to_css_variables()}")
```

### Validation

```python
def validate_brand_config(config: SynetoBrandConfig) -> list[str]:
    """Validate brand configuration and return any issues."""
    issues = []
    
    # Check color format
    import re
    hex_pattern = r'^#[0-9a-fA-F]{6}$'
    
    if not re.match(hex_pattern, config.primary_color):
        issues.append(f"Invalid primary_color: {config.primary_color}")
    
    if not re.match(hex_pattern, config.background_color):
        issues.append(f"Invalid background_color: {config.background_color}")
    
    # Check URLs
    if not config.logo_url.startswith(('http', '/')):
        issues.append(f"Invalid logo_url: {config.logo_url}")
    
    return issues

# Usage
config = SynetoBrandConfig(primary_color="invalid-color")
issues = validate_brand_config(config)
if issues:
    print("Configuration issues:", issues)
``` 