""" Conftest for planning tests."""

import pytest
import json
import os

from pathlib import Path
from subprocess import run, CompletedProcess

class Helper:
    @staticmethod
    def check_result(result: CompletedProcess):
        """Check result of subprocess.run().

        Parameters:
        ===========
        result: CompletedProcess:
            Result of subprocess.run().

        Returns:
        ========
        None
        """
        stderr = result.stderr.decode("utf-8")
        stdout = result.stdout.decode("utf-8")
        if result.stderr and "SetuptoolsDeprecationWarning" not in stderr:
            raise Exception(stderr)
        if "ERROR:" in stdout:
            raise Exception(stdout)
        if "FAILED" in stdout:
            raise Exception(stdout)
        if "WARNING" in stdout:
            raise Exception(stdout)

@pytest.fixture(scope="session")
def helper():
    """Helper for tests."""
    return Helper
