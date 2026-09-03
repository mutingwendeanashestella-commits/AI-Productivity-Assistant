"""
Email Generation Module
Generates professional emails using AI
"""

import os
from openai import OpenAI

class EmailGenerator:
    """Generate professional emails using AI"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"
    
    def generate(self, topic: str, tone: str = "professional", recipient: str = "Team", context: str = "") -> str:
        """
        Generate an email based on the provided parameters
        
        Args:
            topic: Subject of the email
            tone: Tone of the email (professional, friendly, formal, casual)
            recipient: Email recipient
            context: Additional context for the email
            
        Returns:
            Generated email text
        """
        prompt = f"""Generate a professional email with the following details:
        
Topic: {topic}
Tone: {tone}
Recipient: {recipient}
Context: {context}

Requirements:
- Include a proper greeting
- Write 2-3 paragraphs with clear message
- Include a professional closing
- Keep it concise and to the point
- Make it ready to send

Email:"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional email writer. Generate clear, concise, and appropriate emails."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    def generate_response(self, received_email: str, action: str = "respond") -> str:
        """
        Generate a response to a received email
        
        Args:
            received_email: The original email to respond to
            action: Action to take (respond, decline, accept, clarify)
            
        Returns:
            Generated response email
        """
        prompt = f"""Generate an email response to the following email:

Original Email:
{received_email}

Action: {action}

Generate an appropriate professional response that:
- Addresses the key points
- Is clear and concise
- Matches professional standards
- Includes proper greeting and closing

Response Email:"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional email writer. Generate appropriate email responses."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
