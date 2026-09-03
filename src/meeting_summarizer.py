"""
Meeting Summarization Module
Extracts key points and action items from meeting transcripts
"""

import os
from openai import OpenAI

class MeetingSummarizer:
    """Summarize meetings and extract key information"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"
    
    def summarize(self, transcript: str, format: str = "detailed") -> dict:
        """
        Summarize a meeting transcript
        
        Args:
            transcript: Meeting transcript text
            format: Summary format (brief, detailed, executive)
            
        Returns:
            Dictionary with summary, action items, and key points
        """
        prompt = f"""Analyze the following meeting transcript and provide a structured summary.

Meeting Transcript:
{transcript}

Please provide:
1. SUMMARY: A {format} summary of the meeting
2. KEY POINTS: List the 3-5 most important points discussed
3. ACTION ITEMS: List specific action items with owners
4. DECISIONS: Any decisions made during the meeting
5. NEXT STEPS: What needs to happen next
6. PARTICIPANTS: Key participants and their roles (if mentioned)

Format the response as clear sections with headers."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert meeting analyst. Extract key information from meeting transcripts clearly and concisely."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        
        summary_text = response.choices[0].message.content
        
        return {
            "full_summary": summary_text,
            "format_used": format,
            "transcript_length": len(transcript.split()),
        }
    
    def extract_action_items(self, transcript: str) -> list:
        """
        Extract only action items from meeting transcript
        
        Args:
            transcript: Meeting transcript text
            
        Returns:
            List of action items with owners
        """
        prompt = f"""From the following meeting transcript, extract ONLY the action items.
For each action item, identify:
1. The task description
2. The owner/responsible person
3. The deadline (if mentioned)

Meeting Transcript:
{transcript}

Format as a numbered list with clear task, owner, and deadline information."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert at identifying action items from meetings."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )
        
        return response.choices[0].message.content
