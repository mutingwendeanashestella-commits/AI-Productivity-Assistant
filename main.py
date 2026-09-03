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

# Load environment variables
load_dotenv()

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("🤖 AI-POWERED WORKPLACE PRODUCTIVITY ASSISTANT")
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

def email_menu():
    """Email generation interface"""
    print("\n📧 EMAIL GENERATION")
    print("-"*40)
    generator = EmailGenerator()
    
    print("\nOptions:")
    print("1. Generate new email")
    print("2. Generate email response")
    print("3. Back to main menu")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        topic = input("Email topic: ").strip()
        tone = input("Tone (professional/friendly/formal/casual): ").strip() or "professional"
        recipient = input("Recipient: ").strip() or "Team"
        context = input("Additional context (optional): ").strip()
        
        email = generator.generate(topic, tone, recipient, context)
        print("\n✅ Generated Email:")
        print("-"*40)
        print(email)
    
    elif choice == "2":
        print("Paste the email you received (end with blank line):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        
        received_email = "\n".join(lines)
        action = input("Action (respond/decline/accept/clarify): ").strip() or "respond"
        
        response = generator.generate_response(received_email, action)
        print("\n✅ Generated Response:")
        print("-"*40)
        print(response)

def meeting_menu():
    """Meeting summarization interface"""
    print("\n📊 MEETING SUMMARIZATION")
    print("-"*40)
    summarizer = MeetingSummarizer()
    
    print("\nOptions:")
    print("1. Summarize meeting transcript")
    print("2. Extract action items only")
    print("3. Generate executive summary")
    print("4. Back to main menu")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice in ["1", "2", "3"]:
        print("Paste the meeting transcript (end with blank line):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        
        transcript = "\n".join(lines)
        
        if choice == "1":
            format_type = input("Format (brief/detailed/executive): ").strip() or "detailed"
            result = summarizer.summarize(transcript, format_type)
            print("\n✅ Meeting Summary:")
            print("-"*40)
            print(result["full_summary"])
        
        elif choice == "2":
            result = summarizer.extract_action_items(transcript)
            print("\n✅ Action Items:")
            print("-"*40)
            print(result)
        
        elif choice == "3":
            result = summarizer.generate_executive_summary(transcript)
            print("\n✅ Executive Summary:")
            print("-"*40)
            print(result)

def task_menu():
    """Task planning interface"""
    print("\n✓ TASK PLANNING")
    print("-"*40)
    planner = TaskPlanner()
    
    print("\nOptions:")
    print("1. Create project plan")
    print("2. Prioritize tasks")
    print("3. Estimate task effort")
    print("4. Back to main menu")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        project = input("Project name: ").strip()
        deadline = input("Deadline (YYYY-MM-DD, optional): ").strip()
        scope = input("Project scope: ").strip()
        team_size = input("Team size (default 1): ").strip() or "1"
        
        result = planner.create_plan(project, deadline, scope, int(team_size))
        print("\n✅ Project Plan:")
        print("-"*40)
        print(result["plan"])
    
    elif choice == "2":
        print("Enter tasks (one per line, blank line to finish):")
        tasks = []
        while True:
            task = input().strip()
            if not task:
                break
            tasks.append(task)
        
        result = planner.prioritize_tasks(tasks)
        print("\n✅ Prioritized Tasks:")
        print("-"*40)
        print(result)
    
    elif choice == "3":
        task = input("Describe the task to estimate: ").strip()
        result = planner.estimate_effort(task)
        print("\n✅ Effort Estimate:")
        print("-"*40)
        print(result["estimate"])

def research_menu():
    """Research assistance interface"""
    print("\n🔍 RESEARCH ASSISTANCE")
    print("-"*40)
    assistant = ResearchAssistant()
    
    print("\nOptions:")
    print("1. Research a topic")
    print("2. Competitive analysis")
    print("3. Generate insights from data")
    print("4. Back to main menu")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        topic = input("Research topic: ").strip()
        depth = input("Depth (overview/detailed/comprehensive): ").strip() or "comprehensive"
        focus = input("Focus areas (optional): ").strip()
        
        result = assistant.research(topic, depth, focus)
        print("\n✅ Research Findings:")
        print("-"*40)
        print(result["research_findings"])
    
    elif choice == "2":
        company = input("Company/Product: ").strip()
        market = input("Target market (optional): ").strip()
        
        result = assistant.competitive_analysis(company, market)
        print("\n✅ Competitive Analysis:")
        print("-"*40)
        print(result)
    
    elif choice == "3":
        print("Paste or describe the data (end with blank line):")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        
        data = "\n".join(lines)
        result = assistant.generate_insights(data)
        print("\n✅ Generated Insights:")
        print("-"*40)
        print(result)

def chatbot_menu():
    """Chatbot interface"""
    print("\n💬 PRODUCTIVITY CHATBOT")
    print("-"*40)
    chatbot = ProductivityChatbot()
    
    print("Chat with your AI Productivity Assistant!")
    print("(Type 'exit' to return to main menu)")
    print("-"*40)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "exit":
            break
        
        if not user_input:
            continue
        
        response = chatbot.chat(user_input)
        print(f"\n🤖 Assistant: {response}")

def main():
    """Main application loop"""
    print("\n✨ Welcome to AI Productivity Assistant!")
    print("Powered by advanced AI and prompt engineering\n")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            email_menu()
        elif choice == "2":
            meeting_menu()
        elif choice == "3":
            task_menu()
        elif choice == "4":
            research_menu()
        elif choice == "5":
            chatbot_menu()
        elif choice == "6":
            print("\n👋 Thank you for using AI Productivity Assistant!")
            print("Goodbye!\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
