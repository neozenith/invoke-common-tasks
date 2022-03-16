# Standard Library
import os
from functools import lru_cache
from pathlib import Path
from subprocess import CompletedProcess, run
from typing import List, Optional

# Third Party
from poetry.core.factory import Factory
from poetry.core.masonry.builders.wheel import WheelBuilder
from poetry.core.poetry import Poetry


@lru_cache(maxsize=None)
def poetry_project(path: str = ".") -> Poetry:
    """Get an instance of the current Poetry project.

    This is cached so that subsequent calls in the same invoke session reduce interactions with disk.
    """
    poetry = Factory().create_poetry(Path(path).resolve())
    return poetry


@lru_cache(maxsize=None)
def poetry_project_name(path: str = ".") -> str:
    """Get the name of the current Poerty project."""
    return poetry_project(path).pyproject.poetry_config["name"]


@lru_cache(maxsize=None)
def poetry_project_version(path: str = ".") -> str:
    """Get the version of the current Poerty project."""
    return poetry_project(path).pyproject.poetry_config["version"]


@lru_cache(maxsize=None)
def poetry_wheel_builder(path: str = ".") -> WheelBuilder:
    """Get poetry WheelBuilder instance."""
    return WheelBuilder(poetry_project(path))


@lru_cache(maxsize=None)
def poetry_wheelname(path: str = ".") -> str:
    """Get poetry properly formatted wheelname from WheelBuilder instance."""
    builder = poetry_wheel_builder(path)
    return builder.wheel_filename


def __selected_projects(projects: Optional[str], search_dir: str = ".") -> List[str]:
    """Produce a set of either all projects or a validated single project."""
    # Collect list of dirs that are valid projects
    d = search_dir
    all_projects = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d, o)) and not o.startswith(".")]
    _projects = projects.split(",") if projects is not None else None
    validated_projects = []

    # Reconcile list of projects to apply command to
    if _projects is not None:
        difference = set(_projects) - set(all_projects)
        if difference == set():  # _projects is subset of all_projects
            validated_projects = _projects
        else:
            raise ValueError(f"The project '{list(difference)}' is not one of {all_projects}")
    else:
        validated_projects = all_projects

    return validated_projects


def __run_in_subproject(command: str, project_path: str) -> CompletedProcess:
    """Run a command in a poetry sub project."""
    target_venv_path = Path(os.environ["VIRTUAL_ENV"]).parent / project_path / ".venv"
    target_bin_path = str(target_venv_path / "bin")
    target_cwd = str(Path().cwd() / project_path)
    target_path = ":".join([target_bin_path] + os.environ["PATH"].split(":"))

    # Curate new ENV to coerce poetry into picking the subproject venv
    ENV = {"VIRTUAL_ENV": str(target_venv_path), "PATH": target_path}

    result = run(
        command,
        cwd=target_cwd,
        shell=True,
        capture_output=True,
        env=ENV,
    )
    return result
