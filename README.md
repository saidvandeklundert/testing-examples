## Testing examples and notes


```
python -m pytest .
python -m pytest . --durations=0
python -m pytest . --durations=0 -vv
python -m pytest . --durations=5 -vv
python -m mypy src
```

Repository with some notes and examples on testing

- Testing types and a simple unit test x

- Mocks: mocking a function and mocking a class
  - what is a mock
  - mocking a function
  - mocking a class

- Mocks: lots of short mock examples:
  - function
  - class
  - dict
  - building a mock with nested othter mocks

- Pytest: high-level and configuration overview
  - what is pytest?
  - running pytest
  - config options

- test exceptions

- Pytest: fixtures
  - what is a fixture?
  - scopes of fixtures
  - conftest.py
  - make fixture return copy in case of reference types
  - fixture can use fixture

- Pytest: paramatrization
  - testing a function with many variable x
  - feeding the paramatrized function a list of tuples x
  - feed a zip of 2 lists x 

- Pytest: side-effects
  - what is a side effect?
  - how to test a side-effect

- Pytest: test CLI tool
  - example cli tool
  - example test-case


- pytest --pdb 

- use tempfile

- pytest's caplog fixture for logging during testing

- capture stdout

- mark tests

- monkeypatch