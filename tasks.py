# Third Party
from invoke import task

# Our Libraries
from invoke_common_tasks import build, ci, format, lint, test, typecheck  # noqa

# NOTE: Invoke tasks files don't support mypy typechecking for the forseeable future
# They were looking at addressing it after Python2 EOL 01-01-2020 but there was a global pandemic.
# https://github.com/pyinvoke/invoke/issues/357


@task(pre=[format, ci], default=True)
def all(c):
    """Default development workflow."""
    ...
