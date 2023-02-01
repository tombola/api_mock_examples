#Setup

Uses [direnv](https://direnv.net/) to set PYTHONPATH (from `.envrc`).

Set `EXPLORE_RESPONSES` to explore the object returned by requests.

```py
# Run the fake API
flask --app dummy_api run

# Record the output of the API
pytest tests/test_responses_record_mocks.py -s

# Run the test against recorded output
pytest tests/test_responses_mocks.py -s
```