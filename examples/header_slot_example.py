#!/usr/bin/env python3
"""
Example: Using Syneto OpenAPI Themes with custom header slot and sticky header

This example demonstrates how to use the custom header slot functionality
to place logos and content in the RapiDoc header instead of the navigation sidebar.
It also shows how to enable/disable the sticky header feature that keeps the header
fixed at the top of the viewport while scrolling.
"""

from typing import Union

from fastapi import FastAPI

from syneto_openapi_themes import (
    SynetoBrandConfig,
    SynetoTheme,
    add_syneto_rapidoc,
)

# Create FastAPI app
app = FastAPI(
    title="Header Slot Demo API",
    description="An example API demonstrating custom header slot usage",
    version="1.0.0",
)

# Example 1: Default configuration (uses custom header slot with Syneto logo and sticky header)
add_syneto_rapidoc(app, docs_url="/docs", sticky_header=True)

# Example 2: Custom header content with additional elements
custom_header_content = (
    """
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
    <div style="display: flex; align-items: center;">
        <img src="data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"""
    + """%3Ccircle cx='50' cy='50' r='40' fill='%23ad0f6c'/%3E"""
    + """%3Ctext x='50' y='58' text-anchor='middle' fill='white' """
    + """font-family='Arial' font-size='24' font-weight='bold'%3EH%3C/text%3E%3C/svg%3E"
             alt="Custom Logo"
             style="max-height: 40px; max-width: 40px; margin-right: 12px;" />
        <span style="color: #bbb; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 18px;">
            Header Demo API
        </span>
    </div>
    <div style="display: flex; align-items: center; gap: 16px;">
        <span style="color: #999; font-size: 14px;">v1.0.0</span>
        <a href="/health" style="color: #ff53a8; text-decoration: none; font-size: 14px;">Health Check</a>
    </div>
</div>
"""
)

add_syneto_rapidoc(
    app,
    docs_url="/docs-custom-header",
    title="Custom Header Demo",
    header_slot_content=custom_header_content,
    sticky_header=True,  # Enable sticky header
    brand_config=SynetoBrandConfig(
        theme=SynetoTheme.DARK,
        company_name="Header Demo Corp",
        primary_color="#ad0f6c",
    ),
)

# Example 3: Simple custom header with just text
simple_header = """
<div style="text-align: center; padding: 8px;">
    <h2 style="margin: 0; color: #ff53a8; font-family: 'Inter', sans-serif;">
        🚀 Simple Header API Documentation
    </h2>
</div>
"""

add_syneto_rapidoc(
    app,
    docs_url="/docs-simple-header",
    title="Simple Header Demo",
    header_slot_content=simple_header,
    sticky_header=False,  # Disable sticky header for comparison
)

# Example 4: Header with interactive elements
interactive_header = """
<div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 16px;">
    <div style="display: flex; align-items: center;">
        <span style="color: #bbb; font-family: 'Inter', sans-serif; font-weight: 600;">
            Interactive API Docs
        </span>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
                <select id="env-selector"
                style="background: #161c2d; color: #bbb; border: 1px solid #5c606c;
                       padding: 4px 8px; border-radius: 4px;">
            <option value="dev">Development</option>
            <option value="staging">Staging</option>
            <option value="prod">Production</option>
        </select>
                <button onclick="alert('Settings clicked!')"
                style="background: #ad0f6c; color: white; border: none;
                       padding: 6px 12px; border-radius: 4px; cursor: pointer;">
            Settings
        </button>
    </div>
</div>
<script>
document.getElementById('env-selector').addEventListener('change', function(e) {
    console.log('Environment changed to:', e.target.value);
    // Here you could update the API server URL dynamically
});
</script>
"""

add_syneto_rapidoc(
    app,
    docs_url="/docs-interactive-header",
    title="Interactive Header Demo",
    header_slot_content=interactive_header,
    sticky_header=True,  # Enable sticky header with interactive elements
)


# Example API endpoints
@app.get("/")
def read_root() -> dict[str, str]:
    """Welcome endpoint."""
    return {"message": "Welcome to the Header Slot Demo API!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, Union[int, str, bool]]:
    """Get user by ID."""
    return {"user_id": user_id, "name": f"User {user_id}", "active": True}


@app.post("/users")
def create_user(name: str, email: str) -> dict[str, Union[int, str, bool]]:
    """Create a new user."""
    return {"id": 123, "name": name, "email": email, "created": True}


if __name__ == "__main__":
    import uvicorn

    print("🚀 Starting Header Slot Demo API...")
    print("📖 Documentation available at:")
    print("   - Default header (sticky): http://localhost:8000/docs")
    print("   - Custom header (sticky): http://localhost:8000/docs-custom-header")
    print("   - Simple header (non-sticky): http://localhost:8000/docs-simple-header")
    print("   - Interactive header (sticky): http://localhost:8000/docs-interactive-header")
    print("\n💡 Scroll down in the documentation to see the sticky header behavior!")

    uvicorn.run(app, host="0.0.0.0", port=8000)
