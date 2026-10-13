# UI Source Citations

## Goal

Design how the University Assistant displays citations below its answers so students can identify and verify the information sources.

## Design Rules

- Display citations directly below the assistant's answer.
- Show the document title or website name.
- Include a page number or relevant section when available.
- Make the source clickable when a valid URL is available.
- Do not display fabricated sources.
- If no sources are available, display: "No sources available."

## Example 1: Answer with a document source

**Question:** What are the requirements for registering for a graduation thesis?

**Assistant answer (mockup):**

Students should check the graduation thesis requirements in the applicable training regulations for their program.

**Sources:**

1. Training Regulations
   - Section: Graduation Thesis
   - Page: 12
   - Link: `[Open source](https://example.com/training-regulations)`

**UI layout:**

```text
Assistant answer
Students should check the graduation thesis requirements
in the applicable training regulations for their program.

Sources
[1] Training Regulations · Page 12 · Open source
```

Note: The document title, section, and page are illustrative placeholders.

## Example 2: Answer with multiple web sources

**Question:** Where can students find information about the Training Office?

**Assistant answer (mockup):**

Students can consult the university's official website for information about the Training Office and its services.

**Sources:**

1. University Official Website
   - Link: `[Open source](https://example.com/university)`
2. Training Office Information
   - Link: `[Open source](https://example.com/training-office)`

**UI layout:**

```text
Assistant answer
Students can consult the university's official website for
information about the Training Office and its services.

Sources
[1] University Official Website · Open source
[2] Training Office Information · Open source
```

Note: The URLs are placeholders and must be replaced with verified URLs before real use.

## Future Implementation

The UI will render citations from the backend response. The citation data format should be agreed upon with the backend developer before implementation.

Suggested citation fields:

- `title`: document or website title
- `url`: source URL
- `section`: relevant section, if available
- `page`: page number, if available