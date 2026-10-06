import csv


def load_offices(csv_path):
    offices = {}

    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"].strip()
            room = row["room"].strip()
            hours = row["hours"].strip()

            offices[name.lower()] = {
                "name": name,
                "room": room,
                "hours": hours,
            }

    return offices


def reply(question, offices=None):
    question = question.strip()

    if not question:
        return "Please type a question."

    if offices is None:
        offices = load_offices("data/offices.csv")

    normalized = question.lower().strip()

    if normalized == "hi" or normalized == "hello":
        return "Hello!"

    for office_key, office in offices.items():
        if office_key in normalized:
            return (
                f"{office['name']}: "
                f"room {office['room']}, open {office['hours']}."
            )

    return "I don't know."