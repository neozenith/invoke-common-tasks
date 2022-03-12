# Third Party
from invoke import task

# Our Libraries
from invoke_common_tasks import build, ci, format, lint, test  # noqa


@task(pre=[format, lint, test], default=True)
def all(c):
    """Default development workflow."""
    ...
