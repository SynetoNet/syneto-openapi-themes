"""
Basic usage example for Syneto OpenAPI Themes.

This example shows how to use the Syneto-branded documentation tools
with a simple FastAPI application.
"""

from fastapi import FastAPI
from syneto_openapi_themes import (
    SynetoBrandConfig,
    SynetoDocsManager,
    SynetoTheme,
    add_all_syneto_docs,
    add_syneto_rapidoc,
)

# Create FastAPI app
app = FastAPI(title="Example API", description="A sample API to demonstrate Syneto OpenAPI themes", version="1.0.0")


# Create some sample endpoints
@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Hello from Syneto Example API"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Get an item by ID."""
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(item: dict):
    """Create a new item."""
    return {"item": item, "status": "created"}


# Example 1: Basic usage with default Syneto branding
add_syneto_rapidoc(app, docs_url="/docs")

# Example 2: Custom brand configuration
custom_brand = SynetoBrandConfig(
    theme=SynetoTheme.LIGHT, company_name="Syneto Example", logo_url="/static/custom-logo.svg"
)

# Example 3: Add all documentation tools
add_all_syneto_docs(
    app,
    brand_config=custom_brand,
    rapidoc_url="/docs-rapidoc",
    swagger_url="/docs-swagger",
    redoc_url="/docs-redoc",
    elements_url="/docs-elements",
    scalar_url="/docs-scalar",
)

# Example 4: Using the docs manager (recommended approach)
docs_manager = SynetoDocsManager(app, brand_config=custom_brand)
docs_manager.add_all().add_docs_index("/documentation")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
