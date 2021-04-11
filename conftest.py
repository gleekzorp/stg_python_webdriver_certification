import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def project_root() -> str:
    """ The Project (or Workspace) root as a filepath.
    * This conftest.py file should be in the Project Root if not already.
    """
    return os.path.dirname(os.path.abspath(__file__))
