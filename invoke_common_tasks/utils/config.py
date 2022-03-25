from poetry.core.pyproject.toml import PyProjectTOML

FLAKE8 = """[flake8]
exclude =
    venv,
    dist,
    .venv
select = ANN,B,B9,BLK,C,D,DAR,E,F,I,S,W
ignore = E203,E501,W503,D100,D104
per-file-ignores =
    tests/*: D103,S101
max-line-length = 120
max-complexity = 10
import-order-style = google
docstring-convention = google
"""


def write_lint_config() -> None:
    """Save default flake8 linting config."""
    with open(".flake8", "w", encoding="utf-8") as f:
        f.write(FLAKE8)


def add_format_config(pyproject: PyProjectTOML) -> None:
    """Augment pyproject.toml in memory with default formatting config."""
    ...


def add_typecheck_config(pyproject: PyProjectTOML) -> None:
    """Augment pyproject.toml in memory with default typechecking config."""
    ...


def add_test_config(pyproject: PyProjectTOML) -> None:
    """Augment pyproject.toml in memory with default test config."""
    #  pyproject.data["tool"]["pytest"]["ini_options"]["minversion"] = "6.0"
    #  pyproject.data["tool"]["pytest"]["ini_options"]["addopts"] = "-s -vvv --color=yes --cov=. --no-cov-on-fail"
    #
    #  pyproject.data["tool"]["coverage"]["run"]["branch"] = True
    #  pyproject.data["tool"]["coverage"]["run"]["omit"] = ["tests/*", "**/__init__.py", "tasks.py"]
    ...
