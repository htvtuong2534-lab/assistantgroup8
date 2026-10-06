import sys

from assistant.rules import reply


def main():
    if len(sys.argv) > 1:
        print(reply(" ".join(sys.argv[1:])))
        return

    print("Hello! Ask me where an office is, or when it opens.")
    print("Type 'quit' to exit.")

    while True:
        try:
            question = input("> ")
        except EOFError:
            break

        if question.strip().lower() == "quit":
            break

        print(reply(question))


if __name__ == "__main__":
    main()