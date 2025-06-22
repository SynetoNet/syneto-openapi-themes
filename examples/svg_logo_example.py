#!/usr/bin/env python3
"""
Example: Using Syneto OpenAPI Themes with default and custom logos

This example demonstrates the different ways to use logos with Syneto OpenAPI Themes:
1. Default configuration (includes Syneto logo automatically)
2. Custom inline SVG logo
3. Custom logo URL
"""

from fastapi import FastAPI

from syneto_openapi_themes import (
    SYNETO_LOGO_SVG,
    add_syneto_rapidoc,
    get_brand_config_with_svg_logo,
)

# Create FastAPI app
app = FastAPI(
    title="My API with Syneto Branding",
    description="An example API using Syneto OpenAPI Themes with different logo options",
    version="1.0.0",
)

# Example 1: Default configuration (Syneto logo included automatically)
add_syneto_rapidoc(app, docs_url="/docs")

# Example 2: Custom inline SVG logo
custom_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50">
    <rect width="200" height="50" fill="#ad0f6c"/>
    <text x="100" y="30" text-anchor="middle" fill="white" font-family="Arial" font-size="16">
        My Company
    </text>
</svg>"""

custom_brand_config = get_brand_config_with_svg_logo(
    logo_svg=custom_svg,
    company_name="My Company",
)

# Add custom RapiDoc documentation with custom brand configuration
add_syneto_rapidoc(app, brand_config=custom_brand_config, docs_url="/docs-custom")

# Example 3: Using the official Syneto logo constant directly
# (This is the same as the default, but shows how to access the logo constant)
syneto_brand_config = get_brand_config_with_svg_logo(
    logo_svg=SYNETO_LOGO_SVG,  # Using the exported constant
    company_name="Syneto",
)
add_syneto_rapidoc(app, brand_config=syneto_brand_config, docs_url="/docs-syneto")


# Example API endpoints
@app.get("/")
def read_root() -> dict[str, str]:
    """Welcome endpoint."""
    return {"message": "Welcome to the Syneto-branded API!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting API with Syneto branding...")
    print("Visit the following URLs to see different logo configurations:")
    print("- http://localhost:8000/docs (default Syneto logo)")
    print("- http://localhost:8000/docs-custom (custom logo)")
    print("- http://localhost:8000/docs-syneto (explicit Syneto logo)")
    print("💡 The Syneto logo is now embedded inline for better performance!")
    uvicorn.run(app, host="0.0.0.0", port=8000)
