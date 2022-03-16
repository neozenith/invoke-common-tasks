# Invoke Common Tasks

Some common tasks for PyInvoke to bootstrap your code quality and testing workflows.


## Getting Started

```sh
pip install invoke-common-tasks
```

### Invoke Setup

`tasks.py`

```python
from invoke_common_tasks import *
```

Once your `tasks.py` is setup like this `invoke` will have the extra commands:

```sh
λ invoke --list
Available tasks:

  build       Build wheel.
  ci          Run linting and test suite for Continuous Integration.
  format      Autoformat code for code style.
  lint        Linting and style checking.
  test        Run test suite.
  typecheck   Run typechecking tooling.
```


## The Tasks

### build

Assuming you are using `poetry` this will build a wheel (and only a wheel).

### format

This will apply code formatting tools `black` and `isort`.

These are only triggers for these commands, the specifics of configuration are up to you.

Recommended configuration in your `pyproject.toml`:

```toml
[tool.black]
line-length = 120

[tool.isort]
profile = "black"
multi_line_output = 3
import_heading_stdlib = "Standard Library"
import_heading_firstparty = "Our Libraries"
import_heading_thirdparty = "Third Party"
```

### lint

This will run checks for `black`, `isort` and `flake8`.

Up to you to specify your preferences of plugins for `flake8` and its configuration.

Recommended configuration in `.flake8`:

```ini
[flake8]
exclude = 
    venv,
    dist,
    .venv
select = ANN,B,B9,BLK,C,D,DAR,E,F,I,S,W
ignore = E203,E501,W503,D100,D104
per-file-ignores =
    tests/*: D103,S101
max-line-length = 120
max-complexity = 10
import-order-style = google
docstring-convention = google
```

Recommended `flake8` plugins:
 - [`flake8-docstrings`](https://pypi.org/project/flake8-docstrings/)

More `flake8` plugins:

https://github.com/DmytroLitvinov/awesome-flake8-extensions

### typecheck

Simply runs `mypy --pretty --show-error-codes .`.

Recommended configuration to add to your `pyproject.toml`

```toml
[tool.mypy]
pretty = true
show_error_codes = true
show_column_numbers = true
show_error_context = true
exclude = [
  'tests/',
  'tasks\.py'
]
follow_imports = 'silent'
ignore_missing_imports = true
# Work your way up to these:
disallow_incomplete_defs = true
# disallow_untyped_defs = true 
# strict = true
```

### test (and coverage)

This will simply run `python3 -m pytest`. This is important to run as a module instead of `pytest` since it resolves
a lot of import issues.

You can simply not import this task if you prefer something else. But all config and plugins are left flexible for your own desires, this simply triggers the entrypoint.

Recommended configuration in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-s -vvv --color=yes --cov=. --no-cov-on-fail"

[tool.coverage.run]
omit = ["tests/*", "**/__init__.py", "tasks.py"]
branch = true
```

Assuming you also install `pytest-cov` and `coverage[toml]`.

Recommended `pytest` plugins:
 - [`pytest-xdist`](https://pypi.org/project/pytest-xdist/) - Run tests in parallel using maximum cpu cores 
 - [`pytest-randomly`](https://pypi.org/project/pytest-randomly/) - Run tests in random order each time to detect tests with unintentional dependencies to each other that should be isolated. Each run prints out the seed if you need to reproduce an exact seeded run.
 - [`pytest-cov`](https://pypi.org/project/pytest-cov/) - It is recommended to run coverage from the `pytest` plugin.
 
List of other `pytest` plugins:

https://docs.pytest.org/en/latest/reference/plugin_list.html

### ci

This is a task with no commands but chains together `lint`, `typecheck` and `test`. 

## TODO

 - Auto-initialisations of some default config. 
    - eg `invoke format --init` should set config if not present


## Roadmap

This project will get marked as a stable v1.0 once the above TODO features are ticked off and this has seen at least 6 months in the wild in production.


## All Together

Once all the tasks are imported, you can create a custom task as your default task with runs a few tasks chained together.

```python
from invoke import task
from invoke_common_tasks import *

@task(pre=[format, lint, typecheck, test], default=True)
def all(c):
  """Default development loop."""
  ...
```

You will notice a few things here:

1. The method has no implementation `...`
1. We are chaining a series of `@task`s in the `pre=[...]` argument
1. The `default=True` on this root tasks means we could run either `invoke all` or simply `invoke`.

How cool is that?

# Contributing

At all times, you have the power to fork this project, make changes as you see fit and then:

```sh
pip install https://github.com/user/repository/archive/branch.zip
```
[Stackoverflow: pip install from github branch](https://stackoverflow.com/a/24811490/622276)

That way you can run from your own custom fork in the interim or even in-house your work and simply use this project as a starting point. That is totally ok.

However if you would like to contribute your changes back, then open a Pull Request "across forks".

Once your changes are merged and published you can revert to the canonical version of `pip install`ing this package.

If you're not sure how to make changes or if you should sink the time and effort, then open an Issue instead and we can have a chat to triage the issue.


# Resources

 - [`pyinvoke`](https://pyinvoke.org)

# Prior Art

 - https://github.com/Smile-SA/invoke-sphinx
 - https://github.com/Dashlane/dbt-invoke
 - https://invocations.readthedocs.io/en/latest/index.html

