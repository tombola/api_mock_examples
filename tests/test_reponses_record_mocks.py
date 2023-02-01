"""Test cases for the __main__ module."""
import pytest
from rich import print
from responses import _recorder
import dummy_service as service
from utils import explore

@_recorder.record(file_path="recorded_responses/test_responses_recording.toml")
def test_responses_recording_record():
    response = service.get_products()
    explore(response)