"""
Research Assistance Module
Gathers and synthesizes information on topics
"""

import os
from openai import OpenAI

class ResearchAssistant:
    """Provide research assistance and information synthesis"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"
    
    def research(self, topic: str, depth: str = "comprehensive", focus_areas: str = "") -> dict:
        """
        Conduct research on a topic
        
        Args:
            topic: Research topic
            depth: Depth of research (overview, detailed, comprehensive)
            focus_areas: Specific areas to focus on
            
        Returns:
            Dictionary with research findings
        """
        prompt = f"""Conduct a {depth} research on the following topic:

Topic: {topic}
Focus Areas: {focus_areas}

Please provide:
1. OVERVIEW: High-level summary of the topic
2. KEY CONCEPTS: Main concepts and definitions
3. CURRENT STATE: Current status and recent developments
4. TRENDS: Notable trends and patterns
5. CHALLENGES: Current challenges and limitations
6. OPPORTUNITIES: Emerging opportunities
7. RECOMMENDATIONS: Recommended actions or next steps
8. RESOURCES: Key resources for further learning

Be factual, balanced, and cite credible sources where possible."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert researcher with access to broad knowledge. Provide well-researched, balanced, and comprehensive information."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        return {
            "topic": topic,
            "depth": depth,
            "research_findings": response.choices[0].message.content,
            "focus_areas": focus_areas
        }
