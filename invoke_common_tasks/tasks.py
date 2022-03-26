# Standard Library
import shutil

# Third Party
from invoke import task

from .utils.config import (
    add_format_config,
    add_test_config,
    add_typecheck_config,
    write_lint_config,
)
from .utils.poetry import poetry_project

# NOTE: Invoke tasks files don't support mypy typechecking for the forseeable future
# They were looking at addressing it after Python2 EOL 01-01-2020 but there was a global pandemic.
# https://github.com/pyinvoke/invoke/issues/357


@task
def format(c):
    """Autoformat code for code style."""
    c.run("black .")
    c.run("isort .")


@task
def lint(c):
    """Linting and style checking."""
    c.run("black --check .")
    c.run("isort --check .")
    c.run("flake8 .")


@task
def typecheck(c):
    """Run typechecking tooling."""
    c.run("mypy .")


@task
def test(c):
    """Run test suite."""
    c.run("python3 -m pytest")


@task
def build(c):
    """Build wheel."""
    shutil.rmtree("dist/", ignore_errors=True)
    c.run("poetry build -f wheel")


@task(pre=[lint, typecheck, test])
def ci(c):
    """Run linting and test suite for Continuous Integration."""
    ...


@task
def init_config(c, format=False, lint=False, test=False, typecheck=False, all=False):
    """Setup default configuration for development tooling."""
    if all:
        format = True
        lint = True
        typecheck = True
        test = True

    print("Initialise config options selected:")
    print(f"format:    {format}")
    print(f"lint:      {lint}")
    print(f"typecheck: {typecheck}")
    print(f"test:      {test}")

    project = poetry_project()
    pyproject = project.pyproject

    if format:
        print("Adding format config...")
        add_format_config(pyproject)

    if lint:
        print("Adding linting config...")
        write_lint_config()

    if typecheck:
        print("Adding typecheck config...")
        add_typecheck_config(pyproject)

    if test:
        print("Adding test config...")
        add_test_config(pyproject)

    print("Saving updated config...")
    pyproject.save()
