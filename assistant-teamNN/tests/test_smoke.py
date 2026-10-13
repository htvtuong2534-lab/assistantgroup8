"""Lab 01 smoke tests, based on CSC10014-at-fit-hcmus/lab01-starter.

Run from assistant-teamNN with: python -m pytest -q
The starter backend and data/offices.csv must be present.
"""

import pytest

from assistant.rules import load_offices, reply


def test_greeting():
    assert "Hello" in reply("hi")


@pytest.mark.parametrize(
    ("office", "room", "hours"),
    [
        ("Training Office", "I.101", "Mon-Fri 07:30-16:30"),
        ("Student Affairs", "I.102", "Mon-Fri 08:00-16:00"),
        ("Library", "B.201", "Mon-Sat 07:00-20:00"),
        ("IT Helpdesk", "E.005", "Mon-Fri 08:00-17:00"),
    ],
)
def test_office_lookup(office, room, hours):
    assert reply(f"Where is the {office}?") == (
        f"{office}: room {room}, open {hours}."
    )


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_office_lookup_ignores_case_and_surrounding_whitespace():
    assert reply("  WHERE IS THE TRAINING OFFICE?!  ") == reply(
        "Where is the Training Office?"
    )


def test_load_offices_reads_utf8_csv(tmp_path):
    csv_path = tmp_path / "offices.csv"
    csv_path.write_text(
        "name,room,hours\nPhòng Đào Tạo,I.101,Mon-Fri 07:30-16:30\n",
        encoding="utf-8",
    )
    offices = load_offices(csv_path)

    assert reply("Phòng Đào Tạo ở đâu?", offices=offices) == (
        "Phòng Đào Tạo: room I.101, open Mon-Fri 07:30-16:30."
    )
