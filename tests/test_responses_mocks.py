"""Test cases for the __main__ module."""
import pytest
import responses
import tomllib as _toml  # type: ignore[no-redef]

from rich import print
from utils import explore

from dummy_api import API_URL, PRODUCTS_API_URL
import dummy_service as service
import requests

@pytest.mark.dummy
@responses.activate
def test_mocked_response():
    responses.patch(API_URL)
    responses._add_from_file(file_path="recorded_responses/test_responses_recording.toml")

    response = service.get_products()
    explore(response)
    print(response.json())

    assert response.status_code == 200


@pytest.mark.dummy
@responses.activate
def test_mocked_response_with_arbitrary_query():
    responses.patch(API_URL)
    responses._add_from_file(file_path="recorded_responses/test_responses_recording.toml")

    response = requests.get(PRODUCTS_API_URL + "?q=2&something")
    explore(response)
    print(response.json())

    assert response.status_code == 200
