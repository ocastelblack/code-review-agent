from radon.complexity import cc_visit
import subprocess

class AnalysisService:

    def analyze_complexity(self, code: str):
        results = cc_visit(code)
        return [
            {
                "name": r.name,
                "complexity": r.complexity,
                "lineno": r.lineno
            }
            for r in results if r.complexity > 10
        ]

    def analyze_security(self, file_path: str):
        result = subprocess.run(
            ["bandit", "-r", file_path, "-f", "json"],
            capture_output=True,
            text=True
        )
        return result.stdout
