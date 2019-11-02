# Python Package Skeleton

After initializing a new project from this skeleton:

## Create a virtual environment

```sh
./scripts/create_venv.py
```

Activate virtual environment:

```sh
. ./venv/bin/activate
```

## Install requirements

```sh
./scripts/install_test_requirements.py
```

## Unit test

```sh
./scripts/test.py
```

## Build wheel (outside virtual environment)

```sh
python setup.py sdist bdist_wheel
```
