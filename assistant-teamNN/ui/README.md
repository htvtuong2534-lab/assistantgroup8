# User Interface

This directory contains the user interface of the Smart Virtual Assistant project.

## Purpose

The UI is responsible for:

- Receiving questions from users.
- Displaying the assistant's responses.
- Providing a simple and clear interaction between the user and the assistant core.

## Planned Structure

The UI can be implemented as a simple web interface or another interface agreed upon by the team.

Example:

```text
ui/
├── README.md
└── ...
```

## Interaction Flow

The expected interaction is:

```text
User
  ↓
UI
  ↓
Assistant Core
  ↓
Response
  ↓
UI
  ↓
User
```

The UI should not contain the main assistant logic. It should send the user's input to the assistant core and display the returned response.

## Future Development

The UI may later include:

- A text input field for user questions.
- A button to send questions.
- A conversation area for displaying messages.
- Error messages when the assistant cannot process a request.
- Basic styling for better usability.

## Integration

The UI will be connected to the modules inside:

```text
src/assistant/
```

The exact integration method will be decided by the team during development.