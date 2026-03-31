
from datetime import datetime

# ----------------------------------------------------
# GLOBAL DEFAULT MARKETING GUIDELINES (Option A)
# ----------------------------------------------------

GLOBAL_GUIDELINES = [
    "Maintain a professional but friendly tone.",
    "Always write clearly and concisely.",
    "Avoid jargon unless the audience is technical.",
    "Never make unrealistic or exaggerated claims.",
    "Use brand-safe and inclusive language.",
    "Avoid mentioning competitors directly.",
    "Prefer value propositions over features.",
    "Use UK spelling conventions.",
    "Do not reference sensitive demographics or protected attributes.",
]


# ----------------------------------------------------
# STRATEGIST AGENT
# ----------------------------------------------------

class StrategistAgent:
    def __init__(self):
        self.agent_guidelines = [
            "Base all recommendations on audience insights.",
            "Ensure each campaign has measurable KPIs.",
            "Channel strategies must be justified with reasoning.",
            "Positioning must be clear and high-level.",
        ]

    def run(self, objective):
        if "AI" in objective:
            audience = ["Tech Professionals", "Marketing Teams", "Startup Founders"]
        else:
            audience = ["General Online Consumers"]

        strategy = {
            "objective": objective,
            "audience": audience,
            "pillars": [
                "Education",
                "Pain Point Solving",
                "Social Proof",
                "Feature Highlights"
            ],
            "channels": ["LinkedIn", "Email", "Google Ads"],
            "guidelines_respected": self.agent_guidelines,
        }

        return strategy


# ----------------------------------------------------
# COPYWRITER AGENT
# ----------------------------------------------------

class CopywriterAgent:
    def __init__(self):
        self.agent_guidelines = [
            "Tone must be persuasive but not pushy.",
            "Copy must remain concise and skimmable.",
            "Never exaggerate results or create unrealistic expectations.",
            "CTA must be singular and clear.",
            "Avoid technical jargon unless required.",
        ]

    def run(self, strategy):
        audience = ", ".join(strategy["audience"])

        copy = {
            "headline": f"{strategy['objective']} — Designed for {audience}",
            "ad_copy": (
                f"Our solution helps {audience} work smarter and more efficiently. "
                "Built with a value-driven focus, it addresses key challenges clearly "
                "and responsibly while aligning with industry best practices."
            ),
            "cta": "Learn More",
            "guidelines_respected": self.agent_guidelines,
        }

        return copy


# ----------------------------------------------------
# ANALYST AGENT
# ----------------------------------------------------

class AnalystAgent:
    def __init__(self):
        self.agent_guidelines = [
            "Insights must be actionable, not generic.",
            "Avoid subjective language — stick to data-driven reasoning.",
            "No fabricated metrics — use projections only.",
            "Highlight the ‘why’ behind each insight.",
        ]

    def run(self, strategy):
        analysis = {
            "projection": "Expected 15–25% engagement lift based on similar industry campaigns.",
            "recommended_kpis": ["CTR", "CPC", "Lead Conversion Rate"],
            "guidelines_respected": self.agent_guidelines
        }
        return analysis


# ----------------------------------------------------
# SUPERVISOR AGENT
# ----------------------------------------------------

class Supervisor:
    def __init__(self):
        self.global_guidelines = GLOBAL_GUIDELINES
        self.strategist = StrategistAgent()
        self.copywriter = CopywriterAgent()
        self.analyst = AnalystAgent()

    def run_campaign(self, objective):
        strategy = self.strategist.run(objective)
        copy = self.copywriter.run(strategy)
        analysis = self.analyst.run(strategy)

        return {
            "timestamp": datetime.now().isoformat(),
            "objective": objective,
            "strategy": strategy,
            "copy": copy,
            "analysis": analysis,
            "global_guidelines": self.global_guidelines,
        }
