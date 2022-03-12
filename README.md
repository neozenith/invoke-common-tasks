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

  build    Build wheel.
  ci       Run linting and test suite for Continuous Integration.
  format   Autoformat code for code style.
  lint     Linting and style checking.
  test     Run test suite.
```


## The Tasks

### build

Assuming you are using `poetry` this will build a wheel.

### format

This will apply code formatting tools `black` and `isort`.

These are only triggers for these commands, the specifics of configuration are up to you.

### lint

This will run checks for `black`, `isort` and `flake8`.

Up to you to specify your preferences of plugins for `flake8` and its configuration.

### test

This will simply run `python3 -m pytest`. This is important to run as a module instead of `pytest` since it resolves
a lot of import issues.

You can simply not import this task if you prefer something else. But all config and plugins are left flexible for your own desires, this simply triggers the entrypoint.

### ci

This is a task with no commands but chains together `lint` and `test`. 

## TODO

 - typechecking
 - test coverage

Also auto-initialisations of some default config.


## All Together

Once all the tasks are imported, you can create a custom task as your default task with runs a few tasks chained together.

```python
from invoke import task
from invoke_common_tasks import *

@task(pre=[format, lint, test], default=True)
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

Open an issue and lets have a chat to triage needs or concerns before you sink too much effort on a PR.

Or if you're pretty confident your change is inline with the direction of this project then go ahead and open that PR.

Or feel free to fork this project and rename it to your own variant. It's cool, I don't mind.

# Resources

 - [`pyinvoke`](https://pyinvoke.org)

# Prior Art

 - https://github.com/Smile-SA/invoke-sphinx
 - https://github.com/Dashlane/dbt-invoke
 - https://invocations.readthedocs.io/en/latest/index.html

