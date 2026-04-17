from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Candidate:
    name: str
    role: str
    skills: List[str]
    score: float
    feedback: List[str]
    recommendations: List[str] = field(default_factory=list)


class ResumeBuilder:

    @staticmethod
    def classify_feedback(feedback: List[str]) -> Tuple[List[str], List[str]]:
        """Classify feedback into strengths and improvements"""
        strengths = []
        improvements = []

        for f in feedback:
            f_clean = f.lower()
            if any(word in f_clean for word in ["good", "strong", "excellent"]):
                strengths.append(f)
            else:
                improvements.append(f)

        return strengths, improvements

    @staticmethod
    def format_section(title: str, items: List[str]) -> str:
        """Reusable section formatter"""
        lines = [f"\n{title}", "-" * len(title)]

        if not items:
            lines.append("No data available")
        else:
            lines.extend(f"- {item}" for item in items)

        return "\n".join(lines)

    @staticmethod
    def generate(candidate: Candidate) -> str:
        """Generate resume string"""
        strengths, improvements = ResumeBuilder.classify_feedback(candidate.feedback)

        resume_lines = [
            "=" * 35,
            "            RESUME",
            "=" * 35,

            f"\nName        : {candidate.name}",
            f"Target Role : {candidate.role}",

            ResumeBuilder.format_section("SKILLS", [", ".join(candidate.skills)]),

            "\nINTERVIEW PERFORMANCE",
            "-" * 25,
            f"Score       : {candidate.score}/10",

            ResumeBuilder.format_section("Strengths", strengths),
            ResumeBuilder.format_section("Areas to Improve", improvements),
            ResumeBuilder.format_section("RECOMMENDATIONS", candidate.recommendations),

            "\n" + "=" * 35
        ]

        return "\n".join(resume_lines)

    @staticmethod
    def save(resume: str, filename: str = "resume.txt") -> None:
        """Save resume to file"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resume)


def build_resume(candidate: Candidate, filename: str = "resume.txt") -> str:
    """Main function to generate and save resume"""
    try:
        resume = ResumeBuilder.generate(candidate)
        ResumeBuilder.save(resume, filename)
        return f"✅ Resume saved → {filename}"
    except Exception as e:
        return f"❌ Error: {str(e)}"