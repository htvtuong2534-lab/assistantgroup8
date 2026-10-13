# AI vs Non-AI Questions

The following examples distinguish questions that require an LLM from questions that can be answered using existing project data.

| Question | Need AI? | Reason |
|----------|----------|--------|
| Explain recursion in simple terms. | Yes | Requires natural language generation. |
| Summarize this article. | Yes | Requires understanding and summarizing long text. |
| Translate this paragraph into Vietnamese. | Yes | Requires language generation. |
| Rewrite this email professionally. | Yes | Requires text rewriting. |
| Suggest improvements for my resume. | Yes | Requires reasoning and writing. |
| Compare Python and Java. | Yes | Requires explanation and comparison. |
| Write a meeting invitation email. | Yes | Generates new content. |
| Give ideas for a final-year software project. | Yes | Requires creativity and reasoning. |
| Explain why this code may fail. | Yes | Requires analysis of code. |
| Recommend a study plan for learning AI. | Yes | Produces personalized recommendations. |
| What is the Admissions Office address? | No | Can be retrieved from stored data. |
| What are the office opening hours? | No | Simple lookup. |
| What is the office phone number? | No | Stored information. |
| Who manages the Admissions Office? | No | Retrieved from project data. |
| What email should students contact? | No | Stored information. |
| Where is Room A203 located? | No | Data lookup. |
| List all available offices. | No | Retrieve existing dataset. |
| Which office handles scholarship applications? | No | Lookup from structured data. |
| Is the library open on Sunday? | No | Retrieve stored schedule. |
| What services does Student Affairs provide? | No | Retrieve stored information. |

## Summary

Questions requiring reasoning, creativity, summarization, translation, or content generation should be handled by an AI model.

Questions whose answers already exist in the project's dataset should be answered by the retrieval system without using an LLM.