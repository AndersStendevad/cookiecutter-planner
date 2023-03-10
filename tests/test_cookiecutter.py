""" tests for cookiecutter """

from subprocess import run

def test_bake_project(bake):
    """check if cookiecutter will even bake"""
    pass

def test_pre_commit_in_baked_project(bake, helper):
    """check pre-commit in baked project"""
    helper.check_result(
        run("pre-commit run --all-files", shell=True, capture_output=True)
    )

def test_docs(bake, helper):
    """check if docs are generated"""
    helper.check_result(run("tox -e docs", shell=True, capture_output=True))

def test_lint(bake, helper):
    """check lint in baked project"""
    helper.check_result(run("tox -e lint", shell=True, capture_output=True))
