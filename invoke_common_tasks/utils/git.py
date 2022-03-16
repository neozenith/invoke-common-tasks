# Standard Library
from functools import lru_cache

# Third Party
from invoke import run


@lru_cache(maxsize=None)
def git_current_branch() -> str:
    """Get the current git branch."""
    return run("git branch --show-current", hide=True).stdout.strip()
