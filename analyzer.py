from config import call_llm

def generate_report(parsed, competitors):
    comp_info = "\n".join([f"- {c['title']} ({c['link']}): {c['snippet']}" for c in competitors])

    prompt = f"""
You are a startup analyst. A user submitted the following startup idea:

Problem: {parsed['problem']}
Audience: {parsed['audience']}
Solution: {parsed['solution']}

You found the following competitors:
{comp_info}

Now write a report that:
1. Summarizes the idea clearly
2. Lists similar products or competitors
3. Suggests unique angles or differentiators
4. Notes any market risks or opportunities

Write it in clear bullet points or short paragraphs.
"""

    return call_llm(prompt)
