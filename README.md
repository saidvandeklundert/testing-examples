## Testing examples and notes

Testing is tedious but more fun with some easy examples.

You can pull down the repo and run all tests like so:
```
python -m pytest .
```

All of the tests pass. Other options to run the tests are:

```
python -m pytest  .\tests\test_patch_dict.py
python -m pytest . --durations=5 -vv
python -m pytest . --durations=5 -vv
python -m mypy src
```



## Todo:

- Testing types and a simple unit test x

- Mocks: mocking a function and mocking a class
  - what is a mock
  - mocking a function
  - mocking a class

- Mocks: lots of short mock examples:
  - function x
  - class
  - class method
  - dict x
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

- capture stdout x

- mark tests

- monkeypatch