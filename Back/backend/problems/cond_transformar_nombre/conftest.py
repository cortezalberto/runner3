"""
Shared pytest fixtures for conditional problems.
Provides reusable utilities for testing stdin/stdout interactions and function calls.

This file should be copied to each problem directory as conftest.py
"""
import pytest
import sys
from io import StringIO
from typing import Callable, Any


@pytest.fixture
def capture_main_output():
    """
    Fixture that captures stdout from main() function calls with mocked stdin.

    Returns a function that takes input_data and student module,
    executes student.main(), and returns captured output.

    Usage:
        output = capture_main_output("5", student_module)
    """
    def _capture(input_data: str, student_module) -> str:
        """Execute main() with mocked stdin and return captured stdout."""
        old_stdin = sys.stdin
        old_stdout = sys.stdout

        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()

            student_module.main()

            output = sys.stdout.getvalue().strip()
            return output
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

    return _capture


@pytest.fixture
def student_module():
    """
    Fixture that loads the student's code module dynamically.
    This allows tests to import and test student code.

    Returns the student module with all defined functions and classes.
    """
    import importlib.util
    import os

    spec = importlib.util.spec_from_file_location(
        'student_code',
        os.path.join(os.getcwd(), 'student_code.py')
    )
    student = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student)

    return student


@pytest.fixture
def call_function():
    """
    Fixture that safely calls a student function and returns the result.

    Usage:
        result = call_function(student_module, 'my_function', arg1, arg2)
    """
    def _call(student_module, function_name: str, *args, **kwargs) -> Any:
        """Call a function from student module with given arguments."""
        if not hasattr(student_module, function_name):
            pytest.fail(f"La función '{function_name}' no está definida en el código del estudiante")

        func = getattr(student_module, function_name)
        return func(*args, **kwargs)

    return _call
