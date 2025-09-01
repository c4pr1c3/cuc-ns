"""Shared pytest fixtures for the testing suite."""

import tempfile
import shutil
from pathlib import Path
from typing import Generator, Any, Dict
from unittest.mock import Mock

import pytest
import numpy as np


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def temp_file(temp_dir: Path) -> Path:
    """Create a temporary file in the temp directory."""
    temp_file_path = temp_dir / "test_file.txt"
    temp_file_path.write_text("test content")
    return temp_file_path


@pytest.fixture
def sample_data() -> Dict[str, Any]:
    """Provide sample data for testing."""
    return {
        "numbers": [1, 2, 3, 4, 5],
        "labels": ["a", "b", "c"],
        "matrix": [[1, 2], [3, 4]],
        "config": {
            "enabled": True,
            "threshold": 0.8,
            "max_iterations": 100
        }
    }


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """Mock configuration for testing."""
    return {
        "debug": False,
        "log_level": "INFO",
        "data_path": "/tmp/test_data",
        "output_path": "/tmp/test_output",
        "model_params": {
            "learning_rate": 0.01,
            "batch_size": 32
        }
    }


@pytest.fixture
def numpy_random_seed():
    """Set numpy random seed for reproducible tests."""
    np.random.seed(42)
    yield
    # Reset to default random state after test
    np.random.seed(None)


@pytest.fixture
def mock_sklearn_dataset():
    """Mock sklearn dataset for testing ML components."""
    mock_data = Mock()
    mock_data.data = np.array([[1, 2], [3, 4], [5, 6]])
    mock_data.target = np.array([0, 1, 0])
    mock_data.feature_names = ["feature1", "feature2"]
    mock_data.target_names = ["class0", "class1"]
    return mock_data


@pytest.fixture
def mock_roc_data():
    """Mock ROC curve data for testing."""
    return {
        "y_true": np.array([0, 0, 1, 1]),
        "y_scores": np.array([0.1, 0.4, 0.35, 0.8]),
        "expected_fpr": np.array([0.0, 0.5, 0.5, 1.0]),
        "expected_tpr": np.array([0.0, 0.0, 0.5, 1.0])
    }


@pytest.fixture(autouse=True)
def disable_matplotlib_display():
    """Disable matplotlib display during tests."""
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend
    yield


@pytest.fixture
def capture_plots():
    """Capture matplotlib plots without displaying them."""
    import matplotlib.pyplot as plt
    plt.ioff()  # Turn off interactive mode
    yield
    plt.close('all')  # Close all figures after test


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Path to test data directory."""
    return Path(__file__).parent / "data"


@pytest.fixture
def mock_logger():
    """Mock logger for testing."""
    return Mock()


@pytest.fixture(params=[True, False])
def boolean_parameter(request):
    """Parametrized fixture for boolean testing."""
    return request.param


@pytest.fixture(params=[1, 10, 100])
def numeric_parameter(request):
    """Parametrized fixture for numeric testing.""" 
    return request.param