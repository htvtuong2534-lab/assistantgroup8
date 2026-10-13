# AI Service Interface

## Purpose

This document defines the interface for integrating a future Large Language Model (LLM) into the Smart Virtual Assistant project.

At this stage, the project only defines the interface. No actual LLM API is called.

---

## Function Signature

```python
generate_answer(
    question: str,
    context: str | None = None
) -> str
```

---

## Inputs

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| question | string | Yes | User's question. |
| context | string | No | Additional retrieved information that may help answer the question. |

---

## Output

Returns a string containing the generated answer.

Example:

```text
"The Admissions Office is open Monday to Friday from 8:00 to 17:00."
```

---

## Error Handling

The implementation should gracefully handle the following situations:

- Empty question
- Invalid input
- AI provider unavailable
- Timeout while waiting for a response
- Unexpected internal errors

The caller should receive a clear and readable error message instead of the application crashing.

---

## Fallback Behavior

If no AI provider has been configured:

- Do not call any external service.
- Return an informative message.

Example:

```text
AI service is not configured.
```

---

## Future Providers

The interface should allow different providers to be connected later, such as:

- OpenAI
- Google Gemini
- Ollama
- Other compatible LLM providers

No provider-specific implementation is included in this milestone.

---

## Acceptance

This document only specifies the interface.

**No LLM call is implemented yet.**