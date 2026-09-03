# Usage Guide

## Email Generation

### Generate a New Email

```python
from src.email_generator import EmailGenerator

generator = EmailGenerator()
email = generator.generate(
    topic="Q3 Project Update",
    tone="professional",
    recipient="Project Stakeholders",
    context="Project is 85% complete, on schedule"
)
print(email)
```

**Parameters:**
- `topic` (str): Subject of the email
- `tone` (str): professional, friendly, formal, or casual
- `recipient` (str): Who the email is addressed to
- `context` (str): Additional context for better results

### Generate an Email Response

```python
response = generator.generate_response(
    received_email="Your original email text here",
    action="respond"  # or "accept", "decline", "clarify"
)
print(response)
```

---

## Meeting Summarization

### Summarize a Meeting

```python
from src.meeting_summarizer import MeetingSummarizer

summarizer = MeetingSummarizer()
result = summarizer.summarize(
    transcript="Meeting transcript text",
    format="detailed"  # or "brief", "executive"
)
print(result["full_summary"])
```

### Extract Action Items

```python
action_items = summarizer.extract_action_items(
    transcript="Meeting transcript text"
)
print(action_items)
```

**Output includes:**
- Key points discussed
- Action items with owners
- Decisions made
- Next steps
- Participant roles

---

## Task Planning

### Create a Project Plan

```python
from src.task_planner import TaskPlanner

planner = TaskPlanner()
plan = planner.create_plan(
    project="Mobile App Redesign",
    deadline="2026-12-31",
    scope="Complete UI/UX redesign with new features",
    team_size=5
)
print(plan["plan"])
```

**Output includes:**
- Project overview
- Phases and milestones
- Detailed task list with estimates
- Timeline
- Risk assessment
- Success criteria

---

## Research Assistance

### Research a Topic

```python
from src.research_assistant import ResearchAssistant

assistant = ResearchAssistant()
research = assistant.research(
    topic="AI in Workplace Automation",
    depth="comprehensive",  # or "overview", "detailed"
    focus_areas="Productivity gains, cost analysis, implementation"
)
print(research["research_findings"])
```

### Competitive Analysis

```python
analysis = assistant.competitive_analysis(
    company="Your Company",
    market="Technology/SaaS"
)
print(analysis)
```

### Generate Insights from Data

```python
insights = assistant.generate_insights(
    data_summary="Your data summary or raw data"
)
print(insights)
```

---

## Productivity Chatbot

### Interactive Chat

```python
from src.chatbot import ProductivityChatbot

chatbot = ProductivityChatbot()

# Single message
response = chatbot.chat("How should I organize my weekly tasks?")
print(response)

# Multi-turn conversation
response2 = chatbot.chat("What if I have urgent meetings?")
print(response2)
```

### Set Context

```python
# Set background information for better responses
chatbot.set_context("I'm a product manager with 5 direct reports")
response = chatbot.chat("How should I manage my calendar?")
```

### Reset Conversation

```python
chatbot.reset_conversation()  # Start fresh
```

---

## Command-Line Interface

Run the interactive menu:

```bash
python main.py
```

### Example Workflow

1. **Email Generation**: Generate meeting notes email (30 seconds)
2. **Meeting Summarization**: Extract key points from transcript (1 minute)
3. **Task Planning**: Break down project into tasks (2 minutes)
4. **Chatbot**: Ask follow-up questions (ongoing)

---

## Best Practices

### Email Generation
- Be specific about tone and recipient
- Provide relevant context for personalization
- Use professional tone for formal communications

### Meeting Summarization
- Provide complete transcripts for accuracy
- Use "detailed" format for comprehensive summaries
- Use "executive" format for quick overviews

### Task Planning
- Set realistic deadlines
- Define clear project scope
- Include team size for resource planning

### Research Assistance
- Be specific with focus areas
- Use "comprehensive" for deep dives
- Cite sources for verification

### Chatbot
- Provide context for personalized advice
- Ask follow-up questions for clarity
- Reset conversation between unrelated topics

---

## Tips for Better Results

1. **Detailed Input** → Better Output
   - More context = more accurate results
   - Be specific about requirements
   - Include relevant background information

2. **Experiment with Tones**
   - Try different tones for variety
   - Match tone to audience
   - Professional for formal, friendly for casual

3. **Use Multiple Features**
   - Generate email → Summarize response → Plan follow-up
   - Research topic → Plan project → Create tasks
   - Combine features for complete workflow

4. **Iterate and Refine**
   - Review generated content
   - Regenerate with refined prompts
   - Use chatbot to brainstorm improvements

---

## Troubleshooting

### API Errors
- Check your API keys in `config/api_keys.env`
- Verify you have sufficient API credits
- Check internet connection

### Generation Issues
- Provide more context in your prompts
- Be more specific about requirements
- Try reformulating your request

### Performance
- Keep transcripts reasonably sized
- Use briefer prompts for faster responses
- Consider API rate limits

---

## Need Help?

1. Check the [README.md](../README.md) for overview
2. Review [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) for optimization
3. Open an issue on GitHub
4. Check API documentation for specific providers
