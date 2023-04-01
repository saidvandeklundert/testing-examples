## Testing examples and notes

Testing is tedious but more fun with some easy examples.

Written as a lazydog for me to remember how to do the things I regularly do but forget.

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