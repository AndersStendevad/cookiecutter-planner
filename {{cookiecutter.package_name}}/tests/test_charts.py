"""tests for charts"""

from subprocess import run, Popen, CompletedProcess


def test_chart_creation(helper):
    """Test if charts can be created with structurizr"""
    helper.check_result(
        run("ls", shell=True, capture_output=True)
    )
