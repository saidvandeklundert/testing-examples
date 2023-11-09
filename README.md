## Testing examples and notes

Testing is tedious but more fun with some easy examples.

Written as a lazydog for myself to remember how to do the things I regularly do but forget.

Tests are [here](https://github.com/saidvandeklundert/testing-examples/tree/main/tests).


You can pull down the repo and run all tests like so:

```
python -m pytest tests\.
```

All of the tests pass. Other options to run the tests are:

```
python -m pytest  .\tests\test_patch_dict.py
python -m pytest . -k 'test_divide_small_numbers_exception'
python -m pytest . --durations=5 -vv
python -m pytest . --durations=5 -vv
```




Random advice:
* Mock as little as possible. Mocking code means that there are fewer portions of your application that you are testing. In many cases it's possible to re-write your code to avoid needing to mock. Libraries such as moto (for mocking AWS resources) are also pretty handy. 
* Code coverage is nice to see how much of your code is being hit by your tests, but it's not everything. It's possible to have 100% coverage with poor tests.
* Fixtures are great! They allow you to reduce duplicate code between tests, and provide a mechanism for running setup/teardown code for your test regardless of whether it succeeds or fails. Definitely get handy with those
* pytest.mark.parametrize is powerful. Rather than writing 100s of identical tests, you can write a single test and pass in arbitrary values to use in your test.
* Think about how you plan to test code while you are writing the code and try to keep in mind what is easy to test and what is hard to test.
* some resources:
  - [what is mocking](https://realpython.com/python-mock-library/#what-is-mocking)
  - [Python testing with Pytest](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/)
  - [Fixture patterns](https://www.inspiredpython.com/article/five-advanced-pytest-fixture-patterns)