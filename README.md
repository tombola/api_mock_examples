#Setup

Uses [direnv](https://direnv.net/) to set PYTHONPATH (from `.envrc`).

Set `EXPLORE_RESPONSES` env var to explore the object returned by requests.

```py

# Optional
export EXPLORE_RESPONSES=1

# Run the fake API
flask --app dummy_api run

# Record the output of the API
pytest tests/test_responses_record_mocks.py
# or
pytest -m record

# Run the test against recorded output
pytest tests/test_responses_mocks.py
# or
pytest -m dummy

```