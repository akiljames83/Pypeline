# How to Upload to PyPI

## Pre-check

Make sure that the tests have been run and that the conda enviornment files and documentation have been updated:

```bash
$ ./scripts/run_tests.sh; 
$ ./scripts/conda_env.sh;
$ ./scripts/generate_docs.sh;
```

## Instructions

Below are the instructions to upload the pypeline project to PyPi:

1. Test the install

```bash
$ pip install -e .
```

2. Create the source distribution:

```bash
$ python setup.py sdist
```

3. Create the wheel for the project

```bash
$ python setup.py bdist_wheel --universal
```

4. Install twine (if not installed)

```bash
$ conda install twine
```

5. Push the update package to PyPI:

```bash
$ twine upload --verbose dist/*
```

## References:

- https://gist.github.com/arsho/fc651bfadd8a0f42be72156fd21bd8a9
- https://github.com/pypa/warehouse/issues/5890#issuecomment-494868157