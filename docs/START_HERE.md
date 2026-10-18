# Start Here

This course intentionally removes low-priority material from a generic Python beginner syllabus and focuses on the concepts that transfer directly into backend and AI engineering.

## Fast-track rule

For every session:

- **Green:** challenge solved without help → move on.
- **Orange:** solved with one or two hints → review the weak point, then move on.
- **Red:** could not explain or reconstruct the solution → repeat the exercise the next day.

## Priority

The highest-priority session is **02 — Lists + Dictionaries**.

Why:

```python
users = [
    {"name": "Imad", "skills": ["Python", "AI"]},
    {"name": "Sara", "skills": ["UiPath", "RPA"]},
]
```

This pattern appears everywhere:

- JSON
- REST APIs
- FastAPI request/response bodies
- LLM structured outputs
- tool/function calling
- RAG metadata
- configuration
- database result transformation

## Recommended order

Do not jump around:

`01 → 02 → 03 → 04 → 05 → 06 → 07 → 08`

You may move faster through 01 if the diagnostic is easy.

## Deferred topics

Do not spend significant time yet on:

- calendar APIs
- XML parsing
- shell/file-system utilities beyond `pathlib`
- advanced inheritance
- decorators
- generators
- metaclasses
- NumPy

They can be learned when a real project requires them.
