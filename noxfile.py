"""Nox sessions for isoFlux.

Run tests and build docs in isolated virtual environments.
Usage examples:
    nox            # run default sessions (tests on all python versions)
    nox -s docs    # build documentation
"""

import nox

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12"]

@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite with coverage."""
    # Install package plus test extras declared in pyproject.toml
    session.install("-e", ".[test]")
    # Run pytest with coverage
    session.run(
        "pytest",
        "--pyargs",
        "isoflux",
        "--cov",
        "isoflux",
        "--cov-report",
        "term-missing",
        *session.posargs,
    )

@nox.session(python="3.11")
def docs(session):
    """Build the HTML documentation."""
    session.install("-e", ".[docs]")
    session.run(
        "sphinx-build",
        "-b",
        "html",
        "-j",
        "auto",
        "docs",
        "docs/_build/html",
        *session.posargs,
    ) 