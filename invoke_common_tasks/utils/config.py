# Third Party
from poetry.core._vendor.tomlkit import table
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
    tools = pyproject.data["tool"]
    if "black" not in tools:
        black_table = table()
        black_table["line-length"] = 120
        tools["black"] = black_table

    if "isort" not in tools:
        isort_table = table()
        isort_table["profile"] = "black"
        isort_table["multi_line_output"] = 3
        isort_table["import_heading_stdlib"] = "Standard Library"
        isort_table["import_heading_firstparty"] = "Our Libraries"
        isort_table["import_heading_thirdparty"] = "Third Party"
        tools["isort"] = isort_table


def add_typecheck_config(pyproject: PyProjectTOML) -> None:
    """Augment pyproject.toml in memory with default typechecking config."""
    tools = pyproject.data["tool"]

    if "mypy" not in tools:
        mypy_table = table()
        mypy_table["exclude"] = ["tests/", "tasks\.py"]  # noqa
        mypy_table["pretty"] = True
        mypy_table["show_error_codes"] = True
        mypy_table["show_column_numbers"] = True
        mypy_table["show_error_context"] = True
        mypy_table["ignore_missing_imports"] = True
        mypy_table["follow_imports"] = "silent"
        mypy_table["disallow_incomplete_defs"] = True
        mypy_table["disallow_untyped_defs"] = False
        mypy_table["strict"] = False
        tools["mypy"] = mypy_table


def add_test_config(pyproject: PyProjectTOML) -> None:
    """Augment pyproject.toml in memory with default test config."""
    tools = pyproject.data["tool"]
    if "pytest" not in tools:
        ini_options = table()
        ini_options["minversion"] = "6.0"
        ini_options["addopts"] = "-s -vvv --color=yes --cov=. --no-cov-on-fail"

        pytest_table = table()
        # TODO: For some reason nested tables are adding the intermediate table heading
        pytest_table["ini_options"] = ini_options
        tools["pytest"] = pytest_table

    if "coverage" not in tools:
        run_table = table()
        run_table["branch"] = True
        run_table["omit"] = ["tests/*", "**/__init__.py", "tasks.py"]

        coverage_table = table()
        coverage_table["run"] = run_table
        tools["coverage"] = coverage_table
