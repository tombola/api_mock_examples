"""Test cases for the __main__ module."""
import pytest
import responses
import tomllib as _toml  # type: ignore[no-redef]
from responses import _recorder
from responses.matchers import fragment_identifier_matcher
from rich import print
from utils import explore

from dummy_api import API_URL, PRODUCTS_API_URL
import dummy_service as service


@responses.activate
def test_responses_recording():
    responses.patch(API_URL)
    responses._add_from_file(file_path="recorded_responses/test_responses_recording.toml")
    response = service.get_products()
    explore(response)
    print(response.json())

    assert response.status_code == 200
