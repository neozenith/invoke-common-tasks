# Third Party
from invoke import task

# Our Libraries
from invoke_common_tasks import (  # noqa
    build,
    ci,
    format,
    init_config,
    lint,
    test,
    typecheck,
)


@task(pre=[format, ci], default=True)
def all(c):
    """Default development workflow."""
    ...


@task
def toc(c):
    """Automate documentation tasks."""
    c.run("md_toc --in-place github --header-levels 4 README.md")
