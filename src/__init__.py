"""AI Productivity Assistant Package"""

from src.email_generator import EmailGenerator
from src.meeting_summarizer import MeetingSummarizer
from src.task_planner import TaskPlanner
from src.research_assistant import ResearchAssistant
from src.chatbot import ProductivityChatbot

__all__ = [
    'EmailGenerator',
    'MeetingSummarizer',
    'TaskPlanner',
    'ResearchAssistant',
    'ProductivityChatbot'
]
