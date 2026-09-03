"""
Task Planning Module
Breaks down projects into actionable tasks and creates plans
"""

import os
from openai import OpenAI
from datetime import datetime, timedelta

class TaskPlanner:
    """Create and manage task plans for projects"""
    
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"
    
    def create_plan(self, project: str, deadline: str = "", scope: str = "", team_size: int = 1) -> dict:
        """
        Create a project plan with tasks
        
        Args:
            project: Project name/description
            deadline: Project deadline (YYYY-MM-DD format)
            scope: Project scope and details
            team_size: Number of team members
            
        Returns:
            Dictionary with project plan and tasks
        """
        prompt = f"""Create a detailed project plan for the following:

Project: {project}
Deadline: {deadline}
Scope: {scope}
Team Size: {team_size} members

Please provide:
1. PROJECT OVERVIEW: Brief project description
2. PROJECT PHASES: Main phases/milestones
3. TASKS: Detailed list of tasks with task description, estimated hours, priority, and dependencies
4. TIMELINE: Suggested timeline for completion
5. RISKS: Potential risks and mitigation strategies
6. SUCCESS CRITERIA: How to measure project success

Format with clear sections and bullet points."""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert project manager. Create detailed, realistic, and well-structured project plans."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        return {
            "project_name": project,
            "plan": response.choices[0].message.content,
            "created_at": datetime.now().isoformat(),
            "deadline": deadline
        }
