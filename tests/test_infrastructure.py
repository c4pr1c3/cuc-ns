"""Test infrastructure validation to ensure testing setup works correctly."""

import sys
from pathlib import Path
import pytest
import numpy as np
import matplotlib
import sklearn


class TestInfrastructure:
    """Test class to validate testing infrastructure."""

    def test_python_version(self):
        """Test that Python version meets requirements."""
        assert sys.version_info >= (3, 8), "Python 3.8+ required"

    def test_required_packages_import(self):
        """Test that all required packages can be imported."""
        # Core dependencies
        import numpy
        import matplotlib.pyplot
        import sklearn
        import scipy
        
        # Test dependencies  
        import pytest
        import pytest_mock
        import pytest_cov

        assert True, "All required packages imported successfully"

    def test_fixtures_available(self, temp_dir, sample_data, mock_config):
        """Test that shared fixtures are working."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test sample_data fixture
        assert isinstance(sample_data, dict)
        assert "numbers" in sample_data
        assert sample_data["numbers"] == [1, 2, 3, 4, 5]
        
        # Test mock_config fixture
        assert isinstance(mock_config, dict)
        assert "debug" in mock_config
        assert mock_config["debug"] is False

    def test_numpy_functionality(self, numpy_random_seed):
        """Test basic numpy functionality with seeded randomness."""
        arr = np.random.rand(5)
        assert len(arr) == 5
        assert all(0 <= x <= 1 for x in arr)

    def test_matplotlib_backend(self):
        """Test that matplotlib uses non-interactive backend."""
        backend = matplotlib.get_backend()
        assert backend == 'Agg', f"Expected Agg backend, got {backend}"

    def test_project_structure(self):
        """Test that project structure is set up correctly."""
        project_root = Path(__file__).parent.parent
        
        # Check key files exist
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "conftest.py").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()

    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit marker works."""
        assert True

    @pytest.mark.integration  
    def test_integration_marker(self):
        """Test that integration marker works."""
        assert True

    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow marker works."""
        assert True

    def test_parametrized_fixture(self, boolean_parameter, numeric_parameter):
        """Test parametrized fixtures."""
        assert isinstance(boolean_parameter, bool)
        assert isinstance(numeric_parameter, int)
        assert numeric_parameter in [1, 10, 100]

    def test_mock_functionality(self, mocker):
        """Test that pytest-mock is working."""
        mock_func = mocker.Mock(return_value=42)
        result = mock_func()
        assert result == 42
        mock_func.assert_called_once()

    def test_coverage_source_paths(self):
        """Test that coverage is configured for the right paths."""
        project_root = Path(__file__).parent.parent
        ds_security_path = project_root / "ds-security"
        assert ds_security_path.exists(), "ds-security directory should exist for coverage"