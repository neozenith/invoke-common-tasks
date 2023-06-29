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
    branch_name = run("git rev-parse --abbrev-ref HEAD", hide=True).stdout.strip()

    # When using Jenkins or other CI systems, if they checkout a commit hash it is in a detached HEAD state
    # So no branch name will resolve even if there is a branch name associated with that commit hash.
    # So if the above returns the default "HEAD", then we resort to the short hash as a meaningful pointer.
    # https://stackoverflow.com/questions/6245570/how-to-get-the-current-branch-name-in-git#comment50696859_11868440
    if branch_name == "HEAD":
        branch_name = run("git rev-parse --short HEAD", hide=True).stdout.strip()

    return branch_name
