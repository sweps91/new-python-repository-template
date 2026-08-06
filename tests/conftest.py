# from unittest.mock import patch

# import pytest


# @pytest.fixture(autouse=True, scope="session")
# def mock_bigquery_client():
#     with patch("example-service") as mock_client:
#         yield mock_client


# @pytest.fixture(autouse=True)
# def set_project_id(monkeypatch: pytest.MonkeyPatch):
#     monkeypatch.setenv("PROJECT_ID", "dev")
