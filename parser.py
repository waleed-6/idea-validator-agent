from config import call_llm

def parse_idea(idea):
    prompt = f"""
You will be given a startup idea. Extract the following:
- Problem it solves
- Target audience
- Proposed solution
- Related keywords (3–5)

Startup Idea:
\"\"\"{idea}\"\"\"

Respond in this JSON format:
{{
  "problem": "...",
  "audience": "...",
  "solution": "...",
  "keywords": ["...", "..."]
}}
"""
    response = call_llm(prompt)
    return eval(response)  # You can also use json.loads() if formatting is strict
