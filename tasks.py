# Third Party
from invoke import task

# Our Libraries
from invoke_common_tasks import build, format, lint, test  # noqa


@task(pre=[format, lint, test], default=True)
def dev(c):
    """Default development workflow."""
    ...
