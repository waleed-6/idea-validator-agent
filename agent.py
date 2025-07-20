from parser import parse_idea
from search import find_competitors
from analyzer import generate_report

class StartupValidatorAgent:
    def run(self, idea):
        parsed = parse_idea(idea)
        competitors = find_competitors(parsed)
        report = generate_report(parsed, competitors)
        return report
