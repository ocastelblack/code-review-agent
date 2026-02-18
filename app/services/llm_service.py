# TODO: improve prompt engineering

class LLMService:
    def review(self, diffs: dict):
        findings = []

        for file, diff in diffs.items():
            findings.append(f"LLM review simulated for {file}")

        return findings
