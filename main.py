"""
AI Productivity Assistant - Main Application
Entry point for the AI Productivity Assistant
"""

import os
import sys
from dotenv import load_dotenv
from src.email_generator import EmailGenerator
from src.meeting_summarizer import MeetingSummarizer
from src.task_planner import TaskPlanner
from src.research_assistant import ResearchAssistant
from src.chatbot import ProductivityChatbot

load_dotenv()

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("AI-POWERED WORKPLACE PRODUCTIVITY ASSISTANT")
    print("="*60)
    print("\nSelect an option:")
    print("1. Email Generation")
    print("2. Meeting Summarization")
    print("3. Task Planning")
    print("4. Research Assistance")
    print("5. Productivity Chatbot")
    print("6. Exit")
    print("-"*60)
    return input("Enter your choice (1-6): ").strip()

def main():
    """Main application loop"""
    print("\nWelcome to AI Productivity Assistant!")
    print("Powered by advanced AI and prompt engineering\n")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            print("\nEMAIL GENERATION")
            generator = EmailGenerator()
            topic = input("Email topic: ").strip()
            tone = input("Tone (professional/friendly): ").strip() or "professional"
            email = generator.generate(topic, tone)
            print("\nGenerated Email:\n" + email)
        
        elif choice == "2":
            print("\nMEETING SUMMARIZATION")
            summarizer = MeetingSummarizer()
            print("Paste meeting transcript (end with blank line):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            transcript = "\n".join(lines)
            result = summarizer.summarize(transcript, "detailed")
            print("\nMeeting Summary:\n" + result["full_summary"])
        
        elif choice == "3":
            print("\nTASK PLANNING")
            planner = TaskPlanner()
            project = input("Project name: ").strip()
            deadline = input("Deadline (YYYY-MM-DD): ").strip()
            scope = input("Project scope: ").strip()
            result = planner.create_plan(project, deadline, scope)
            print("\nProject Plan:\n" + result["plan"])
        
        elif choice == "4":
            print("\nRESEARCH ASSISTANCE")
            assistant = ResearchAssistant()
            topic = input("Research topic: ").strip()
            result = assistant.research(topic, "comprehensive")
            print("\nResearch Results:\n" + result["research_findings"])
        
        elif choice == "5":
            print("\nPRODUCTIVITY CHATBOT")
            print("Chat with your AI Assistant (type 'exit' to quit)")
            chatbot = ProductivityChatbot()
            while True:
                user_input = input("\nYou: ").strip()
                if user_input.lower() == "exit":
                    break
                if user_input:
                    response = chatbot.chat(user_input)
                    print(f"Assistant: {response}")
        
        elif choice == "6":
            print("\nThank you for using AI Productivity Assistant!\n")
            sys.exit(0)
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
