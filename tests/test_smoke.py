"""Smoke tests for the pystatsfinance package skeleton."""

import re

import pystatsfinance


def test_version_is_semver():
    assert isinstance(pystatsfinance.__version__, str)
    assert re.match(r"^\d+\.\d+\.\d+", pystatsfinance.__version__)


def test_maintainer_metadata():
    assert pystatsfinance.__author__ == "Hai-Shuo"
    assert pystatsfinance.__email__ == "contact@sgcx.org"
