import pytest
from config import TOKEN


"""Replaces any occurrence  of the sensitive TOKEN in the long representation of the report with [HIDDEN]."""
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.outcome == "failed" and hasattr(report, "longrepr"):
        report.longrepr = str(report.longrepr).replace(TOKEN, "[HIDDEN]")
