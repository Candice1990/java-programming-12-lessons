# Java Programming — Twelve Lessons

Open `index.html` in a modern browser. All lesson text, styling, diagrams and navigation are included in that file and work offline. Keep the demos folder beside it for the Download links.

- Twelve lessons with concept explanations, relationship diagrams and complete Java demonstrations.
- Search across all lessons; use Large text for classroom viewing.
- Print the current lesson or print all lessons from the course overview.
- Each demo folder includes source files, supporting input when needed, and run instructions.
- Examples target JDK 21. Expected output is shown beside each demonstration.

## Rebuild and verify

Use Python 3.12 or later and JDK 21 or later. No Python packages are required.

```sh
python3 tools/build.py
python3 tools/verify.py
```

The build regenerates index.html, demo files and course data from tools/.
The verifier compiles every demonstration with Java 21 compatibility and checks its output.
All build inputs are included in this repository.
