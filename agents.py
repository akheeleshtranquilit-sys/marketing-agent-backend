
from datetime import datetime
import os
import requests

# ----------------------------------------------------
# GLOBAL MARKETING GUIDELINES
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
# REAL WEB SEARCH (SERPAPI)
# ----------------------------------------------------
def web_search(query):
    """
    Performs a real Google search via SERPAPI.
    Returns the top 5 organic results:
    - Title
    - Snippet
    - URL

    REQUIREMENT:
    Add SERPAPI_KEY to Railway → Variables
    """
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        # fallback if no key is found
        return [f"[NO API KEY] SERPAPI_KEY missing. Could not fetch real data for '{query}'."]

    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
    except Exception as e:
        return [f"Error fetching real data: {e}"]

    results = []

    if "organic_results" in data:
        for item in data["organic_results"][:5]:
            title = item.get("title", "No title")
            snippet = item.get("snippet", "No description available")
            link = item.get("link", "No link available")
            results.append(f"{title} – {snippet} ({link})")
    else:
        results.append("No organic results from SERPAPI.")

    return results


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
# ✅ COMPETITOR ANALYSIS AGENT (REAL DATA + ADVANCED LOGIC)
# ----------------------------------------------------
class CompetitorAnalysisAgent:
    def __init__(self):
        self.agent_guidelines = [
            "Competitor insights must remain factual.",
            "Avoid defamatory or unverifiable claims.",
            "Focus on opportunities, not attacks.",
            "Use ethical positioning practices."
        ]

    # ✅ Simple Overview (REAL competitor names)
    def simple_analysis(self, objective):
        search_query = f"{objective} industrial PC competitors"
        real_results = web_search(search_query)

        competitor_names = []

        # Extract real competitor names from SERPAPI results
        for result in real_results:
            text = result

            # Extract company name before dash or before parentheses
            if "–" in text:
                name = text.split("–")[0].strip()
            else:
                name = text.split("(")[0].strip()

            # Avoid empty / weird values
            if len(name) > 1:
                competitor_names.append(name)

        # ✅ If SERPAPI returns no usable companies, use known industry competitors
        if not competitor_names:
            competitor_names = [
                "OnLogic",
                "Advantech",
                "Kontron",
                "AAEON",
                "Lanner Electronics",
                "Axiomtek",
                "Arbor Industrial",
                "IEI Integration",
                "WinSystems",
                "SECO / Seattle Embedded",
            ]

        return {
            "competitors": competitor_names,
            "real_world_results": real_results,
            "strengths": [
                "Strong brand awareness",
                "Good UX/interface",
                "Large user base"
            ],
            "weaknesses": [
                "Higher pricing",
                "Slower innovation cycles",
                "Limited personalisation"
            ],
            "opportunities": [
                "Position as more efficient",
                "Compete on pricing/value",
                "Differentiate through automation"
            ],
        }

    # ✅ Advanced SWOT + Feature Comparison + Pricing
    def advanced_analysis(self):
        return {
            "swot": {
                "OnLogic": {
                    "strengths": ["Strong reputation", "High‑quality rugged PCs"],
                    "weaknesses": ["More expensive than competitors"],
                    "opportunities": ["AI Edge expansion"],
                    "threats": ["Advantech, Kontron increasing market share"]
                },
                "Advantech": {
                    "strengths": ["Largest IPC manufacturer globally"],
                    "weaknesses": ["Very large catalogue = complexity"],
                    "opportunities": ["Edge‑as‑a‑Service growth"],
                    "threats": ["Smaller agile vendors like OnLogic"]
                }
            },
            "feature_comparison": {
                "Your App": ["AI automation", "Fast setup", "Modern UI"],
                "OnLogic": ["Fanless PCs", "Industrial rugged systems", "Edge AI support"],
                "Advantech": ["Wide product range", "AI edge servers", "WISE‑DeviceOn management"]
            },
            "pricing_comparison": {
                "Your App": "$29/mo",
                "OnLogic": "$500–$2500 per unit (typical)",
                "Advantech": "$400–$2200 per unit (typical)"
            },
        }

    # ✅ Web Research (Raw SERPAPI results)
    def web_research_analysis(self, objective):
        results = web_search(objective)
        return {"web_research": results}

    # ✅ Final combined output
    def run(self, objective):
        return {
            "simple": self.simple_analysis(objective),
            "advanced": self.advanced_analysis(),
            "web_research": self.web_research_analysis(objective),
            "guidelines_respected": self.agent_guidelines,
        }

    # ✅ Advanced SWOT + Pricing + Feature Comparison
    def advanced_analysis(self):
        return {
            "swot": {
                "Competitor A": {
                    "strengths": ["Strong reputation", "Good onboarding"],
                    "weaknesses": ["Expensive", "No automation"],
                    "opportunities": ["Better AI features"],
                    "threats": ["Emerging startups"]
                },
                "Competitor B": {
                    "strengths": ["Affordable", "Large customer base"],
                    "weaknesses": ["Poor UI", "No analytics"],
                    "opportunities": ["Offer premium AI analytics"],
                    "threats": ["Market saturation"]
                }
            },
            "feature_comparison": {
                "Your App": ["AI automation", "Fast setup", "Modern UI"],
                "Competitor A": ["Manual features", "Good onboarding"],
                "Competitor B": ["Cheap", "Basic tools"]
            },
            "pricing_comparison": {
                "Your App": "$29/mo",
                "Competitor A": "$49/mo",
                "Competitor B": "$19/mo"
            },
        }

    # ✅ Web Research
    def web_research_analysis(self, objective):
        results = web_search(objective)
        return {"web_research": results}

    def run(self, objective):
        return {
            "simple": self.simple_analysis(objective),
            "advanced": self.advanced_analysis(),
            "web_research": self.web_research_analysis(objective),
            "guidelines_respected": self.agent_guidelines,
        }


# ----------------------------------------------------
# SUPERVISOR
# ----------------------------------------------------
class Supervisor:
    def __init__(self):
        self.global_guidelines = GLOBAL_GUIDELINES
        self.strategist = StrategistAgent()
        self.copywriter = CopywriterAgent()
        self.analyst = AnalystAgent()
        self.competitor = CompetitorAnalysisAgent()

    def run_campaign(self, objective):
        strategy = self.strategist.run(objective)
        copy = self.copywriter.run(strategy)
        analysis = self.analyst.run(strategy)
        competitor_analysis = self.competitor.run(objective)

        return {
            "timestamp": datetime.now().isoformat(),
            "objective": objective,
            "strategy": strategy,
            "copy": copy,
            "analysis": analysis,
            "competitor_analysis": competitor_analysis,
            "global_guidelines": self.global_guidelines,
        }
