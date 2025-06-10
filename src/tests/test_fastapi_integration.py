"""
Tests for FastAPI integration utilities.
"""

from unittest.mock import Mock, patch

from fastapi import FastAPI
from fastapi.testclient import TestClient
from syneto_openapi_themes.brand import SynetoBrandConfig, SynetoTheme
from syneto_openapi_themes.fastapi_integration import (
    SynetoDocsManager,
    add_all_syneto_docs,
    add_syneto_elements,
    add_syneto_rapidoc,
    add_syneto_redoc,
    add_syneto_scalar,
    add_syneto_swagger,
)


class TestFastAPIIntegrationFunctions:
    """Test FastAPI integration functions."""

    def test_add_syneto_rapidoc_default_params(self):
        """Test adding RapiDoc with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoRapiDoc") as mock_rapidoc:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>RapiDoc</html>"
            mock_rapidoc.return_value = mock_instance

            add_syneto_rapidoc(app)

            # Verify RapiDoc was initialized correctly
            mock_rapidoc.assert_called_once_with(
                openapi_url="/openapi.json", title="Test API - API Documentation", brand_config=None
            )

            # Verify route was added (FastAPI may add default docs route too)
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/docs"]
            assert len(routes) >= 1

    def test_add_syneto_rapidoc_custom_params(self):
        """Test adding RapiDoc with custom parameters."""
        app = FastAPI(title="Custom API")
        brand_config = SynetoBrandConfig(primary_color="#custom")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoRapiDoc") as mock_rapidoc:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>Custom RapiDoc</html>"
            mock_rapidoc.return_value = mock_instance

            add_syneto_rapidoc(
                app,
                openapi_url="/custom/openapi.json",
                docs_url="/custom-docs",
                title="Custom Title",
                brand_config=brand_config,
                custom_param="test",
            )

            # Verify RapiDoc was initialized with custom parameters
            mock_rapidoc.assert_called_once_with(
                openapi_url="/custom/openapi.json", title="Custom Title", brand_config=brand_config, custom_param="test"
            )

            # Verify custom route was added
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/custom-docs"]
            assert len(routes) == 1

    def test_add_syneto_swagger_default_params(self):
        """Test adding SwaggerUI with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoSwaggerUI") as mock_swagger:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>SwaggerUI</html>"
            mock_swagger.return_value = mock_instance

            add_syneto_swagger(app)

            # Verify SwaggerUI was initialized correctly
            mock_swagger.assert_called_once_with(
                openapi_url="/openapi.json", title="Test API - API Documentation", brand_config=None
            )

            # Verify route was added
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/swagger"]
            assert len(routes) == 1

    def test_add_syneto_swagger_custom_params(self):
        """Test adding SwaggerUI with custom parameters."""
        app = FastAPI(title="Custom API")
        brand_config = SynetoBrandConfig(theme=SynetoTheme.LIGHT)

        with patch("syneto_openapi_themes.fastapi_integration.SynetoSwaggerUI") as mock_swagger:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>Custom SwaggerUI</html>"
            mock_swagger.return_value = mock_instance

            add_syneto_swagger(
                app,
                openapi_url="/api/openapi.json",
                docs_url="/swagger-ui",
                title="Swagger Documentation",
                brand_config=brand_config,
            )

            # Verify SwaggerUI was initialized with custom parameters
            mock_swagger.assert_called_once_with(
                openapi_url="/api/openapi.json", title="Swagger Documentation", brand_config=brand_config
            )

    def test_add_syneto_redoc_default_params(self):
        """Test adding ReDoc with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoReDoc") as mock_redoc:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>ReDoc</html>"
            mock_redoc.return_value = mock_instance

            add_syneto_redoc(app)

            # Verify ReDoc was initialized correctly
            mock_redoc.assert_called_once_with(
                openapi_url="/openapi.json", title="Test API - API Documentation", brand_config=None
            )

            # Verify route was added (FastAPI may add default redoc route too)
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/redoc"]
            assert len(routes) >= 1

    def test_add_syneto_elements_default_params(self):
        """Test adding Elements with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoElements") as mock_elements:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>Elements</html>"
            mock_elements.return_value = mock_instance

            add_syneto_elements(app)

            # Verify Elements was initialized correctly
            mock_elements.assert_called_once_with(
                openapi_url="/openapi.json", title="Test API - API Documentation", brand_config=None
            )

            # Verify route was added
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/elements"]
            assert len(routes) == 1

    def test_add_syneto_scalar_default_params(self):
        """Test adding Scalar with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.SynetoScalar") as mock_scalar:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>Scalar</html>"
            mock_scalar.return_value = mock_instance

            add_syneto_scalar(app)

            # Verify Scalar was initialized correctly
            mock_scalar.assert_called_once_with(
                openapi_url="/openapi.json", title="Test API - API Documentation", brand_config=None
            )

            # Verify route was added
            routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/scalar"]
            assert len(routes) == 1

    def test_add_all_syneto_docs_default_params(self):
        """Test adding all documentation tools with default parameters."""
        app = FastAPI(title="Test API")

        with (
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc") as mock_rapidoc,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_swagger") as mock_swagger,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_redoc") as _mock_redoc,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_elements") as _mock_elements,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_scalar") as _mock_scalar,
        ):

            add_all_syneto_docs(app)

            # Verify all documentation tools were added
            mock_rapidoc.assert_called_once_with(app, openapi_url="/openapi.json", docs_url="/docs", brand_config=None)
            mock_swagger.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/swagger", brand_config=None
            )
            _mock_redoc.assert_called_once_with(app, openapi_url="/openapi.json", docs_url="/redoc", brand_config=None)
            _mock_elements.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/elements", brand_config=None
            )
            _mock_scalar.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/scalar", brand_config=None
            )

    def test_add_all_syneto_docs_custom_params(self):
        """Test adding all documentation tools with custom parameters."""
        app = FastAPI(title="Custom API")
        brand_config = SynetoBrandConfig(primary_color="#custom")

        with (
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc") as mock_rapidoc,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_swagger") as mock_swagger,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_redoc") as _mock_redoc,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_elements") as _mock_elements,
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_scalar") as _mock_scalar,
        ):

            add_all_syneto_docs(
                app,
                openapi_url="/custom/openapi.json",
                brand_config=brand_config,
                rapidoc_url="/custom-docs",
                swagger_url="/custom-swagger",
                redoc_url="/custom-redoc",
                elements_url="/custom-elements",
                scalar_url="/custom-scalar",
                custom_param="test",
            )

            # Verify all documentation tools were added with custom parameters
            mock_rapidoc.assert_called_once_with(
                app,
                openapi_url="/custom/openapi.json",
                docs_url="/custom-docs",
                brand_config=brand_config,
                custom_param="test",
            )
            mock_swagger.assert_called_once_with(
                app,
                openapi_url="/custom/openapi.json",
                docs_url="/custom-swagger",
                brand_config=brand_config,
                custom_param="test",
            )


class TestSynetoDocsManager:
    """Test SynetoDocsManager class."""

    def test_initialization_default_params(self):
        """Test SynetoDocsManager initialization with default parameters."""
        app = FastAPI(title="Test API")

        with patch("syneto_openapi_themes.fastapi_integration.get_default_brand_config") as mock_get_default:
            mock_brand_config = Mock()
            mock_get_default.return_value = mock_brand_config

            manager = SynetoDocsManager(app)

            assert manager.app is app
            assert manager.brand_config is mock_brand_config
            assert manager.openapi_url == "/openapi.json"
            assert manager._docs_endpoints == {}

    def test_initialization_custom_params(self):
        """Test SynetoDocsManager initialization with custom parameters."""
        app = FastAPI(title="Custom API")
        brand_config = SynetoBrandConfig(primary_color="#custom")

        manager = SynetoDocsManager(app, brand_config=brand_config, openapi_url="/custom/openapi.json")

        assert manager.app is app
        assert manager.brand_config is brand_config
        assert manager.openapi_url == "/custom/openapi.json"
        assert manager._docs_endpoints == {}

    def test_add_rapidoc(self):
        """Test adding RapiDoc through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc") as mock_add:
            result = manager.add_rapidoc("/custom-docs", custom_param="test")

            # Verify method chaining
            assert result is manager

            # Verify add_syneto_rapidoc was called correctly
            mock_add.assert_called_once_with(
                app,
                openapi_url="/openapi.json",
                docs_url="/custom-docs",
                brand_config=manager.brand_config,
                custom_param="test",
            )

            # Verify endpoint was registered
            assert manager._docs_endpoints["rapidoc"] == "/custom-docs"

    def test_add_swagger(self):
        """Test adding SwaggerUI through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_swagger") as mock_add:
            result = manager.add_swagger("/swagger-ui")

            # Verify method chaining
            assert result is manager

            # Verify add_syneto_swagger was called correctly
            mock_add.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/swagger-ui", brand_config=manager.brand_config
            )

            # Verify endpoint was registered
            assert manager._docs_endpoints["swagger"] == "/swagger-ui"

    def test_add_redoc(self):
        """Test adding ReDoc through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_redoc") as mock_add:
            result = manager.add_redoc()

            # Verify method chaining
            assert result is manager

            # Verify add_syneto_redoc was called correctly
            mock_add.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/redoc", brand_config=manager.brand_config
            )

            # Verify endpoint was registered
            assert manager._docs_endpoints["redoc"] == "/redoc"

    def test_add_elements(self):
        """Test adding Elements through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_elements") as mock_add:
            result = manager.add_elements("/elements-docs")

            # Verify method chaining
            assert result is manager

            # Verify add_syneto_elements was called correctly
            mock_add.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/elements-docs", brand_config=manager.brand_config
            )

            # Verify endpoint was registered
            assert manager._docs_endpoints["elements"] == "/elements-docs"

    def test_add_scalar(self):
        """Test adding Scalar through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_scalar") as mock_add:
            result = manager.add_scalar("/scalar-docs")

            # Verify method chaining
            assert result is manager

            # Verify add_syneto_scalar was called correctly
            mock_add.assert_called_once_with(
                app, openapi_url="/openapi.json", docs_url="/scalar-docs", brand_config=manager.brand_config
            )

            # Verify endpoint was registered
            assert manager._docs_endpoints["scalar"] == "/scalar-docs"

    def test_add_all(self):
        """Test adding all documentation tools through manager."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        with (
            patch.object(manager, "add_rapidoc") as mock_rapidoc,
            patch.object(manager, "add_swagger") as mock_swagger,
            patch.object(manager, "add_redoc") as mock_redoc,
            patch.object(manager, "add_elements") as mock_elements,
            patch.object(manager, "add_scalar") as mock_scalar,
        ):

            # Configure mocks to return manager for chaining
            mock_rapidoc.return_value = manager
            mock_swagger.return_value = manager
            mock_redoc.return_value = manager
            mock_elements.return_value = manager
            mock_scalar.return_value = manager

            result = manager.add_all(custom_param="test")

            # Verify method chaining
            assert result is manager

            # Verify all methods were called with custom parameters
            mock_rapidoc.assert_called_once_with(custom_param="test")
            mock_swagger.assert_called_once_with(custom_param="test")
            mock_redoc.assert_called_once_with(custom_param="test")
            mock_elements.assert_called_once_with(custom_param="test")
            mock_scalar.assert_called_once_with(custom_param="test")

    def test_add_docs_index(self):
        """Test adding documentation index page."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        # Add some endpoints first
        manager._docs_endpoints = {"rapidoc": "/docs", "swagger": "/swagger", "redoc": "/redoc"}

        result = manager.add_docs_index("/docs-index")

        # Verify method chaining
        assert result is manager

        # Verify route was added
        routes = [route for route in app.routes if hasattr(route, "path") and route.path == "/docs-index"]
        assert len(routes) == 1

    def test_render_docs_index(self):
        """Test rendering documentation index page."""
        app = FastAPI(title="Test API")
        brand_config = SynetoBrandConfig(primary_color="#test123", background_color="#bg456", text_color="#text789")
        manager = SynetoDocsManager(app, brand_config=brand_config)

        # Add some endpoints
        manager._docs_endpoints = {"rapidoc": "/docs", "swagger": "/swagger-ui", "redoc": "/redoc"}

        result = manager._render_docs_index()

        # Verify HTML structure
        assert "<!DOCTYPE html>" in result
        assert "Test API - API Documentation" in result
        assert "#test123" in result
        assert "#bg456" in result
        assert "#text789" in result

        # Verify endpoints are included
        assert "/docs" in result
        assert "/swagger-ui" in result
        assert "/redoc" in result
        assert "Rapidoc" in result
        assert "Swagger" in result
        assert "Redoc" in result

    def test_render_docs_index_empty_endpoints(self):
        """Test rendering documentation index page with no endpoints."""
        app = FastAPI(title="Empty API")
        manager = SynetoDocsManager(app)

        result = manager._render_docs_index()

        # Verify basic HTML structure is still present
        assert "<!DOCTYPE html>" in result
        assert "Empty API - API Documentation" in result
        assert "docs-grid" in result

    def test_endpoints_property(self):
        """Test endpoints property returns copy of endpoints."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        # Add some endpoints
        manager._docs_endpoints = {"rapidoc": "/docs", "swagger": "/swagger"}

        endpoints = manager.endpoints

        # Verify it's a copy
        assert endpoints == manager._docs_endpoints
        assert endpoints is not manager._docs_endpoints

        # Verify modifying the returned dict doesn't affect the original
        endpoints["new"] = "/new"
        assert "new" not in manager._docs_endpoints

    def test_manager_integration_workflow(self):
        """Test complete workflow using manager."""
        app = FastAPI(title="Integration Test API")
        brand_config = SynetoBrandConfig(primary_color="#integration")

        with (
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc"),
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_swagger"),
            patch("syneto_openapi_themes.fastapi_integration.add_syneto_redoc"),
        ):

            manager = SynetoDocsManager(app, brand_config=brand_config)

            # Chain multiple operations
            result = (
                manager.add_rapidoc("/api-docs")
                .add_swagger("/swagger-ui")
                .add_redoc("/redoc-ui")
                .add_docs_index("/docs")
            )

            # Verify chaining worked
            assert result is manager

            # Verify all endpoints were registered
            assert manager.endpoints == {"rapidoc": "/api-docs", "swagger": "/swagger-ui", "redoc": "/redoc-ui"}


class TestFastAPIIntegrationEdgeCases:
    """Test edge cases and error conditions."""

    def test_add_docs_with_none_title(self):
        """Test adding docs when app title is None."""
        app = FastAPI()  # No title provided
        app.title = None

        with patch("syneto_openapi_themes.fastapi_integration.SynetoRapiDoc") as mock_rapidoc:
            mock_instance = Mock()
            mock_instance.render.return_value = "<html>RapiDoc</html>"
            mock_rapidoc.return_value = mock_instance

            add_syneto_rapidoc(app)

            # Should handle None title gracefully
            mock_rapidoc.assert_called_once_with(
                openapi_url="/openapi.json", title="None - API Documentation", brand_config=None
            )

    def test_manager_with_custom_openapi_url(self):
        """Test manager with custom OpenAPI URL."""
        app = FastAPI(title="Custom API")
        manager = SynetoDocsManager(app, openapi_url="/v2/openapi.json")

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc") as mock_add:
            manager.add_rapidoc()

            # Verify custom OpenAPI URL was used
            mock_add.assert_called_once_with(
                app, openapi_url="/v2/openapi.json", docs_url="/docs", brand_config=manager.brand_config
            )

    def test_docs_index_with_special_characters_in_title(self):
        """Test docs index with special characters in app title."""
        app = FastAPI(title="Test & <Special> API")
        manager = SynetoDocsManager(app)

        result = manager._render_docs_index()

        # Verify special characters are handled properly
        assert "Test &amp; &lt;Special&gt; API" in result or "Test & <Special> API" in result

    def test_manager_endpoints_isolation(self):
        """Test that different manager instances have isolated endpoints."""
        app1 = FastAPI(title="API 1")
        app2 = FastAPI(title="API 2")

        manager1 = SynetoDocsManager(app1)
        manager2 = SynetoDocsManager(app2)

        with patch("syneto_openapi_themes.fastapi_integration.add_syneto_rapidoc"):
            manager1.add_rapidoc("/docs1")
            manager2.add_rapidoc("/docs2")

            # Verify endpoints are isolated
            assert manager1.endpoints == {"rapidoc": "/docs1"}
            assert manager2.endpoints == {"rapidoc": "/docs2"}


class TestFastAPIIntegrationWithTestClient:
    """Test FastAPI integration with actual HTTP requests using TestClient."""

    def test_fastapi_integration_with_test_client_rapidoc(self):
        """Test RapiDoc endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API", docs_url=None, redoc_url=None)  # Disable default docs
        add_syneto_rapidoc(app, docs_url="/rapidoc")

        client = TestClient(app)
        response = client.get("/rapidoc")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        # Just verify it's HTML content - the actual implementation might vary
        assert "<html" in response.text.lower()

    def test_fastapi_integration_with_test_client_swagger(self):
        """Test SwaggerUI endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API")
        add_syneto_swagger(app, docs_url="/swagger")

        client = TestClient(app)
        response = client.get("/swagger")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        assert "swagger" in response.text.lower()

    def test_fastapi_integration_with_test_client_redoc(self):
        """Test ReDoc endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API", docs_url=None, redoc_url=None)  # Disable default docs
        add_syneto_redoc(app, docs_url="/redoc-custom")

        client = TestClient(app)
        response = client.get("/redoc-custom")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        assert "redoc" in response.text.lower()

    def test_fastapi_integration_with_test_client_elements(self):
        """Test Elements endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API")
        add_syneto_elements(app, docs_url="/elements")

        client = TestClient(app)
        response = client.get("/elements")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        assert "elements" in response.text.lower()

    def test_fastapi_integration_with_test_client_scalar(self):
        """Test Scalar endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API")
        add_syneto_scalar(app, docs_url="/scalar")

        client = TestClient(app)
        response = client.get("/scalar")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        assert "scalar" in response.text.lower()

    def test_docs_manager_index_with_test_client(self):
        """Test docs manager index endpoint returns HTML response via TestClient."""
        app = FastAPI(title="Test API")
        manager = SynetoDocsManager(app)

        # Add some documentation endpoints first
        manager.add_rapidoc("/docs").add_swagger("/swagger")
        manager.add_docs_index("/docs-index")

        client = TestClient(app)
        response = client.get("/docs-index")

        assert response.status_code == 200
        assert response.headers["content-type"] == "text/html; charset=utf-8"
        assert "<!DOCTYPE html>" in response.text or "<!doctype html>" in response.text
        assert "Test API - API Documentation" in response.text
        assert "/docs" in response.text
        assert "/swagger" in response.text
