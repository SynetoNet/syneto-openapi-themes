"""Tests for the main module initialization and imports."""

import importlib
import sys
from unittest.mock import patch

import pytest

import syneto_openapi_themes


class TestModuleImports:
    """Test module import functionality."""

    def test_core_imports_available(self) -> None:
        """Test that core imports are available."""
        from syneto_openapi_themes import (
            SynetoBrandConfig,
            SynetoColors,
            SynetoTheme,
            get_default_brand_config,
            get_light_brand_config,
        )

        assert SynetoBrandConfig is not None
        assert SynetoColors is not None
        assert SynetoTheme is not None
        assert get_default_brand_config is not None
        assert get_light_brand_config is not None

    def test_documentation_classes_available(self) -> None:
        """Test that documentation classes are available."""
        from syneto_openapi_themes import (
            SynetoElements,
            SynetoRapiDoc,
            SynetoReDoc,
            SynetoScalar,
            SynetoSwaggerUI,
        )

        assert SynetoRapiDoc is not None
        assert SynetoSwaggerUI is not None
        assert SynetoReDoc is not None
        assert SynetoElements is not None
        assert SynetoScalar is not None

    def test_elements_available(self) -> None:
        """Test that Elements class is available."""
        from syneto_openapi_themes import SynetoElements

        assert SynetoElements is not None

    def test_version_available(self) -> None:
        """Test that version information is available."""
        assert hasattr(syneto_openapi_themes, "__version__")
        assert hasattr(syneto_openapi_themes, "__author__")
        assert hasattr(syneto_openapi_themes, "__email__")

        assert syneto_openapi_themes.__version__ == "0.1.0"
        assert syneto_openapi_themes.__author__ == "Syneto"
        assert syneto_openapi_themes.__email__ == "dev@syneto.net"

    def test_fastapi_conditional_import_success(self) -> None:
        """Test FastAPI imports when available."""
        try:
            from syneto_openapi_themes import (
                SynetoDocsManager,
                add_all_syneto_docs,
                add_syneto_elements,
                add_syneto_rapidoc,
                add_syneto_redoc,
                add_syneto_scalar,
                add_syneto_swagger,
            )

            # If we get here, FastAPI is available
            assert SynetoDocsManager is not None
            assert add_all_syneto_docs is not None
            assert add_syneto_elements is not None
            assert add_syneto_rapidoc is not None
            assert add_syneto_redoc is not None
            assert add_syneto_scalar is not None
            assert add_syneto_swagger is not None
        except ImportError:
            # FastAPI not available, which is fine
            pass

    def test_fastapi_conditional_import_failure(self) -> None:
        """Test behavior when FastAPI is not available."""
        # Mock FastAPI import failure
        with patch.dict(sys.modules, {"fastapi": None}):
            # Force reimport to trigger the ImportError path
            if "syneto_openapi_themes" in sys.modules:
                del sys.modules["syneto_openapi_themes"]
            if "syneto_openapi_themes.fastapi_integration" in sys.modules:
                del sys.modules["syneto_openapi_themes.fastapi_integration"]

            import syneto_openapi_themes

            # FastAPI integration should be None when not available
            assert syneto_openapi_themes.SynetoDocsManager is None
            assert syneto_openapi_themes.add_all_syneto_docs is None  # type: ignore[unreachable]

    def test_core_functionality_without_fastapi(self) -> None:
        """Test that core functionality works without FastAPI."""
        from syneto_openapi_themes import (
            get_default_brand_config,
        )

        # Test that we can create instances
        brand_config = get_default_brand_config()
        from syneto_openapi_themes import SynetoBrandConfig

        assert isinstance(brand_config, SynetoBrandConfig)

        # Test that we can create documentation instances
        from syneto_openapi_themes import (
            SynetoElements,
            SynetoRapiDoc,
            SynetoReDoc,
            SynetoScalar,
            SynetoSwaggerUI,
        )

        rapidoc = SynetoRapiDoc(brand_config=brand_config)
        swagger = SynetoSwaggerUI(brand_config=brand_config)
        redoc = SynetoReDoc(brand_config=brand_config)
        elements = SynetoElements(brand_config=brand_config)
        scalar = SynetoScalar(brand_config=brand_config)

        assert rapidoc is not None
        assert swagger is not None
        assert redoc is not None
        assert elements is not None
        assert scalar is not None

    def test_brand_config_integration(self) -> None:
        """Test brand configuration integration."""
        from syneto_openapi_themes import SynetoBrandConfig, SynetoElements

        brand_config = SynetoBrandConfig(
            primary_color="#ff0000",
            background_color="#000000",
        )

        elements = SynetoElements(brand_config=brand_config)
        assert elements.brand_config.primary_color == "#ff0000"
        assert elements.brand_config.background_color == "#000000"

    def test_conditional_imports_available(self) -> None:
        """Test that conditional imports work when dependencies are available."""
        try:
            from syneto_openapi_themes import (
                SynetoBrandConfig,  # noqa: F401
                SynetoElements,  # noqa: F401
                SynetoRapiDoc,  # noqa: F401
                SynetoReDoc,  # noqa: F401
                SynetoScalar,  # noqa: F401
                SynetoSwaggerUI,  # noqa: F401
            )

            # Verify all classes are importable and callable
            classes = [
                SynetoBrandConfig,
                SynetoElements,
                SynetoRapiDoc,
                SynetoReDoc,
                SynetoScalar,
                SynetoSwaggerUI,
            ]
            for cls in classes:
                assert callable(cls)
                assert hasattr(cls, "__name__")
        except ImportError:
            pytest.skip("FastAPI dependencies not available")


class TestModuleStructure:
    """Test module structure and organization."""

    def test_all_exports_defined(self) -> None:
        """Test that __all__ is properly defined."""
        assert hasattr(syneto_openapi_themes, "__all__")
        assert isinstance(syneto_openapi_themes.__all__, list)
        assert len(syneto_openapi_themes.__all__) > 0

    def test_all_exports_importable(self) -> None:
        """Test that all items in __all__ are importable."""
        for item in syneto_openapi_themes.__all__:
            assert hasattr(syneto_openapi_themes, item), f"Missing export: {item}"

    def test_circular_imports(self) -> None:
        """Test that there are no circular import issues."""
        try:
            # Test that we can import the main module without circular import issues
            import syneto_openapi_themes

            # If we get here, no circular imports
            assert syneto_openapi_themes is not None
        except ImportError as e:
            pytest.fail(f"Circular import detected: {e}")

    def test_namespace_pollution(self) -> None:
        """Test that the module doesn't pollute the namespace."""
        # Check that only intended attributes are public
        public_attrs = [attr for attr in dir(syneto_openapi_themes) if not attr.startswith("_")]

        # Exclude module imports that are not meant to be public exports
        excluded_attrs = {"brand", "elements", "rapidoc", "redoc", "scalar", "swagger", "fastapi_integration"}
        public_attrs = [attr for attr in public_attrs if attr not in excluded_attrs]

        for attr_name in public_attrs:
            assert attr_name in syneto_openapi_themes.__all__, f"Public attribute {attr_name} not in __all__"


class TestVersionCompatibility:
    """Test version and compatibility information."""

    def test_version_format(self) -> None:
        """Test that version follows semantic versioning."""
        version = syneto_openapi_themes.__version__
        parts = version.split(".")
        assert len(parts) >= 2, "Version should have at least major.minor"
        for part in parts:
            assert part.isdigit(), f"Version part '{part}' should be numeric"

    def test_metadata_types(self) -> None:
        """Test that metadata has correct types."""
        assert isinstance(syneto_openapi_themes.__version__, str)
        assert isinstance(syneto_openapi_themes.__author__, str)
        assert isinstance(syneto_openapi_themes.__email__, str)


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_graceful_import_failure_handling(self) -> None:
        """Test that import failures are handled gracefully."""
        # This test ensures the module can be imported even if dependencies fail
        assert hasattr(syneto_openapi_themes, "get_default_brand_config")
        assert hasattr(syneto_openapi_themes, "SynetoBrandConfig")

    def test_module_reload_safety(self) -> None:
        """Test that the module can be safely reloaded."""
        # Get initial state
        initial_version = syneto_openapi_themes.__version__
        config = syneto_openapi_themes.get_default_brand_config()

        # Reload module
        importlib.reload(syneto_openapi_themes)

        # Check that state is consistent
        assert syneto_openapi_themes.__version__ == initial_version
        new_config = syneto_openapi_themes.get_default_brand_config()
        assert type(config) is type(new_config)

    def test_import_error_resilience(self) -> None:
        """Test resilience to import errors."""
        # Test that core functionality works even if optional dependencies fail
        from syneto_openapi_themes import SynetoBrandConfig, get_default_brand_config

        config = get_default_brand_config()
        assert isinstance(config, SynetoBrandConfig)
