# Prompt Engineering Guide

## Introduction

Prompt engineering is the art and science of crafting effective prompts to get the best results from AI models. This guide covers the techniques used in this AI Productivity Assistant.

---

## Core Principles

### 1. **Role-Based Prompts**

Define clear roles for the AI to adopt:

```
"You are a professional email writer..."
"You are an expert project manager..."
"You are a meeting analyst..."
```

**Benefits:**
- Consistent tone and style
- Domain-specific expertise simulation
- Better quality outputs

### 2. **Context Optimization**

Provide relevant background:

```
✓ Good: "Generate an email to my manager about the Q3 project completion"
✗ Poor: "Generate an email"
```

**Techniques:**
- Specify recipient and relationship
- Include project/situation details
- Mention constraints or requirements

### 3. **Output Formatting**

Specify desired output structure:

```
"Format the response as:
1. Summary (2-3 sentences)
2. Key Points (bulleted list)
3. Action Items (numbered list)
4. Next Steps"
```

**Benefits:**
- Consistent structure
- Easy to parse and use
- Better readability

### 4. **Few-Shot Learning**

Include examples for consistency:

```
"Generate an email in this style:

Example:
Subject: Project Update
Body: [example email]

Now generate an email about..."
```

---

## Technique-Specific Guides

### Email Generation

**Effective Prompt Structure:**

```
Generate a {tone} email with these details:
- Topic: {topic}
- Recipient: {recipient}
- Context: {context}
- Key Points: {points to cover}

Requirements:
- Professional greeting
- 2-3 clear paragraphs
- Specific call-to-action
- Professional closing

Email:
```

**Tone Options:**
- Professional: Business, formal
- Friendly: Warm, approachable
- Formal: Strict, ceremonial
- Casual: Relaxed, conversational

**Pro Tips:**
- Include key information to address
- Specify any tone requirements
- Mention the purpose/goal
- Note any constraints (length, urgency)

### Meeting Summarization

**Effective Prompt Structure:**

```
Analyze this meeting transcript and provide:

1. SUMMARY ({format} overview)
2. KEY POINTS (3-5 most important)
3. ACTION ITEMS (with owners and deadlines)
4. DECISIONS (what was decided)
5. NEXT STEPS (what happens next)
6. PARTICIPANTS (key people mentioned)

Format: Use clear headers and bullet points
```

**Format Options:**
- Brief: 100-150 words
- Detailed: Comprehensive coverage
- Executive: High-level overview

**Pro Tips:**
- Clean up transcripts before processing
- Specify desired depth/length
- Request specific extraction (action items only, decisions, etc.)
- Ask for participant identification

### Task Planning

**Effective Prompt Structure:**

```
Create a detailed plan for this project:

Project: {name}
Deadline: {date}
Scope: {description}
Team: {size} members

Provide:
1. PROJECT OVERVIEW
2. PHASES/MILESTONES
3. DETAILED TASKS (with estimates, priority, dependencies)
4. TIMELINE
5. RISKS & MITIGATION
6. SUCCESS CRITERIA

Format: Use headers and bullet points for clarity
```

**Pro Tips:**
- Be specific about deliverables
- Define team size for resource planning
- Mention any constraints
- Specify task detail level needed
- Include success metrics

### Research Assistance

**Effective Prompt Structure:**

```
Conduct {depth} research on: {topic}

Focus areas: {specific areas of interest}

Provide:
1. OVERVIEW (summary)
2. KEY CONCEPTS (definitions)
3. CURRENT STATE (developments)
4. TRENDS (patterns)
5. CHALLENGES (limitations)
6. OPPORTUNITIES (emerging)
7. RECOMMENDATIONS (actions)
8. RESOURCES (for learning)

Be: Factual, balanced, well-sourced
```

**Depth Options:**
- Overview: High-level summary
- Detailed: Specific focus areas
- Comprehensive: Complete analysis

**Pro Tips:**
- Specify focus areas for relevance
- Request source citations
- Define depth to control output length
- Ask for actionable insights

### Chatbot Interactions

**Effective Prompt Structure:**

```
You are an AI Productivity Assistant. Help users with:
- Task planning
- Time management
- Meeting preparation
- Email writing
- Research
- Project management

Be: Helpful, professional, concise, actionable
```

**Pro Tips:**
- Set context at the start
- Ask clarifying questions
- Provide multi-step solutions
- Suggest next steps
- Adapt to conversation flow

---

## Advanced Techniques

### 1. **Chain of Thought**

Break complex tasks into steps:

```
"To solve this, first:
1. Identify key components
2. Analyze relationships
3. Generate recommendations
4. Format results"
```

### 2. **Temperature Control**

Adjust creativity vs consistency:

- **Lower (0.3-0.5)**: Factual, consistent (summaries, lists)
- **Higher (0.7-0.9)**: Creative, varied (brainstorming)

### 3. **Token Optimization**

Control output length:

```
"Provide a {100-150 word} summary"
"Keep response to 3-5 bullet points"
"Write 2 paragraphs maximum"
```

### 4. **System Prompts**

Set overall behavior:

```python
system_prompt = "You are a professional project manager. 
Create realistic, detailed plans focusing on team success."
```

---

## Common Patterns

### Pattern 1: Refinement Loop

```
Initial Prompt → Review Output → Refine Prompt → Better Results
```

**Example:**
1. "Summarize this meeting" → Too brief
2. "Provide a detailed summary with action items and decisions" → Better

### Pattern 2: Multi-Step Processing

```
1. Generate base content
2. Refine with specific feedback
3. Format according to requirements
4. Validate against criteria
```

### Pattern 3: Context Building

```
1. Provide background context
2. Specify constraints
3. Define success criteria
4. Request structured output
```

---

## Optimization Checklist

Before using a prompt, verify:

- [ ] **Clear Role**: Does AI know what role to play?
- [ ] **Sufficient Context**: Is there enough background?
- [ ] **Specific Output**: Is the format defined?
- [ ] **Constraints**: Are limitations specified?
- [ ] **Examples**: Are sample outputs provided (if needed)?
- [ ] **Tone**: Is the desired tone explicit?
- [ ] **Length**: Is output length controlled?
- [ ] **Metrics**: Are success criteria defined?

---

## Common Mistakes & Fixes

| Mistake | Fix |
|---------|-----|
| Too vague | Add specific details and context |
| Unclear format | Specify exact output structure |
| Missing role | Define AI's role explicitly |
| No constraints | Set length, tone, style limits |
| Ambiguous requirements | Use examples or templates |
| Poor input data | Clean and structure data first |
| Low creativity | Increase temperature setting |
| Inconsistent results | Decrease temperature, add examples |

---

## Templates by Use Case

### Email Generation Template

```
Role: Professional business email writer
Task: Write a {tone} email
To: {recipient}
About: {subject}
Context: {situation}
Key points: {what to include}
Constraints: {any limits}
Format: Subject line + body
```

### Meeting Summary Template

```
Role: Expert meeting analyst
Task: Summarize meeting
Format: {brief/detailed/executive}
Extract: {what to focus on}
Structure: {headers, bullets, tables}
Length: {target length}
Participants: {named/anonymous}
```

### Task Planning Template

```
Role: Expert project manager
Task: Create project plan
Project: {name}
Scope: {description}
Timeline: {deadline}
Resources: {team size}
Focus: {what matters most}
Output: {structure needed}
```

---

## Practice Exercises

### Exercise 1: Email Refinement
1. Write a basic email prompt
2. Review output
3. Add more specificity
4. Compare results

### Exercise 2: Summary Optimization
1. Create a meeting summary prompt
2. Try different formats (brief/detailed)
3. Adjust focus areas
4. Measure improvement

### Exercise 3: Plan Development
1. Start with basic project description
2. Add constraints and timeline
3. Include team information
4. Evaluate comprehensiveness

---

## Resources

- **OpenAI Prompt Engineering**: https://platform.openai.com/docs/guides/prompt-engineering
- **Best Practices**: Check API documentation for your provider
- **Community Tips**: Review GitHub issues and discussions

---

## Continuous Improvement

1. **Track what works**: Document effective prompts
2. **Test variations**: Experiment with different approaches
3. **Measure results**: Evaluate output quality
4. **Share learnings**: Contribute improvements
5. **Iterate**: Refine based on real-world usage

---

*Remember: The key to great AI results is clear, specific, well-structured prompts with sufficient context and explicit requirements.*
