"""Smoke tests for the starter's python -m assistant entry point."""

import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_assistant(*args, input_text=None):
    env = os.environ.copy()
    paths = [str(PROJECT_ROOT / "src")]
    if env.get("PYTHONPATH"):
        paths.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(paths)
    env["PYTHONIOENCODING"] = "utf-8"

    return subprocess.run(
        [sys.executable, "-m", "assistant", *args],
        cwd=PROJECT_ROOT,
        env=env,
        input=input_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=10,
        check=False,
    )


def test_cli_office_lookup():
    result = run_assistant("where", "is", "the", "IT", "helpdesk?")

    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == (
        "IT Helpdesk: room E.005, open Mon-Fri 08:00-17:00."
    )


def test_interactive_greeting_and_quit():
    result = run_assistant(input_text="hi\nquit\n")

    assert result.returncode == 0, result.stderr
    assert "Type 'quit' to exit." in result.stdout
    assert "Hello! Ask me where an office is, or when it opens." in result.stdout
