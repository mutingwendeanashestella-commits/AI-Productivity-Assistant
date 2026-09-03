"""
Productivity Chatbot Module
Provides real-time assistance through conversation
"""

import os
from openai import OpenAI

class ProductivityChatbot:
    """Interactive chatbot for workplace productivity assistance"""
    
    def __init__(self, system_prompt: str = ""):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"
        self.conversation_history = []
        
        if not system_prompt:
            system_prompt = """You are an AI Productivity Assistant designed to help professionals manage their work effectively. 
You can help with task planning, time management, meeting preparation, email writing, research, and project management.
Be helpful, professional, and concise. Provide actionable advice when possible."""
        
        self.system_prompt = system_prompt
    
    def chat(self, user_message: str) -> str:
        """
        Process user message and return response
        
        Args:
            user_message: User's message
            
        Returns:
            Chatbot response
        """
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.chat.completions.create(
            model=self.model,
            system=self.system_prompt,
            messages=self.conversation_history,
            temperature=0.7,
            max_tokens=500
        )
        
        assistant_message = response.choices[0].message.content
        
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
