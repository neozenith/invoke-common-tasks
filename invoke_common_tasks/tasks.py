# Third Party
from invoke import task
import shutil


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
def test(c):
    """Run test suite."""
    c.run("python3 -m pytest")


@task
def build(c):
    """Build wheel."""
    shutil.rmtree("dist/")
    c.run("poetry build -f wheel")
