# Third Party
from invoke import task

# Our Libraries
from invoke_common_tasks import build, ci, format, lint, test, typecheck  # noqa


@task(pre=[format, ci], default=True)
def all(c):
    """Default development workflow."""
    ...
