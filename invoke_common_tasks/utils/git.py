# Standard Library
from functools import lru_cache

# Third Party
from invoke import run


@lru_cache(maxsize=None)
def git_current_branch() -> str:
    """Get the current git branch."""
    #  return run("git branch --show-current", hide=True).stdout.strip()
    # git 2.22+ supports the above command but to get backwards compatability need to use the below command.
    # https://stackoverflow.com/a/6245587/622276
    return run("git rev-parse --abbrev-ref HEAD", hide=True).stdout.strip()
