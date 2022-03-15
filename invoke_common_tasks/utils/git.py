# Standard Library
from functools import lru_cache

# Third Party
from invoke import run

POLL_DELAY = 5


@lru_cache(maxsize=None)
def git_current_branch():
    """Get the current git branch."""
    return run("git branch --show-current", hide=True).stdout.strip()
